# -*- coding: utf-8 -*-
# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

#with open('LICENSE') as f:
#    license = f.read()

setup(
    name='trusspy',
    version='20180816-6',
    description='Truss Solver for Python',
    long_description=readme,
    long_description_content_type='text/x-rst',
    author='Andreas Dutzler',
    author_email='a.dutzler@gmail.com',
    url='https://github.com/adtzlr/trusspy',
    license='GNU GPLv3',
    packages=find_packages(exclude=('tests', 'docs'))
)