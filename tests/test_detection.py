#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Plagiarism Analyzer using Artificial Intelligence
File: test_detection.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-05
Updated: 2025-11-05
License: MIT License (see LICENSE file for details)
=

Description:
Unit tests for core plagiarism detection logic.

Usage:
pytest tests/test_detection.py
=================================================================================================================
"""

from plagiarism_analyzer.detection import Document, analyze_documents


def test_analyze_documents_detects_similar_pair() -> None:
    docs = [
        Document(doc_id="a", text="This is a simple test document." * 3),
        Document(doc_id="b", text="This is a simple test document." * 3),
        Document(doc_id="c", text="Completely different content that should not match heavily." * 3),
    ]

    pairs = analyze_documents(docs, threshold=0.8)
    ids = {(p.doc_id_a, p.doc_id_b) for p in pairs}

    assert ("a", "b") in ids or ("b", "a") in ids


def test_analyze_documents_ignores_very_short_docs() -> None:
    docs = [
        Document(doc_id="short", text="too short"),
        Document(doc_id="other", text="This is a longer piece of text that should remain." * 2),
    ]

    pairs = analyze_documents(docs, threshold=0.1)
    assert pairs == []