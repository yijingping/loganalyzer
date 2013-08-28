#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='loganalyzer',
    version='1.0',
    description="",
    author="Lincoln Loop",
    author_email='info@lincolnloop.com',
    url='',
    packages=find_packages(),
    package_data={'loganalyzer': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
