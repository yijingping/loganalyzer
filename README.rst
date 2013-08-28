.. 

loganalyzer
======================

Quickstart
----------

To bootstrap the project::

    virtualenv loganalyzer
    source loganalyzer/bin/activate
    cd path/to/loganalyzer/repository
    pip install -r requirements.pip
    pip install -e .
    cp loganalyzer/settings/local.py.example loganalyzer/settings/local.py
    manage.py syncdb --migrate

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
