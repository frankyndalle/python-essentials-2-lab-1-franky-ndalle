# Python Essentials 2 — Lab 1
## Modules, Packages, and PIP

**Author:** Franky Ndalle

## Task 1: Built-in Modules

File: `builtin_usage.py`

This program uses the `math`, `random`, and `platform` modules to generate a random integer between 1 and 100, calculate and round down its square root, identify the operating system, and display the Python version.

## Task 2: Creating a Package

Package: `mypackage`

Files:
- `mypackage/__init__.py`
- `mypackage/utilities.py`
- `use_utilities.py`

The package contains a greeting function and a factorial function. The main program imports the package and demonstrates both functions.

## Task 3: Installing an External Package

File: `external_package.py`

This program uses Colorama to display colored terminal messages.

Install the dependency with:

```bash
python -m pip install -r requirements.txt
```

## How to Run

Run these commands from the project folder:

```bash
python builtin_usage.py
python use_utilities.py
python external_package.py
```

## Example Outputs

The `outputs` folder contains text output evidence for all three programs.

## Requirements

- Python 3
- Colorama (listed in `requirements.txt`)
