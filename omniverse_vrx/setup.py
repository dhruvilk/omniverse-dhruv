#!/usr/bin/env python3

# ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD !

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages = ['omniverse_vrx'], # omniverse_vrx/src/omniverse_vrx
    package_dir = {'': 'src'},
)

setup(**setup_args)
