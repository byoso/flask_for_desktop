#! /usr/bin/env python3
# coding: utf-8

"""
REMINDER:
1- build
./setup.py sdist bdist_wheel
2- basic verifications
twine check dist/*
2.5- Deploy on testpypi (optionnal, site here : https://test.pypi.org/):
twine upload --repository testpypi dist/*
3- upload to PyPi
twine upload dist/*
"""

from flask_fd import __version__
import pathlib
from setuptools import setup


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="flask-fd",
    version=f"{__version__}",
    description=(
        "Use flask to create a desktop GUI"
        ),
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/byoso/flask_for_desktop",
    author="Vincent Fabre",
    author_email="peigne.plume@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
    ],
    packages=[
        "flask_fd",
        "flask_fd.gui",
        "flask_fd.launchers",
        "flask_fd.plop",
        "flask_fd.plop.flask",
        "flask_fd.plop.installer",
        "flask_fd.plop.icon",
        ],
    # include_package_data=True,
    package_data={'': ['FlaskFdIcon', 'installer']},
    python_requires='>=3.6',
    install_requires=[
        "flamewok >= 1.0.8",
    ],
    keywords='flask desktop gui',
    entry_points={
        "console_scripts": [
            "flask-fd=flask_fd.cmd:cmd",
        ]
    },
    setup_requires=['wheel'],
)
