#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Plagiarism Analyzer using Artificial Intelligence
File: detection.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-05
Updated: 2025-11-05
License: MIT License (see LICENSE file for details)
=

Description:
Core logic for detecting potentially plagiarized document pairs using TF-IDF
and cosine similarity.

Usage:
from plagiarism_analyzer.detection import analyze_folder, analyze_csv

Notes:
- This module is used both by the CLI and by the public package API.
=================================================================================================================
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence

import pandas as pd

from .config import DEFAULT_THRESHOLD, MIN_DOC_LENGTH
from .features import build_tfidf_matrix, cosine_similarity_matrix
from .preprocessing import preprocess_corpus


@dataclass
class Document:
    """Simple container for a document.

    Attributes
    ----------
    doc_id:
        Unique identifier for the document.
    text:
        Raw text content.
    """

    doc_id: str
    text: str


@dataclass
class SuspiciousPair:
    """Suspicious pair of documents and their similarity score."""

    doc_id_a: str
    doc_id_b: str
    similarity: float


def _filter_short_docs(docs: Sequence[Document]) -> List[Document]:
    """Filter out documents that are too short to be meaningful."""

    return [d for d in docs if len(d.text) >= MIN_DOC_LENGTH]


def _detect_pairs(docs: Sequence[Document], threshold: float) -> List[SuspiciousPair]:
    """Internal helper to detect suspicious pairs given documents and threshold."""

    filtered_docs = _filter_short_docs(docs)
    if len(filtered_docs) < 2:
        return []

    corpus = preprocess_corpus([d.text for d in filtered_docs])
    _, matrix = build_tfidf_matrix(corpus)
    sim_matrix = cosine_similarity_matrix(matrix)

    results: List[SuspiciousPair] = []
    n_docs = len(filtered_docs)
    for i in range(n_docs):
        for j in range(i + 1, n_docs):
            score = float(sim_matrix[i, j])
            if score >= threshold:
                results.append(
                    SuspiciousPair(
                        doc_id_a=filtered_docs[i].doc_id,
                        doc_id_b=filtered_docs[j].doc_id,
                        similarity=score,
                    )
                )
    return results


def analyze_documents(docs: Iterable[Document], threshold: float | None = None) -> List[SuspiciousPair]:
    """Analyze an iterable of Document objects for potential plagiarism.

    Parameters
    ----------
    docs:
        Iterable of Document instances.
    threshold:
        Similarity threshold in [0, 1]. Defaults to DEFAULT_THRESHOLD.
    """

    if threshold is None:
        threshold = DEFAULT_THRESHOLD
    doc_list = list(docs)
    return _detect_pairs(doc_list, threshold=threshold)


def analyze_folder(path: str | Path, threshold: float | None = None) -> List[SuspiciousPair]:
    """Analyze all `.txt` files in a folder.

    Parameters
    ----------
    path:
        Path to a directory containing `.txt` files.
    threshold:
        Similarity threshold in [0, 1].
    """

    base = Path(path)
    if not base.is_dir():
        raise ValueError(f"Input path is not a directory: {base}")

    docs: List[Document] = []
    for txt_file in sorted(base.glob("*.txt")):
        text = txt_file.read_text(encoding="utf-8", errors="ignore")
        docs.append(Document(doc_id=txt_file.name, text=text))

    return analyze_documents(docs, threshold=threshold)


def analyze_csv(path: str | Path, threshold: float | None = None) -> List[SuspiciousPair]:
    """Analyze documents defined in a CSV file.

    The CSV must contain at least two columns: `id` and `text`.
    """

    csv_path = Path(path)
    if not csv_path.is_file():
        raise ValueError(f"CSV file does not exist: {csv_path}")

    df = pd.read_csv(csv_path)
    if "id" not in df.columns or "text" not in df.columns:
        raise ValueError("CSV must contain 'id' and 'text' columns")

    docs = [Document(doc_id=str(row["id"]), text=str(row["text"])) for _, row in df.iterrows()]
    return analyze_documents(docs, threshold=threshold)