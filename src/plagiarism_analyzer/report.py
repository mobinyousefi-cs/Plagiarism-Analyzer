#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Plagiarism Analyzer using Artificial Intelligence
File: report.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-05
Updated: 2025-11-05
License: MIT License (see LICENSE file for details)
=

Description:
Helpers for converting suspicious pairs into tabular structures and exporting
reports as CSV or JSON.

Usage:
from plagiarism_analyzer.report import pairs_to_dataframe, save_report

Notes:
- Keeps I/O logic separate from the core detection algorithm.
=================================================================================================================
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

from .detection import SuspiciousPair


def pairs_to_dataframe(pairs: Iterable[SuspiciousPair]) -> pd.DataFrame:
    """Convert suspicious pairs into a pandas DataFrame."""

    records = [
        {
            "doc_id_a": p.doc_id_a,
            "doc_id_b": p.doc_id_b,
            "similarity": p.similarity,
        }
        for p in pairs
    ]
    return pd.DataFrame.from_records(records)


def save_report(pairs: Iterable[SuspiciousPair], path: str | Path) -> None:
    """Save suspicious pairs to CSV or JSON based on file extension."""

    output_path = Path(path)
    df = pairs_to_dataframe(pairs)

    if output_path.suffix.lower() == ".csv":
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(output_path, index=False)
    elif output_path.suffix.lower() in {".json", ".jsn"}:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        df.to_json(output_path, orient="records", force_ascii=False, indent=2)
    else:
        raise ValueError("Unsupported output format. Use .csv or .json")