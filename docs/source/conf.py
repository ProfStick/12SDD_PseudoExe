# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('../../pse_ast/'))
sys.path.insert(0, os.path.abspath('../../pseudoexe/'))
sys.path.insert(0, os.path.abspath('../../module1/'))

# -- Docs setup --------------------------------------------------------------
# RTD requires that all the source documents used to build the docs are in or 
# below the source directory. Sometimes this is not ideal for the project 
# directory structure. This routine copies specified files into the source
# directory at the time of RTD production it does not affect the git repository
import shutil

filenames = ['../../README.md', '../pseudoexe.ebnf', '../../fibonacci.pse']

for fn_src in filenames:
    fn_dest = fn_src.strip("../")
    try:
        source = os.path.abspath(fn_src)
        dest = os.path.abspath(fn_dest)
        shutil.copy(source, dest)
    except FileNotFoundError:
        print('{} file not found'.format(source))
    
# -- Project information -----------------------------------------------------

project = 'Aurora 12SDD PseudoExe Language Project'
copyright = '2020, ProfStick'
author = 'ProfStick'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	    'sphinx.ext.autodoc',
	    'sphinx.ext.viewcode', #Add links to highlighted source code
	    'sphinx.ext.napoleon',
	    'sphinx.ext.coverage', # what is this for?
        'recommonmark', # to read markdown
        'sphinx.ext.intersphinx', # to reference other files in the structure eg README.md
        ]

napoleon_google_docstring = True

source_suffix = ['.rst', '.md']
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

master_doc = 'index'
