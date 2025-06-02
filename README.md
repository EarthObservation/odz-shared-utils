# IAPŠ ODZ Shared Utilities Repository

This repository contains a collection of useful scripts, functions, and Jupyter notebooks developed by our department. It is intended for internal use, collaboration, and sharing of common tools.

---

## Structure
- `cheat_sheets/`: Any documents with tips and tricks for coding, workflows and more.
- `scripts/`: Standalone scripts for various processing tasks.
- `notebooks/`: Example notebooks showcasing workflows or analyses.
- `functions/`: Reusable modules grouped by domain (e.g. lidar, geospatial).
- `tests/`: Unit tests for core functions.

## Contributing
Please read `CONTRIBUTING.md` for guidelines on how to contribute.

## Python File Docstring Format
Each Python file should begin with a module-level docstring that includes:
- **Date of creation**
- **Author**
- **Short description** of what the script or module does

### Example:
```python
"""
Created on 2025-04-17
Author: Jane Doe

This script provides utility functions to clean and normalize raw tabular datasets.
"""
```

## Jupyter Notebook Header Format
At the beginning of each Jupyter notebook, include a Markdown cell with the following metadata:
- **Title**
- **Date of creation**
- **Author**
- **Short description** of what the notebook demonstrates or analyses

### Example:
```markdown
# Lidar DEM Filtering Example

**Date:** 2025-04-17  
**Author:** Jane Doe  
**Description:** This notebook demonstrates how to filter noise from a high-resolution lidar-derived DEM using a median filter.
```
```

---

## requirements.txt (optional) (TBA)

```
numpy
pandas
matplotlib
jupyter
```

---

## setup.py (optional) (TBA)

```python
from setuptools import setup, find_packages

setup(
    name="shared_utils",
    version="0.1",
    packages=find_packages(where="functions"),
    package_dir={"": "functions"},
)
```

---

## GitHub Actions: python-tests.yml (optional) (TBA)

```yaml
name: Python Tests

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest
      - name: Run tests
        run: |
          pytest tests/
```

---

## LICENSE (MIT License)

```
MIT License

Copyright (c) 2025 ZRC SAZU

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---