import io
import os
import re
import codecs
import os.path
from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name="deepextract",
    version=get_version("deepextract/__init__.py"),
    url="https://github.com/ya332/deepextract",
    license='MIT',

    author="Yigit Alparslan",
    author_email="alparslanyigitcan@gmail.com",

    description="A Python library to parse JSON, YAML files and extract deeply nested keys.",
    long_description=read("README.md"),
    long_description_content_type='text/markdown',

    packages=find_packages(exclude=('tests','data')),

    install_requires=[],
    python_requires=">=3.6.0",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
