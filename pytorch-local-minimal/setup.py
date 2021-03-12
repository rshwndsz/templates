#!/usr/bin/env python
import os
import sys
import subprocess
from setuptools import setup, find_packages

if sys.version_info[0:2] < (3, 6):
    raise RuntimeError("Python version >= 3.6 required.")

setup(
    name='projname', # TODO
    version='0.1.0',
    description="Project description", # TODO
    long_description=open("README.md").read(),
    author="Author", # TODO
    url="https://github.com/username/projname", # TODO
    packages=find_packages(include=['projname', 'projname.*']), # TODO
    install_requires=[
        'torch>=1.5',
        'torchvision',
        'pytorch_lightning',
        'numpy',
        'matplotlib',
        'pillow',
        'pytest'
    ],
    extras_require={
        # Use pip install -e .[training]
        # Use pip install -e .\[training\] on zsh
        'training': ['albumentations', 'matplotlib', 'tqdm'],
    },
    tests_require=['pytest'],
)
