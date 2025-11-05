#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Plagiarism Analyzer using Artificial Intelligence
File: __init__.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-05
Updated: 2025-11-05
License: MIT License (see LICENSE file for details)
=

Description:
Package initialization for the plagiarism_analyzer module. Exposes high-level
APIs for programmatic use.

Usage:
from plagiarism_analyzer import analyze_folder, analyze_csv

Notes:
- This file centralizes the most important public functions.
=================================================================================================================
"""

from .config import DEFAULT_THRESHOLD
from .detection import analyze_csv, analyze_folder

__all__ = ["DEFAULT_THRESHOLD", "analyze_folder", "analyze_csv"]

__version__ = "0.1.0"