#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Plagiarism Analyzer using Artificial Intelligence
File: preprocessing.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-05
Updated: 2025-11-05
License: MIT License (see LICENSE file for details)
=

Description:
Text preprocessing utilities: normalization, punctuation removal, and token
preparation for vectorization.

Usage:
from plagiarism_analyzer.preprocessing import preprocess_corpus

Notes:
- Keep preprocessing relatively light to avoid destroying semantic information.
=================================================================================================================
"""

from __future__ import annotations

import re
from typing import Iterable, List

_WHITESPACE_RE = re.compile(r"\s+")
_PUNCT_RE = re.compile(r"[^\w\s]")


def normalize_whitespace(text: str) -> str:
    """Collapse consecutive whitespace characters into single spaces.

    Parameters
    ----------
    text:
        Raw input text.
    """

    return _WHITESPACE_RE.sub(" ", text).strip()


def remove_punctuation(text: str) -> str:
    """Remove punctuation characters while keeping word boundaries.

    Parameters
    ----------
    text:
        Normalized text.
    """

    return _PUNCT_RE.sub("", text)


def basic_preprocess(text: str) -> str:
    """Perform basic text preprocessing.

    Steps:
    - Lowercase
    - Normalize whitespace
    - Remove punctuation
    """

    lowered = text.lower()
    normalized = normalize_whitespace(lowered)
    no_punct = remove_punctuation(normalized)
    return normalize_whitespace(no_punct)


def preprocess_corpus(texts: Iterable[str]) -> List[str]:
    """Preprocess an iterable of texts into a clean corpus.

    Parameters
    ----------
    texts:
        Iterable of raw documents.

    Returns
    -------
    list[str]
        Preprocessed text documents.
    """

    return [basic_preprocess(t) for t in texts]