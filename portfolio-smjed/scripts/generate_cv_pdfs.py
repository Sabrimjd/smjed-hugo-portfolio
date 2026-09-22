#!/usr/bin/env python3
"""Regenerate the public EN/FR CV PDFs from scripts/cv/*.md.

Requirements:
  python3 -m pip install markdown
  Google Chrome or Chromium available on PATH
"""

from pathlib import Path
import importlib.util
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = Path(__file__).resolve().parent / "cv"
OUTPUT_DIR = ROOT / "static" / "files"
sys.dont_write_bytecode = True


def load_renderer():
    spec = importlib.util.spec_from_file_location("cv_renderer", SOURCE_DIR / "render.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load scripts/cv/render.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def browser_binary() -> str:
    for name in ("google-chrome", "chromium", "chromium-browser"):
        path = shutil.which(name)
        if path:
            return path
    raise RuntimeError("Google Chrome or Chromium is required to render the PDFs")


def pdf_pages(path: Path) -> int | None:
    pdfinfo = shutil.which("pdfinfo")
    if not pdfinfo:
        return None
    output = subprocess.check_output([pdfinfo, str(path)], text=True)
    for line in output.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    return None


def main() -> int:
    try:
        renderer = load_renderer()
    except ModuleNotFoundError as exc:
        if exc.name == "markdown":
            print("Missing dependency: python3 -m pip install markdown", file=sys.stderr)
            return 2
        raise

    browser = browser_binary()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for lang in ("en", "fr"):
        source = SOURCE_DIR / f"sabri-mjahed-cv-{lang}.md"
        html = renderer.render(source)
        output = OUTPUT_DIR / f"sabri-mjahed-cv-{lang}.pdf"
        subprocess.run(
            [
                browser,
                "--headless",
                "--no-sandbox",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--print-to-pdf={output}",
                html.resolve().as_uri(),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        pages = pdf_pages(output)
        if pages is not None and pages != 2:
            raise RuntimeError(f"{output.name} rendered as {pages} pages, expected 2")
        html.unlink(missing_ok=True)
        print(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
