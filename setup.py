# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='movies',
    version='0.1.0',
    description='Downloads and prepares movie data',
    long_description=readme,
    author='Judith Wuerfel',
    author_email='judith.wuerfel@outlook.com',
    url='https://github.com/timo-schuerg/formulaone',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
