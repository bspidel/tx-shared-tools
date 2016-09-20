import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(f_name):
    return open(os.path.join(os.path.dirname(__file__), f_name)).read()

setup(
    name="tx-shared-tools",
    version="0.0.5",
    author="unfoldingWord",
    author_email="unfoldingword.org",
    description="A collection of useful scripts abd classes for tX",
    url="https://github.org/unfoldingWord-dev/tx-shared-tools",
    license="MIT",
    keywords="unfoldingWord python tools tx",
    packages=['aws_tools', 'gogs_tools'],
    long_description=read('README.rst'),
    classifiers=[],
    install_requires=[
        'requires',
        'boto3',
        'gogs_client'

    ],
    requires=['pygithub']
)

