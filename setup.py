from pathlib import Path

from setuptools import setup, find_packages

README = Path(__file__).parent / "README.md"
long_description = README.read_text(encoding="utf-8")

setup(
    name="app-store-asset-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "crawl4ai>=0.7.0",
        "aiohttp>=3.8.0",
        "beautifulsoup4>=4.12.0",
        "python-dotenv>=1.0.0",
        "reportlab>=4.0.0",
        "Pillow>=10.0.0",
        "typer>=0.9.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "app-store-asset-cli=app_store_asset_cli.main:app",
        ],
    },
    python_requires=">=3.8",
    description="Download App Store logos and screenshots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Your Name",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
