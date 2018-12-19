#!/usr/bin/env python
from distutils.core import setup
import os

from select_multiple_field import __version__

cmdclasses = {}
README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.rst')
long_description = open(README_PATH, 'r').read()


setup(
    name='django-select-multiple-field',
    description='Select multiple choices in a single Django model field',
    long_description=long_description,
    version=__version__,
    license='BSD',
    keywords=[
        'select', 'select multiple', 'Django', 'model-field',
        'Django-Select-Multiple-Field'
    ],
    author='Kelvin Wong',
    author_email='code@kelvinwong.ca',
    url='https://github.com/smenateam/django-select-multiple-field',
    classifiers=[],
    packages=['select_multiple_field'],
    cmdclass={}
)
