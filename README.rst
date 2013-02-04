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

Corpus downloading
------------------

Download and unpack the archive with XML files from
http://www.ruscorpora.ru/corpora-usage.html

Corpus reading
--------------

``ruscorpora.parse_xml`` function parses single XML file and returns
an iterator over sentences; each sentence is a list of ``ruscorpora.Token``
instances, annotated with a list of ``ruscorpora.Annotation`` instances.

``ruscorpora.simplify`` simplifies a result of ``ruscorpora.parse_xml`` by
removing ambiguous annotations, joining split tokens and removing accent
information.

::

    >>> import ruscorpora as rnc
    >>> for sent in rnc.simplify(rnc.parse('fiction.xml')):
    ...     print(sent)

Working with tags
-----------------

``ruscorpora.Tag`` class is a convenient wrapper for tags used in
ruscorpora::

    >>> tag = rnc.Tag('S,f,inan=sg,nom')
    >>> tag.POS
    'S'
    >>> tag.gender
    'f'
    >>> tag.animacy
    'inan'
    >>> tag.number
    'sg'
    >>> tag.case
    'nom'
    >>> tag.tense
    None

(there are also other attributes).

Check if a grammeme is in tag::

    >>> 'S' in tag
    True
    >>> 'V' in tag
    False
    >>> 'Foo' in tag
    Traceback (most recent call last)
    ...
    ValueError: Grammeme is unknown: Foo

Test tags equality::

    >>> tag == rnc.Tag('S,f,inan=sg,nom')
    True
    >>> tag == 'S,f,inan=sg,nom'
    True
    >>> tag == rnc.Tag('S,f,inan=sg,acc')
    False
    >>> tag == 'S,f,inan=sg,acc'
    False
    >>> tag == 'Foo,inan'
    Traceback (most recent call last)
    ...
    ValueError: Unknown grammemes: frozenset({Foo})

Tags returned by ``rnc.simplify`` are wrapped with this class by default.

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