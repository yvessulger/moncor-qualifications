#!/usr/bin/env python3
"""Assemble dashboard-dossiers.html : insère SheetJS dans la page pour un fonctionnement 100 % hors-ligne."""
from pathlib import Path

here = Path(__file__).parent
src = (here / "dashboard-dossiers.src.html").read_text(encoding="utf-8")
lib = (here / "xlsx-0.18.5.full.min.js").read_text(encoding="utf-8")
assert "</script" not in lib.lower()
out = src.replace("/*__XLSX_LIB__*/", lib, 1)
(here.parent / "dashboard-dossiers.html").write_text(out, encoding="utf-8")
print("dashboard-dossiers.html", len(out.encode()), "octets")
