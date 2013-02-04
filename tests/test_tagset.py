# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import pytest
import ruscorpora as rnc

def test_attributes():
    tag = rnc.Tag('S,f,inan=sg,nom')
    assert tag.POS == 'S'
    assert tag.gender == 'f'
    assert tag.animacy == 'inan'
    assert tag.number == 'sg'
    assert tag.case == 'nom'
    assert tag.tense is None
    assert tag.short_full is None
    assert tag.aspect is None
    assert tag.degree_of_comparison is None
    assert tag.mood is None
    assert tag.person is None
    assert tag.transitivity is None
    assert tag.verb_form is None
    assert tag.voice is None

def test_attributes2():
    tag = rnc.Tag('V,ipf,intr,act=n,sg,praet,indic')

    assert tag.POS == 'V'
    assert tag.aspect == 'ipf'
    assert tag.gender == 'n'
    assert tag.mood == 'indic'
    assert tag.tense == 'praet'
    assert tag.transitivity == 'intr'

def test_contains():
    tag = rnc.Tag('V,ipf,intr,act=n,sg,praet,indic')
    assert 'V' in tag
    assert 'ipf' in tag
    assert 'indic' in tag

    assert 'S' not in tag
    assert 'pl' not in tag

    with pytest.raises(ValueError):
        'Foo' in tag

def test_eq():
    assert rnc.Tag('V') == 'V'
    assert rnc.Tag('S,f,inan=sg,nom') == 'S,f,inan,sg,nom'
    assert rnc.Tag('S,f') == rnc.Tag('S,f')

    assert rnc.Tag('S,f') != rnc.Tag('V')
    assert rnc.Tag('V') != 'S,f'

    with pytest.raises(ValueError):
        rnc.Tag('S,f') == 'Foo'
