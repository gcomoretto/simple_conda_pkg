""" Simple setup.py
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='mypkg',  # Required
    version='0.0.1',  # Required
    description='A sample Python project',  # Required
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
)
