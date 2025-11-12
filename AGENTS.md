# Repository Guidelines

## Project Structure & Module Organization
- `main.py` wires the Typer app, registers the `assets` command group, and renders the fancy Rich help panels when no subcommand is passed.
- `assets.py`, `download_app_assets.py`, `output.py`, `locale_utils.py`, and `validation.py` form the CLI core: `assets.py` holds the Typer command definitions, helpers in `download_app_assets.py`/`output.py` manage download mechanics and report generation, and `locale_utils.py`/`validation.py` keep locale lookups and request validation in one place.
- `config.py` centralizes `dotenv`-driven settings (`APP_STORE_DEFAULT_COUNTRY`, `APP_STORE_DEFAULT_LANGUAGE`, `APP_STORE_HTTP_PROXY`).
- `app_store_assets/` currently mirrors downloaded example data (each folder named after a sample app) and can be referenced when inspecting how downloads are structured.
- Generated content lives under `outputs/<app_name>/`, with each country folder storing logos/screenshots plus the root `download_report.json`/`assets_report.pdf` described in `README.md`.

## Build, Test, and Development Commands
- `python -m pip install -r requirements.txt` installs the runtime dependencies used across downloads, PDF generation, and Rich output.
- `python -m pip install -e .` installs the CLI in editable mode so `app-store-asset-cli` runs from the checkout.
- `app-store-asset-cli assets download <app_id>` is the primary workflow; add `--countries`, `--languages`, `--output-dir`, or `--no-pdf` to customize which locales run and where reports land.

## Coding Style & Naming Conventions
- Follow the existing idiomatic Python style: four-space indentation, expressive docstrings/comments, and descriptive variable names aligned with Typer/Rich conventions.
- Keep helper functions short, return data structures (e.g., dataclasses in `config.py`), and prefer the existing `snake_case` for functions and `UPPER_SNAKE` for environment variables.
- No formatter is enforced, so mimic the current layout when adding files (matching import ordering and line length ~88).

## Testing Guidelines
- There is no automated test suite yet; exercise the CLI directly via `app-store-asset-cli assets download <app_id>` to validate new logic.
- When adding tests in the future, mirror any new module under `tests/` (create the directory) and name files/functions after the functionality being covered (e.g., `test_download_assets.py`).

## Configuration & Environment Tips
- Drop an `.env` file adjacent to the root to override `APP_STORE_DEFAULT_COUNTRY`, `APP_STORE_DEFAULT_LANGUAGE`, or `APP_STORE_HTTP_PROXY` before running the CLI.

## Commit & Pull Request Guidelines
- Commit messages should be short, imperative, and descriptive (see history: “Enhance PDF report…” or “Refactor screenshot download logic…”).
- Pull requests should explain what changed, why it matters, and, when applicable, link the issue or ticket they resolve. Include screenshots or sample output only if the change affects the generated reports or CLI UX.
