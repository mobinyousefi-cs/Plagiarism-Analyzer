# Plagiarism Analyzer using Artificial Intelligence

An end-to-end **plagiarism detection tool** written in Python. It uses classic NLP
and machine learning (TF–IDF vectorization + cosine similarity) to measure
similarity between documents and flag potentially plagiarized text.

> Author: **Mobin Yousefi** ([GitHub: mobinyousefi-cs](https://github.com/mobinyousefi-cs))

---

## ✨ Features

- Load raw text documents from:
  - A folder of `.txt` files, or
  - A CSV file with `id` and `text` columns
- Clean and normalize text (lowercasing, punctuation removal, whitespace fix)
- Vectorize documents with **TF–IDF**
- Compute **cosine similarity** between all document pairs
- Flag suspicious pairs above a configurable similarity threshold
- Export results as **CSV** or **JSON** reports
- Simple **command-line interface (CLI)**
- Production-ready structure: `src/` layout, tests, CI, Black + Ruff

---

## 🏗 Project Structure

```text
plagiarism-analyzer-ai/
├─ pyproject.toml          # Build configuration & dependencies
├─ README.md               # Project documentation
├─ LICENSE                 # MIT license
├─ .gitignore              # Ignore Python build & cache files
├─ .editorconfig           # Consistent editor settings
├─ .github/
│  └─ workflows/
│     └─ ci.yml            # GitHub Actions: lint + tests
├─ src/
│  └─ plagiarism_analyzer/
│     ├─ __init__.py       # Package metadata
│     ├─ config.py         # Global settings and defaults
│     ├─ preprocessing.py  # Text cleaning utilities
│     ├─ features.py       # TF–IDF and similarity helpers
│     ├─ detection.py      # Core plagiarism detection logic
│     ├─ report.py         # Report generation (CSV / JSON)
│     └─ cli.py            # Command-line interface
└─ tests/
   ├─ __init__.py
   ├─ test_preprocessing.py
   └─ test_detection.py
```

---

## 🚀 Installation

```bash
# Clone your repository
git clone https://github.com/mobinyousefi-cs/plagiarism-analyzer-ai.git
cd plagiarism-analyzer-ai

# (Optional) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate

# Install in editable mode with dev dependencies
pip install -e .[dev]
```

---

## 🧪 Quick Start

### 1. Prepare a Dataset

You can use either:

1. A **folder of .txt files**:
   - `data/essay1.txt`
   - `data/essay2.txt`
   - `data/source_article.txt`

2. Or a **CSV file** with at least:

```csv
id,text
essay1,"This is the first essay ..."
essay2,"This is another essay ..."
```

### 2. Run from the Command Line

```bash
# Analyze a folder of .txt files
plagiarism-analyzer --input-path ./data --threshold 0.8 --output ./reports/report.csv

# Analyze a CSV file
plagiarism-analyzer --input-path ./data/essays.csv --threshold 0.85 --output ./reports/report.json
```

The output file will contain all document pairs with similarity above the
specified threshold.

---

## ⚙️ CLI Usage

```bash
plagiarism-analyzer --help
```

Output:

```text
usage: plagiarism-analyzer [-h] --input-path INPUT_PATH [--threshold THRESHOLD]
                           [--output OUTPUT]

Analyze documents for potential plagiarism using TF-IDF and cosine similarity.

options:
  -h, --help            show this help message and exit
  --input-path INPUT_PATH
                        Path to a folder of .txt files or a CSV file with 'id'
                        and 'text' columns.
  --threshold THRESHOLD
                        Similarity threshold in [0, 1] above which pairs are
                        flagged as suspicious (default: 0.8).
  --output OUTPUT       Optional output path (.csv or .json). If omitted, shows
                        a short summary in the console.
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📂 Example Datasets

For real research or production, you can use datasets such as:

- Student essays and reference materials from your university LMS
- Public plagiarism detection benchmarks (e.g., PAN workshop corpora)

> ⚠️ Always ensure that you have the right to process and store the texts you
> use.

---

## 📄 License

This project is released under the [MIT License](LICENSE).

---

## 🧠 Future Improvements

- Use **pre-trained language models** (e.g., Sentence-BERT) for better semantic
  similarity
- Add **character-level n-gram** similarity for obfuscated plagiarism
- Add a lightweight **web UI** for interactive analysis
- Visualize similarity as a **heatmap** between documents