# -*- coding: utf-8 -*-
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TIA Portal Openness 技术文档'
copyright = '2026, Siemens AG'
author = 'Siemens AG'
release = 'V17.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.githubpages',
]

myst_enable_extensions = [
    'amsmath',
    'attrs_inline',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'html_admonition',
    'html_image',
    'linkify',
    'replacements',
    'smartquotes',
    'strikethrough',
    'substitution',
    'tasklist',
]

# MyST default roles
myst_default_role = 'code'
myst_default_flavor = 'markdown'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static', 'images']

# Alabaster theme configuration
html_theme_options = {
    'canonical_url': '',
    'logo': None,
    'description': 'TIA Portal Openness 技术文档',
    'github_user': 'opendatalab',
    'github_repo': 'MinerU-Ecosystem',
    'github_banner': True,
    'travis_button': False,
    }

# -- Options for myst_parser -------------------------------------------------
# Enable LaTeX rendering for math expressions
myst_number_code_blocks = ['python', 'csharp', 'javascript', 'xml']

# -- Options for toctree -----------------------------------------------------
# Document language
language = 'zh_CN'

# -- Options for PDF output (if using sphinxcontrib-bibtex or similar) --------
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
}
