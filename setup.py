#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages
import easygraphql

setup(
    name='easygraphql',
    version=easygraphql.__version__,
    description='A minimal library to interact with GraphQL from Python',
    url='https://github.com/brunneis/easygraphql',
    author='Rodrigo Martínez Castaño',
    author_email='rodrigo@martinez.gal',
    license='GNU General Public License v3 (GPLv3)',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=['requests']
)
