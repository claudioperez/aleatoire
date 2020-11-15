---
title: Aleatoire
url: https://github.com/claudioperez/aleatoire
description: A set of object-oriented tools for the probabilistic analysis of systems.
...

<h1>Aleatoire</h1>

A set of tools for the probabilistic analysis of systems.

--------------------

[![PyPI Version][pypi-v-image]][pypi-v-link]
[![Commits since latest release][gh-image]][gh-link]

**Table of contents**

- [Installation](#installation)

A rough compilation of general-purpose system reliability functions and classes written over the course of a semester. This package implements probability transformations composed of marginal distributions which are defined using objects from the popular scipy.stats statistical library. This package is largely built upon the framework for reliability computations layed out in CalRel and FERUM.

## Installation

```shell
pip install aleatoire
```

You can also install the in-development version with:

```shell
pip install https://github.com/claudioperez/aleatoire/archive/master.zip
```


[pypi-v-image]: https://img.shields.io/pypi/v/aleatoire.svg
[pypi-v-link]: https://pypi.org/project/aleatoire/

[travis-image]: https://api.travis-ci.org/claudioperez/aleatoire.svg?branch=master
[travis-link]: https://travis-ci.org/claudioperez/aleatoire

[gh-link]: https://github.com/claudioperez/aleatoire/compare/v0.0.2...master
[gh-image]: https://img.shields.io/github/commits-since/claudioperez/aleatoire/v0.0.2?style=social
