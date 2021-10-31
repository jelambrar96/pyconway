# -*- coding: utf-8 -*-

# Import modules
from setuptools import find_packages, setup


with open("README.md", encoding="utf8") as readme_file:
    readme = readme_file.read()


with open("requirements-lib.txt") as f:
    requirements = f.read().splitlines()

with open("requirements-test.txt") as f:
    test_requirements = f.read().splitlines()


setup (
    name="pyconway",
    version="0.1.0-beta",
    description="Python Library Simulation of Conway's Game",
    long_description=readme,
    author="jelambrar96",
    author_email="jelambrar@gmail.com",
    url="https://github.com/jelambrar96/pyconway",
    packages=find_packages(exclude=["docs", "tests"]),
    include_package_data=True,
    install_requires=requirements,
    tests_require=test_requirements,
    license="MIT license",
    zip_safe=False,
    keywords=["conway game", "game of life"],
    test_suite="tests",
)