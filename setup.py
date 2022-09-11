from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.7'
DESCRIPTION = 'API Wrapper and CLI for Metlink API'
LONG_DESCRIPTION = '''A python package to easily access
infomation from the official metlink api, either through python or CLI.'''

# Setting up
setup(
    name="metlink-python",
    version=VERSION,
    author="Harry Ludemann",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['urllib3', 'certifi'],
    keywords=[
        'python',
        'harryludemann',
        'metlink',
        'wellington',
        'metlink-python'
        ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
