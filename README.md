# PyInspector - Python Code Analyzer

## Overview
This script analyses Python files in a specified directory using `pylint` and `flake8` to check for coding standards, errors, and style issues.
-   `pylint`: more comprehensive and strict, outputs a score (checks for PEP 8 standard, programming errors, code smells, refactoring etc.)
-   `flake8`: faster and simpler, good for CI/CD (checks for logical errors, PEP 8, Cycolmatic (McCabe) Complexity etc.)

## Installation
To run this script, you need to have Python installed along with the following packages:
- pylint
- flake8

Either:
1.  Install globally using brew: brew install pylint flake8
2.  Install in a venv using pip: pip install -r requirements.txt

## Run
-   Navigate to main.py
-   Alter the directory in __main__ to any folder of Python files you would like to analyse
-   Results will be output in the terminal
