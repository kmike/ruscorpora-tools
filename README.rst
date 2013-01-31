================
ruscorpora-tools
================

This package provides Python interface to a free corpus subset
available at http://ruscorpora.ru.

Installation
============

::

    pip install ruscorpora-tools

Usage
=====

Obtaining corpora
-----------------

Download and unpack the archive with XML files from
http://www.ruscorpora.ru/corpora-usage.html

Using corpora
-------------

``ruscorpora.parse_xml`` function parses single XML file and returns
an iterator over sentences; each sentence is a list of ``ruscorpora.Token``
instances, annotated with a list of ``ruscorpora.Annotation`` instances.

``ruscorpora.simplify`` simplifies a result of ``ruscorpora.parse_xml`` by
removing ambiguous annotations, joining split tokens and removing accent
information.

::

    >>> import ruscorpora as rc
    >>> for sent in rc.simplify(rc.parse('fiction.xml')):
    ...     print(sent)

Development
===========

Development happens at github and bitbucket:

* https://github.com/kmike/ruscorpora-tools
* https://bitbucket.org/kmike/ruscorpora-tools

The issue tracker is at github: https://github.com/kmike/ruscorpora-tools/issues

Feel free to submit ideas, bugs, pull requests (git or hg) or regular patches.

Running tests
-------------

Make sure `tox <http://tox.testrun.org>`_ is installed and run

::

    $ tox

from the source checkout. Tests should pass under python 2.6..3.3
and pypy > 1.8.