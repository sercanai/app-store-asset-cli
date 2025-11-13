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

After installation, crawl4ai expects a Playwright browser binary. Run once:
```bash
python -m playwright install --with-deps chromium
```
This downloads the Chromium engine Playwright uses for scraping.
If you want every Playwright browser available, run:
```bash
python -m playwright install
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
- Birden fazla ülke için App Store ikonlarını ve ekran görüntülerini indirir (varsayılan `us,tr,jp`) ve isteğe bağlı dil eşlemesi yapmanıza izin verir.
- İndirilen meta verileri `download_report.json` dosyasında saklar ve terminalde Rich tabanlı bir özet tablosu gösterir.
- Her ülkenin logosunu ve ekran görüntülerini `assets_report.pdf` dosyasında düzenleyerek ülke bazlı farkları tek bakışta görmenizi sağlar.
- Çıktı klasörünü, PDF üretimini ve ülke/dil filtrelerini bayraklarla kolayca özelleştirebilirsiniz.

### Kurulum
CLI'yi doğrudan kurmak için:
```bash
python -m pip install app-store-asset-cli
```

Yerel geliştirme planlıyorsanız önce bağımlılıkları, ardından editable kurulumu yapın:
```bash
python -m pip install -r requirements.txt
python -m pip install -e .
```

Crawl4AI, Playwright'ın Chromium motoruna ihtiyaç duyar; bir kez çalıştırmanız yeterli:
```bash
python -m playwright install --with-deps chromium
```
Dilerseniz tüm Playwright tarayıcılarını da kurabilirsiniz:
```bash
python -m playwright install
```

### Kullanım
```bash
app-store-asset-cli assets download <app_id>
```
Komut varsayılan olarak `us,tr,jp` ülkelerini tarar. Davranışı aşağıdaki seçeneklerle değiştirebilirsiniz:

- `--countries us,tr,gb` ile farklı ülke listeleri verin (ISO2, virgülle ayrılmış).
- `--languages tr:tr-tr,jp:ja-jp` ile ülke bazlı locale zorlamaları tanımlayın.
- `--output-dir ./my_assets` ile dosyaların kaydedileceği dizini değiştirin.
- `--no-pdf` ile sadece JSON ve indirilen görselleri üretin.

Örnek:
```bash
app-store-asset-cli assets download 123456789 --countries tr,gb --languages tr:tr-tr --output-dir ./downloads
```

### Çıktı Düzeni
Tüm dosyalar `<output_dir>/<app_name>/` altında toplanır. Her ülke için ayrı klasörler oluşur (`…/tr`, `…/gb`); kök dizinde şu özet dosyaları yer alır:

- `download_report.json` (genel özet + ülke bazlı meta veriler)
- `assets_report.pdf` (her ülke için logo + ekran görüntüsü sayfası)

Komutu tekrar çalıştırdığınızda ilgili uygulama klasörü yeniden oluşturulur; mevcut görseller üzerine yazılır.

<a href="https://github.com/unclecode/crawl4ai">
  <img src="https://raw.githubusercontent.com/unclecode/crawl4ai/main/docs/assets/powered-by-light.svg" alt="Powered by Crawl4AI" width="200"/>
</a>
