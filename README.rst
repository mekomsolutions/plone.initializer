.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://travis-ci.org/mekomsolutions/plone.initializer.svg?branch=master
    :target: https://travis-ci.org/mekomsolutions/plone.initializer

.. image:: https://coveralls.io/repos/github/mekomsolutions/plone.initializer/badge.svg?branch=master
    :target: https://coveralls.io/github/mekomsolutions/plone.initializer?branch=master
    :alt: Coveralls

.. image:: https://img.shields.io/pypi/v/plone.initializer.svg
    :target: https://pypi.python.org/pypi/plone.initializer/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/plone.initializer.svg
    :target: https://pypi.python.org/pypi/plone.initializer
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/plone.initializer.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/plone.initializer.svg
    :target: https://pypi.python.org/pypi/plone.initializer/
    :alt: License

=================

plone.initializer
=================

This  plugin will load data  exported from the ZMI into a new Plone site. The plugin expects  the data to exist at `${var-dir}/importdata/data.tar.gz` . It is created specifically for importing data from [SENAITE](https://www.senaite.com/) but should work with any data exported as tar.gz from the ZMI interface.

Installation
------------

Install plone.initializer by adding it to your buildout::

    [buildout]
    
    ...
    
    eggs =
        plone.initializer


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/mekomsolutions/plone.initializer/issues
- Source Code: https://github.com/mekomsolutions/plone.initializer


License
-------

The project is licensed under the MIT licence.
