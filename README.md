# App Store Asset CLI

A Typer + Rich powered CLI that pulls App Store logos and screenshots from multiple countries, combines them into structured JSON, and optionally generates a PDF report with each country’s assets.

## Features
- download logos + screenshots per country (default `us,tr,jp`) with optional language overrides
- stores metadata in `download_report.json` and prints a rich summary table
- builds `assets_report.pdf` that lists every country, shows the logo, and lays out the screenshots
- configurable output directory, PDF generation toggle, and country/language filters

## Installation
```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Usage
```bash
app-store-asset-cli assets download <app_id>
```
By default the command tries `us,tr,jp` with App Store metadata. Customize the downloads with:

- `--countries us,tr,gb` to request a different country list (comma-separated ISO codes)
- `--languages tr:tr-tr,jp:ja-jp` to force specific locales when scraping
- `--output-dir ./my_assets` to place reports somewhere else
- `--no-pdf` if you only need JSON and downloaded images

For example:
```bash
app-store-asset-cli assets download 123456789 --countries tr,gb --languages tr:tr-tr --output-dir ./downloads
```

## Output layout
Files are saved under `<output_dir>/<app_name>/`. Each country gets its own folder (`.../tr`, `.../gb`, etc.) with logos and screenshots. In the root folder you will find:

- `download_report.json` (summary + per-country metadata)
- `assets_report.pdf` (one page per country, localized logos/screenshots)

If you rerun the command, existing images are overwritten because we recreate the folders for that app.

## Contributions
Pull requests, issues, and README improvements are very welcome — feel free to open one when you have a change or suggestion.
