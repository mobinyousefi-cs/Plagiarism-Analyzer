#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Plagiarism Analyzer using Artificial Intelligence
File: features.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-05
Updated: 2025-11-05
License: MIT License (see LICENSE file for details)
=

Description:
Feature extraction utilities based on TF-IDF vectorization and cosine
similarity.

Usage:
from plagiarism_analyzer.features import build_tfidf_matrix, cosine_similarity_matrix

Notes:
- Uses scikit-learn's TfidfVectorizer under the hood.
=================================================================================================================
"""

from __future__ import annotations

from typing import List, Tuple

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def build_tfidf_matrix(corpus: List[str]) -> Tuple[TfidfVectorizer, np.ndarray]:
    """Build a TF-IDF matrix for the given corpus.

    Parameters
    ----------
    corpus:
        List of preprocessed text documents.

    Returns
    -------
    vectorizer, matrix
        The fitted TfidfVectorizer and the resulting TF-IDF matrix.
    """

    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(corpus)
    return vectorizer, matrix


def cosine_similarity_matrix(matrix: np.ndarray) -> np.ndarray:
    """Compute the pairwise cosine similarity matrix.

    Parameters
    ----------
    matrix:
        TF-IDF feature matrix.

    Returns
    -------
    np.ndarray
        Dense cosine similarity matrix with shape (n_docs, n_docs).
    """

    return cosine_similarity(matrix)