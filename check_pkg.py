import importlib

# List of libraries to check
libraries = [
    "pandas", "notebook", "numpy", "scikit-learn", "matplotlib", "python_box",
    "pyyaml", "tqdm", "ensure", "joblib", "types_PyYAML", "flask", "flask_cors", "box"
]

# Iterate and check each library
for lib in libraries:
    try:
        importlib.import_module(lib)
        print(f"{lib}: Installed")
    except ImportError:
        print(f"{lib}: Not Installed")
