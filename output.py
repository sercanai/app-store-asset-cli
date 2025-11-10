"""Output utilities for ASO CLI."""

import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from rich.console import Console


class OutputManager:
    """Manages output files and directories."""

    def __init__(self, base_dir: str = "outputs"):
        self.base_dir = Path(base_dir)
        self.console = Console()
        self._ensure_directories()

    def _ensure_directories(self) -> None:
        """Create output directories if they don't exist."""
        directories = ["searches", "scrapes", "analyses", "reports"]

        for directory in directories:
            (self.base_dir / directory).mkdir(parents=True, exist_ok=True)

    def get_timestamped_filename(self, prefix: str, extension: str = "json") -> str:
        """Generate a timestamped filename."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{prefix}_{timestamp}.{extension}"

    def save_json(
        self,
        data: Dict[str, Any],
        subdir: str,
        filename: str,
        *,
        app_slug: Optional[str] = None,
    ) -> Path:
        """Save data as JSON file (optionally inside an app-specific subdirectory)."""
        output_dir = self.base_dir / subdir
        if app_slug:
            output_dir = output_dir / app_slug
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / filename

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        self.console.print(f"[green]✓[/green] Saved: {output_path}")
        return output_path

    def load_json(self, filepath: str) -> Dict[str, Any]:
        """Load JSON file."""
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def get_latest_file(self, subdir: str, pattern: str = "*.json") -> Path:
        """Get the most recent file in a subdirectory."""
        directory = self.base_dir / subdir
        files = list(directory.glob(pattern))

        if not files:
            raise FileNotFoundError(f"No files found in {directory}")

        return max(files, key=lambda f: f.stat().st_mtime)

    def print_summary(self, stats: Dict[str, Any]) -> None:
        """Print summary statistics."""
        from rich.table import Table

        table = Table(title="Summary", show_header=False)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")

        for key, value in stats.items():
            table.add_row(key.replace("_", " ").title(), str(value))

        self.console.print(table)

    def derive_app_slug(
        self,
        *,
        app: Optional[Dict[str, Any]] = None,
        app_name: Optional[str] = None,
        app_id: Optional[str] = None,
        store: Optional[str] = None,
    ) -> str:
        """Return a filesystem-safe slug derived from app name/id and store label."""
        if app:
            app_name = app_name or app.get("app_name") or app.get("name") or app.get("title")
            app_id = app_id or app.get("app_id") or app.get("id")
            store = store or app.get("store")

        base_candidate = app_name or app_id or "app"
        base_slug = self._slugify(base_candidate)

        store_slug = self._slugify(store) if store else ""
        if store_slug:
            if not base_slug.endswith(store_slug):
                return f"{base_slug}-{store_slug}"
        return base_slug

    def derive_slug_from_payload(
        self,
        data: Dict[str, Any],
        default: str = "report",
    ) -> str:
        """Infer an app slug from a generic payload (app/app lists/results)."""
        app_entry = data.get("app")
        if isinstance(app_entry, dict):
            return self.derive_app_slug(app=app_entry)

        for key in ("apps", "results"):
            apps = data.get(key)
            if not isinstance(apps, list):
                continue
            for item in apps:
                candidate = item.get("app") if isinstance(item, dict) and isinstance(item.get("app"), dict) else item
                if isinstance(candidate, dict):
                    return self.derive_app_slug(app=candidate)

        return self._slugify(default)

    @staticmethod
    def _slugify(value: Optional[str]) -> str:
        if not value:
            return "app"
        normalized = value.lower()
        normalized = re.sub(r"[^a-z0-9]+", "-", normalized)
        normalized = normalized.strip("-")
        return normalized or "app"
