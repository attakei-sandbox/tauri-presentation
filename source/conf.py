# -- Project information
project = "Tauri presentation"
copyright = "2022, Kazuya Takei"
author = "Kazuya Takei"
release = "2022.7"
# -- General configuration
extensions = [
    "sphinx_revealjs",
]
templates_path = ["_templates"]
language = "ja"
exclude_patterns = []

# -- Options for HTML output
html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for REVEALJS output
revealjs_static_path = ["_static"]
