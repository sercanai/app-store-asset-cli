# App Store Asset CLI

A command-line tool that pulls App Store logos and screenshots from multiple countries, combines them into structured JSON, and optionally generates a PDF report with each country’s assets.

## Features
- download logos + screenshots per country (default `us,tr,jp`) with optional language overrides
- stores metadata in `download_report.json` and prints a rich summary table
- builds `assets_report.pdf` that lists every country, shows the logo, and lays out the screenshots
- configurable output directory, PDF generation toggle, and country/language filters

## Installation
Install from PyPI for normal CLI usage:
```bash
python -m pip install app-store-asset-cli
```

For local development:
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

## Türkçe

### Özellikler
- Çok ülkeyle App Store ikon ve ekran görüntüleri indirir (varsayılan `us,tr,jp`) ve dil geçersiz kılmaları almanızı sağlar.
- İndirilen meta verileri `download_report.json` içinde saklar ve zengin özet tablosu basar.
- Her ülke için logo ve ekran görüntülerini PDF’e yerleştirerek `assets_report.pdf` oluşturur.
- Çıktı klasörünü, PDF üretimini ve ülke/dil filtrelerini yapılandırabilirsiniz.

### Kurulum
CLI'yi doğrudan kurmak için:
```bash
python -m pip install app-store-asset-cli
```

Geliştirme yapmak isterseniz:
```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

### Kullanım
```bash
app-store-asset-cli assets download <app_id>
```
Varsayılan olarak `us,tr,jp` ülkelerine bakar. İndirme davranışını şu parametrelerle özelleştirin:

- `--countries us,tr,gb` ile farklı ülke kodları tanımlayın.
- `--languages tr:tr-tr,jp:ja-jp` ile özel lokal ayarları zorlayın.
- `--output-dir ./my_assets` ile raporların kaydedildiği klasörü değiştirin.
- `--no-pdf` ile PDF raporunu atlayın, sadece JSON ve resimleri alın.

Örnek:
```bash
app-store-asset-cli assets download 123456789 --countries tr,gb --languages tr:tr-tr --output-dir ./downloads
```

### Çıktı Düzeni
`<output_dir>/<app_name>/` altında dosyalar oluşur. Her ülke kendi klasöründe logo ve ekran görüntülerini barındırır (`…/tr`, `…/gb`). Kök klasörde ayrıca:

- `download_report.json` (özet + ülke bazlı meta verileri)
- `assets_report.pdf` (her ülke için sayfa, lokal logolar/screen shot’lar)

Komutu tekrar çalıştırırsanız ilgili klasör yeniden oluşturulup resimler üzerine yazılır.

<a href="https://github.com/unclecode/crawl4ai">
  <img src="https://raw.githubusercontent.com/unclecode/crawl4ai/main/docs/assets/powered-by-light.svg" alt="Powered by Crawl4AI" width="200"/>
</a>
