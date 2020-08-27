import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="apache-dcg",
    version="0.0.1",
    author="Throw Out Error",
    description=("Generates Apache2 config files for custom domains."),
    license="MIT",
    keywords="apache generation tool",
    url="https://github.com/throw-out-error/apache-dcg",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "apache-dcg=apache_dcg.start:main"
        ],
    },
    long_description=read('README.md'),
    classifiers=[
        "Topic :: Utilities",
    ],
)
