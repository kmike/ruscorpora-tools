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
            ('«', '«', 'PNCT', None),
            ('Школа', 'школа', 'S,f,inan=sg,nom', None),
            ('злословия', 'злословие', 'S,n,inan=sg,gen', None),
            (' » ,-', ' » ,-', 'PNCT', None),
            ('СМИ', 'сми', 'S,0=sg,nom', None),
            (' !', ' !', 'PNCT', None)
        ]
    ]


def test_joined_hyphen():
    corpus = """
    <se>
    <w><ana lex="Сегодня" gr="ADV" joined="hyphen"></ana>Сег`одня</w>-<w><ana lex="завтра" gr="ADV" joined="hyphen"></ana>з`автра</w>
    <w><ana lex="школа" gr="S,f,inan=sg,nom"></ana>шк`ола</w></se>
    """
    parsed = _parse(corpus)
    assert len(parsed) == 1
    assert parsed[0] == [
        ('Сегодня-завтра', 'Сегодня-завтра', 'ADV', 'hyphen'),
        ('школа', 'школа', 'S,f,inan=sg,nom', None),
    ]


def test_joined_hyphen_complex():
    corpus = """
    <se>
    <w><ana lex="певец" gr="S,m,anim=pl,ins" joined="hyphen"></ana>певц`ами</w>-<w><ana lex="солист" gr="S,m,anim=pl,ins" joined="hyphen"></ana>сол`истами</w> ,
    <w><ana lex="интернет" gr="S,m,inan=sg,nom" joined="hyphen"></ana>интерн`ет</w>-<w><ana lex="торговля" gr="S,f,inan=sg,gen" joined="hyphen"></ana>торг`овли</w>
    <w><ana lex="они" gr="S-PRO,pl,3p=gen" joined="hyphen"></ana>их</w>-<w><ana lex="то" gr="PART" joined="hyphen"></ana>то</w></se>
    """
    parsed = _parse(corpus)
    assert len(parsed) == 1
    assert parsed[0] == [
        ('певцами-солистами', 'певец-солист', 'S,m,anim=pl,ins', 'hyphen'),
        (' ,', ' ,', 'PNCT', None),
        ('интернет-торговли', 'интернет-торговля', 'S,f,inan=sg,gen', 'hyphen'),
        ('их-то', 'они-то', 'S-PRO,pl,3p=gen', 'hyphen'),
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
            ('Злословия', 'злословие', 'S,n,inan=sg,gen', None),
            (' -', ' -', 'PNCT', None),
            ('полдюжины', 'полдюжина', 'S,f,inan=sg,gen', 'together')
        ]
    ]
