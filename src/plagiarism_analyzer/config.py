#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=================================================================================================================
Project: Plagiarism Analyzer using Artificial Intelligence
File: config.py
Author: Mobin Yousefi (GitHub: github.com/mobinyousefi-cs)
Created: 2025-11-05
Updated: 2025-11-05
License: MIT License (see LICENSE file for details)
=

Description:
Global configuration constants and default parameters for the plagiarism
analyzer.

Usage:
from plagiarism_analyzer.config import DEFAULT_THRESHOLD

Notes:
- Adjust the defaults here to tune behavior across the project.
=================================================================================================================
"""

from __future__ import annotations

DEFAULT_THRESHOLD: float = 0.8
MIN_DOC_LENGTH: int = 50  # Minimum number of characters to consider a document