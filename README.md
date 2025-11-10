# App Store Asset CLI

A lightweight Typer + Rich CLI that fetches App Store logos and screenshots for multiple countries, then stores the results as JSON and an optional PDF report.

## Features
- download logos + screenshots per country with optional language overrides
- retains metadata in `download_report.json`
- generates a `assets_report.pdf` with each country’s logo and screenshots (unless `--no-pdf` is used)

## Installation
```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

## Usage
```bash
app-store-asset-cli assets download <app_id>
```
Use `--countries` to set country codes, `--output-dir` to change the destination, and `--no-pdf` to skip the PDF.

## Output
Results live under `<output_dir>/<app_name>/`. JSON and PDF summaries are named `download_report.json` and `assets_report.pdf`, respectively.

## Contributions
Feel free to open issues or send pull requests for improvements.
