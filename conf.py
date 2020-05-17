# Configuration file for the Sphinx documentation builder.
#
# Documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html

# my rules for rest addons
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
import myrules

import datetime
# oggi instead of today: there is another variabile called "today"
oggi = datetime.date.today()
year = oggi.strftime("%Y")
ver = oggi.strftime("%Y%m%d")
# -- Project information -----------------------------------------------------

project = 'Python Course'
copyright = year + ', Andrea Diamantini. License: CC BY-NC-SA 4.0. Version: ' + ver + ". "
author = 'Andrea Diamantini'

# The full version, including alpha/beta/rc tags
version = ver
release = 'latest'


# -- General configuration ---------------------------------------------------

# needed for RTD builds
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'it'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']

# code highlights
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]
