[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://gitHub.com/ya332/deepextract/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PyPI version fury.io](https://badge.fury.io/py/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![Latest PyPI versions](https://img.shields.io/pypi/v/deepextract.svg)](https://pypi.python.org/pypi/deepextract)
[![Latest Travis CI build status](https://travis-ci.com/ya332/deepextract.svg?branch=master)](https://travis-ci.com/github/ya332/deepextract)

# deepextract

A Python library to parse JSON, YAML files and extract deeply nested keys.

## Usage

## Installation

```sh
pip install deepextract
```

## Requirements

<= Python 3.6

## Deployment

Based on descriptions from [here](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/), whenever project owner pushes a tagged commit to your Git repository remote on GitHub, this workflow will publish it to PyPI.

And it'll publish any push to TestPyPI which is useful for providing test builds to repo's alpha users as well as making sure that your release pipeline remains healthy.

Manual deploy to TestPyPI:
`python setup.py sdist bdist_wheel`
`twine upload -r testpypi dist/*`


## Licence

MIT. See LICENSE.md

# Authors

`deepextract` was written by `Yigit Alparslan <alparslanyigitcan@gmail.com>`.
