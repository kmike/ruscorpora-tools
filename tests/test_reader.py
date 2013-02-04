# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import io
import ruscorpora as rnc

def _parse(corpus_xml):
    corpus = '<?xml version="1.0" encoding="utf-8" ?>\n<corpus>\n%s\n</corpus>' % corpus_xml
    fp = io.BytesIO(corpus.encode('utf8'))
    return list(rnc.simplify(rnc.parse_xml(fp)))


def test_simple():
    corpus = """
    <se>«
    <w><ana lex="школа" gr="S,f,inan=sg,nom"></ana>Шк`ола</w>
     <w><ana lex="злословие" gr="S,n,inan=sg,gen"></ana>злосл`овия</w> » ,-
    <w><ana lex="сми" gr="S,0=sg,nom"></ana>СМИ</w> !</se>"""

    assert _parse(corpus) == [
        [
            ('«', [rnc.Annotation(lex='«', gr='PNCT', joined=None)]),
            ('Школа', [rnc.Annotation(lex='школа', gr='S,f,inan=sg,nom', joined=None)]),
            ('злословия', [rnc.Annotation(lex='злословие', gr='S,n,inan=sg,gen', joined=None)]),
            (' » ,-', [rnc.Annotation(lex=' » ,-', gr='PNCT', joined=None)]),
            ('СМИ', [rnc.Annotation(lex='сми', gr='S,0=sg,nom', joined=None)]),
            (' !', [rnc.Annotation(lex=' !', gr='PNCT', joined=None)])
        ]
    ]


def test_joined_hyphen():
    corpus = """
    <se>
    <w><ana lex="Сегодня" gr="ADV" joined="hyphen"></ana>Сег`одня</w>-<w><ana lex="завтра" gr="ADV" joined="hyphen"></ana>з`автра</w>
    <w><ana lex="школа" gr="S,f,inan=sg,nom"></ana>шк`ола</w></se>
    """
    assert _parse(corpus) == [
        [
            ('Сегодня-завтра', [
                rnc.Annotation(lex='Сегодня', gr='ADV', joined='hyphen'),
                rnc.Annotation(lex='завтра', gr='ADV', joined='hyphen')]),
            ('школа', [rnc.Annotation(lex='школа', gr='S,f,inan=sg,nom', joined=None)])
        ]
    ]


def test_joined_together():
    corpus = """
    <se>
    <w><ana lex="злословие" gr="S,n,inan=sg,gen"></ana>Злосл`овия</w> -
    <w><ana lex="пол" gr="NUM" joined="together"></ana>пол</w><w><ana lex="дюжина" gr="S,f,inan=sg,gen" joined="together"></ana>дюжины</w>
    </se>
    """
    assert _parse(corpus) == [
        [
            ('Злословия', [rnc.Annotation(lex='злословие', gr='S,n,inan=sg,gen', joined=None)]),
            (' -', [rnc.Annotation(lex=' -', gr='PNCT', joined=None)]),
            ('полдюжины', [
                rnc.Annotation(lex='пол', gr='NUM', joined='together'),
                rnc.Annotation(lex='дюжина', gr='S,f,inan=sg,gen', joined='together')])
        ]
    ]
