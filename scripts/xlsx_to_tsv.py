#!/usr/bin/env python3
"""Convert each sheet of the Supplementary Data workbook to a tab-delimited .txt file.

Usage: python3 scripts/xlsx_to_tsv.py "inputs/Supplementary Data.xlsx" data_tables/
"""
import re
import sys
from pathlib import Path

import openpyxl


def fmt(v):
    if v is None:
        return ""
    if isinstance(v, bool):
        return "TRUE" if v else "FALSE"
    if isinstance(v, float):
        # 15 significant digits matches Excel's displayed precision
        return f"{v:.15g}"
    return str(v).strip()


def file_name(sheet_title):
    num, name = re.match(r"(\d+)\.\s*(.+)", sheet_title).groups()
    slug = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
    return f"supplementary_data_{int(num):02d}_{slug}.txt"


def trim(rows):
    """Drop fully empty rows and columns beyond the last non-empty header cell."""
    ncol = max(i for i, v in enumerate(rows[0]) if v is not None) + 1
    rows = [list(r[:ncol]) + [None] * (ncol - len(r)) for r in rows]
    return [r for r in rows if any(fmt(v) for v in r)]


def cohort_characteristics(rows):
    """Flatten the display-formatted cohort table into one row per characteristic."""
    header = ["characteristic"] + [f"{g} ({n})" for g, n in zip(rows[0][2:], rows[1][2:])]
    out, section = [header], None
    for label, sublabel, *vals in rows[2:]:
        if label and not any(fmt(v) for v in vals):
            section = label
            continue
        name = label if label else f"{section}: {sublabel}"
        if label:
            section = None
        out.append([name] + vals)
    return out


def fill_down(rows, col):
    last = None
    for r in rows[1:]:
        if r[col] is None:
            r[col] = last
        last = r[col]
    return rows


def main(xlsx, outdir):
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    wb = openpyxl.load_workbook(xlsx, read_only=True, data_only=True)
    for ws in wb.worksheets:
        rows = trim([list(r) for r in ws.iter_rows(values_only=True)])
        if ws.title.startswith("2."):
            rows = cohort_characteristics(rows)
        elif ws.title.startswith("4."):
            rows = fill_down(rows, 0)
        path = outdir / file_name(ws.title)
        with open(path, "w", newline="\n", encoding="utf-8") as f:
            for r in rows:
                f.write("\t".join(fmt(v) for v in r) + "\n")
        print(f"{path}\t{len(rows) - 1} rows\t{len(rows[0])} columns")


if __name__ == "__main__":
    main(*sys.argv[1:3])
