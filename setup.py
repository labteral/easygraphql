#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages
from pathlib import Path
import re

ROOT = Path(__file__).parent
VERSION = re.search(r"^__version__ = '([^']+)'",
                    (ROOT / 'easygraphql/__init__.py').read_text(), re.M)[1]

setup(
    name='easygraphql',
    version=VERSION,
    long_description='A minimal library to interact with GraphQL from Python.',
    long_description_content_type='text/plain',
    python_requires='>=3.10,<4',
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
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=['requests>=2.34.2,<3']
)
