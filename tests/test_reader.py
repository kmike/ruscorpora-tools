# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import io
import ruscorpora as rc

def _parse(corpus_xml):
    corpus = '<?xml version="1.0" encoding="utf-8" ?>\n<corpus>\n%s\n</corpus>' % corpus_xml
    fp = io.BytesIO(corpus.encode('utf8'))
    return list(rc.simplify(rc.parse_xml(fp)))


def test_simple():
    corpus = """
    <se>«
    <w><ana lex="школа" gr="S,f,inan=sg,nom"></ana>Шк`ола</w>
     <w><ana lex="злословие" gr="S,n,inan=sg,gen"></ana>злосл`овия</w> » ,-
    <w><ana lex="сми" gr="S,0=sg,nom"></ana>СМИ</w> !</se>"""

    assert _parse(corpus) == [
        [
            ('«', [rc.Annotation(lex='«', gr='PNCT', joined=None)]),
            ('Школа', [rc.Annotation(lex='школа', gr='S,f,inan=sg,nom', joined=None)]),
            ('злословия', [rc.Annotation(lex='злословие', gr='S,n,inan=sg,gen', joined=None)]),
            (' » ,-', [rc.Annotation(lex=' » ,-', gr='PNCT', joined=None)]),
            ('СМИ', [rc.Annotation(lex='сми', gr='S,0=sg,nom', joined=None)]),
            (' !', [rc.Annotation(lex=' !', gr='PNCT', joined=None)])
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
                rc.Annotation(lex='Сегодня', gr='ADV', joined='hyphen'),
                rc.Annotation(lex='завтра', gr='ADV', joined='hyphen')]),
            ('школа', [rc.Annotation(lex='школа', gr='S,f,inan=sg,nom', joined=None)])
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
            ('Злословия', [rc.Annotation(lex='злословие', gr='S,n,inan=sg,gen', joined=None)]),
            (' -', [rc.Annotation(lex=' -', gr='PNCT', joined=None)]),
            ('полдюжины', [
                rc.Annotation(lex='пол', gr='NUM', joined='together'),
                rc.Annotation(lex='дюжина', gr='S,f,inan=sg,gen', joined='together')])
        ]
    ]
