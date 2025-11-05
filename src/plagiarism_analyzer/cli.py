#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Plagiarism Analyzer using Artificial Intelligence
File: cli.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-05
Updated: 2025-11-05
License: MIT License (see LICENSE file for details)
=

Description:
Command-line interface entry point for the plagiarism analyzer.

Usage:
plagiarism-analyzer --input-path ./data --threshold 0.8 --output ./reports/report.csv

Notes:
- Registered as a console script in pyproject.toml.
=================================================================================================================
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

from .config import DEFAULT_THRESHOLD
from .detection import analyze_csv, analyze_folder
from .report import save_report


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Analyze documents for potential plagiarism using TF-IDF and cosine similarity.",
    )
    parser.add_argument(
        "--input-path",
        required=True,
        help=(
            "Path to a folder of .txt files or a CSV file with 'id' and 'text' columns."
        ),
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=DEFAULT_THRESHOLD,
        help=(
            "Similarity threshold in [0, 1] above which pairs are flagged as "
            "suspicious (default: %(default)s)."
        ),
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help=("Optional output path (.csv or .json). If omitted, a short summary is printed."),
    )
    return parser


def main(argv: Optional[list[str]] = None) -> None:
    parser = _build_parser()
    args = parser.parse_args(argv)

    input_path = Path(args.input_path)
    threshold = float(args.threshold)
    output = args.output

    if not input_path.exists():
        raise SystemExit(f"Input path does not exist: {input_path}")

    if input_path.is_dir():
        pairs = analyze_folder(input_path, threshold=threshold)
    elif input_path.is_file() and input_path.suffix.lower() == ".csv":
        pairs = analyze_csv(input_path, threshold=threshold)
    else:
        raise SystemExit(
            "--input-path must be either a directory of .txt files or a .csv file with 'id' and 'text' columns."
        )

    if output:
        save_report(pairs, output)
        print(f"Saved report with {len(pairs)} suspicious pairs to: {output}")
    else:
        print(f"Found {len(pairs)} suspicious pairs with threshold >= {threshold:.2f}")
        for pair in pairs[:10]:
            print(
                f"- {pair.doc_id_a} vs {pair.doc_id_b}: similarity={pair.similarity:.3f}",
            )


if __name__ == "__main__":  # pragma: no cover
    main()