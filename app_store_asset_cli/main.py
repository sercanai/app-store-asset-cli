"""Main CLI entry point using Typer."""

import typer
from rich.console import Console

from . import assets

app = typer.Typer(
    name="app-store-asset-cli",
    help="🚀 App Store Asset CLI - Download App Store assets",
    no_args_is_help=False,  # We'll handle it ourselves
    rich_markup_mode="rich",
    add_completion=False,  # We'll add it manually
    invoke_without_command=True,  # Allow callback to run without command
)

console = Console()

# Add command groups
app.add_typer(assets.app, name="assets", help="🎨 Download app assets (icons, screenshots)")


@app.command()
def help() -> None:
    """Show help guide with examples."""
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text

    # Main header
    header_text = Text("🚀 App Store Asset CLI", style="bold cyan")
    subheader = Text("Download App Store logos and screenshots", style="dim")

    console.print()
    console.print(Panel(header_text + "\n" + subheader, border_style="cyan", padding=(1, 2)))

    # Examples table
    table = Table(title="Examples", show_header=True, header_style="bold magenta")
    table.add_column("Command", style="cyan", width=50)
    table.add_column("Description", style="white")

    table.add_row(
        "app-store-asset-cli assets download 123456789",
        "Download assets for app ID 123456789 (default countries)"
    )
    table.add_row(
        "app-store-asset-cli assets download 123456789 --countries US,TR,GB",
        "Download assets for specific countries"
    )
    table.add_row(
        "app-store-asset-cli assets download 123456789 --output-dir ./my_assets",
        "Save assets to custom directory"
    )
    table.add_row(
        "app-store-asset-cli assets download 123456789 --no-pdf",
        "Skip PDF report generation"
    )

    console.print(table)
    console.print("\n[dim]For detailed help: app-store-asset-cli assets download --help[/dim]")


@app.callback()
def main(
    ctx: typer.Context,
    version: bool = typer.Option(
        False, "--version", "-v", help="Show version and exit"
    ),
    verbose: bool = typer.Option(False, "--verbose", help="Enable verbose output"),
) -> None:
    """App Store Asset CLI - Download App Store logos and screenshots."""

    if version:
        console.print(f"app-store-asset-cli version 0.1.0")
        raise typer.Exit()

    # If no command provided, show beautiful help instead of default
    if ctx.invoked_subcommand is None:
        from rich.panel import Panel
        from rich.text import Text

        # Main header
        header_text = Text("🚀 App Store Asset CLI", style="bold cyan")
        subheader = Text("Download App Store logos and screenshots", style="dim")

        console.print()
        console.print(Panel(header_text + "\n" + subheader, border_style="cyan", padding=(1, 2)))

        examples_panel = Panel(
            "\n".join(
                [
                    "[bold green]📱 Usage Examples[/bold green]",
                    "",
                    "[cyan]app-store-asset-cli assets download 123456789[/cyan]",
                    "  Download assets for app ID 123456789 (default countries)",
                    "",
                    "[cyan]app-store-asset-cli assets download 123456789 --countries US,TR,GB[/cyan]",
                    "  Download assets for specific countries",
                    "",
                    "[cyan]app-store-asset-cli assets download 123456789 --output-dir ./my_assets[/cyan]",
                    "  Save assets to custom directory",
                    "",
                    "[cyan]app-store-asset-cli assets download 123456789 --no-pdf[/cyan]",
                    "  Skip PDF report generation",
                ]
            ),
            border_style="green",
            padding=(1, 2),
        )
        console.print("\n", examples_panel)

        console.print("\n[dim]Run 'app-store-asset-cli help' for detailed examples[/dim]")
        raise typer.Exit()


if __name__ == "__main__":
    app()
