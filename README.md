# IAPŠ ODZ Shared Utilities Repository

This repository contains a collection of useful scripts, functions, and Jupyter notebooks developed by our department. It is intended for internal use, collaboration, and sharing of common tools.

---

## Structure
- `scripts/`: Scripts, functions and code snippets for various processing tasks.
- `notebooks/`: Example notebooks showcasing workflows or analyses.

## Contributing
- Include at least author, date and short description at top of each file
- Write clear, descriptive commit messages
- Follow PEP8 for Python code
- Use meaningful names and add docstrings
- Clean notebook outputs before committing
- Use Issues or GitHub Discussions to suggest features or raise bugs

### Python File Docstring Format
Each Python file should begin with a module-level docstring that includes:
- **Date of creation**
- **Author**
- **Short description** of what the script or module does

**Example:**
```python
"""
Created on 2020-09-03
Author: Janez Novak

This script provides utility functions to clean and normalize raw tabular datasets.
"""
```

### Jupyter Notebook Header Format
* At the beginning of each Jupyter notebook, include a Markdown cell with the following metadata:
    - **Date of creation**
    - **Author**
    - **Short description** of what the notebook demonstrates or analyses

### Example:
```markdown
# Lidar DEM Filtering Example

**Date:** 2020-09-03 
**Author:** Janez Novak  
**Description:** This notebook demonstrates how to filter noise from a high-resolution lidar-derived DEM using a median filter.
```


---