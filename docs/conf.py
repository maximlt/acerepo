"""Sphinx configuration."""
project = "acerepo"
author = "maximlt"
copyright = "2023, maximlt"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
