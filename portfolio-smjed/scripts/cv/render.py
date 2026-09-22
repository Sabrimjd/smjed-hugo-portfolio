#!/usr/bin/env python3
from pathlib import Path
import html
import re
import sys
import markdown

ROOT = Path(__file__).resolve().parent
CSS = r"""
@page { size: A4; margin: 11mm 14mm 12mm 14mm; }
* { box-sizing: border-box; }
html { background: #ffffff; }
body {
  margin: 0;
  color: #172033;
  font-family: "Inter", "Noto Sans", "Liberation Sans", Arial, sans-serif;
  font-size: 9.1pt;
  line-height: 1.35;
  letter-spacing: -0.005em;
}
body.lang-fr {
  font-size: 8.75pt;
  line-height: 1.32;
}
a { color: #1f5d87; text-decoration: none; }
h1 {
  margin: 0 0 1.5mm;
  color: #0d2740;
  font-size: 26pt;
  line-height: 1;
  letter-spacing: 0.035em;
  font-weight: 800;
}
h1 + p {
  margin: 0 0 1.5mm;
  font-size: 9.1pt;
  line-height: 1.4;
}
h1 + p strong {
  color: #0f5d7a;
  font-size: 10.8pt;
  letter-spacing: 0.055em;
}
h2 {
  margin: 4mm 0 1.7mm;
  padding-bottom: 1mm;
  color: #0f5d7a;
  border-bottom: 0.55pt solid #b7c8d4;
  font-size: 9.4pt;
  line-height: 1.1;
  letter-spacing: 0.095em;
  font-weight: 800;
  text-transform: uppercase;
  break-after: avoid;
}
h3 {
  margin: 2.7mm 0 0.8mm;
  color: #0d2740;
  font-size: 10.2pt;
  line-height: 1.14;
  font-weight: 760;
  break-after: avoid;
}
h3 + p {
  margin-top: 0;
  break-after: avoid;
}
p { margin: 0 0 1.4mm; }
ul { margin: 0.7mm 0 1.8mm 4.4mm; padding-left: 2.5mm; }
li { margin: 0 0 0.65mm; padding-left: 0.7mm; }
li::marker { color: #0f7091; }
strong { font-weight: 750; color: #111f32; }
.metric-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2mm;
  margin: 3mm 0 3.2mm;
}
.metric-grid > div {
  min-height: 13mm;
  padding: 2.1mm 2.2mm 1.7mm;
  border: 0.55pt solid #c8d6df;
  border-top: 2.1pt solid #0f7091;
  border-radius: 1.2mm;
  background: #f7fafc;
}
.metric-grid strong {
  display: block;
  color: #0d2740;
  font-size: 12.2pt;
  line-height: 1.05;
  letter-spacing: -0.02em;
}
.metric-grid span {
  display: block;
  margin-top: 0.8mm;
  color: #4e6171;
  font-size: 7.35pt;
  line-height: 1.16;
}
.page-break { break-before: page; page-break-before: always; }
.page2-header {
  margin: 0 0 2mm;
  padding-bottom: 1.2mm;
  border-bottom: 0.7pt solid #8fa8b8;
  color: #587082;
  font-size: 7.6pt;
  font-weight: 700;
  letter-spacing: 0.075em;
}
@media print {
  body { print-color-adjust: exact; -webkit-print-color-adjust: exact; }
  a { color: #1f5d87; }
}
"""

def title_from_markdown(text: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else "CV"

def render(src: Path) -> Path:
    text = src.read_text(encoding="utf-8")
    body = markdown.markdown(text, extensions=["extra", "sane_lists"])
    title = title_from_markdown(text)
    lang = "fr" if src.stem.endswith("-fr") else "en"
    page = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} CV</title>
<style>{CSS}</style>
</head>
<body class="lang-{lang}">{body}</body>
</html>
"""
    out = src.with_suffix(".html")
    out.write_text(page, encoding="utf-8")
    return out

if __name__ == "__main__":
    sources = [Path(x) for x in sys.argv[1:]] or sorted(ROOT.glob("*.md"))
    for src in sources:
        print(render(src))
