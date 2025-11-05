#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Plagiarism Analyzer using Artificial Intelligence
File: test_preprocessing.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-05
Updated: 2025-11-05
License: MIT License (see LICENSE file for details)
=

Description:
Unit tests for the preprocessing utilities.

Usage:
pytest tests/test_preprocessing.py
=================================================================================================================
"""

from plagiarism_analyzer.preprocessing import basic_preprocess, normalize_whitespace


def test_normalize_whitespace_basic() -> None:
    assert normalize_whitespace("Hello   world\n\t!") == "Hello world !"


def test_basic_preprocess_lower_and_punct() -> None:
    text = "Hello, WORLD!!!"
    processed = basic_preprocess(text)
    assert processed == "hello world"