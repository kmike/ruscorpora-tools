# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals, print_function
try:
    from xml.etree import cElementTree as ElementTree
except ImportError:
    from xml.etree import ElementTree

import warnings
import functools
from collections import namedtuple

Token = namedtuple('Token', 'text annotations')
Annotation = namedtuple('Annotation', 'lex gr joined')

def parse_xml(source):
    """
    Parse XML file ``source`` (which can be obtained from ruscorpora.ru);
    return an iterator of sentences. Each sentence is a list of Token
    instances.
    """
    xml = ElementTree.parse(source)

    def punct_tokens(txt):
        if not txt:
            return []

        tokens = [tok for tok in txt.split('\n')]
        return [Token(tok, None) for tok in tokens if tok]

    for se in xml.findall('se'):
        sent = []
        sent.extend(punct_tokens(se.text))

        for w in se.findall('w'):
            ana_elems = w.findall('ana')

            # text after the last annotation is a word
            word = ana_elems[-1].tail or ''

            annotations = [
                Annotation(a.get('lex'), a.get('gr'), a.get('joined'))
                for a in ana_elems
            ]
            sent.append(Token(word, annotations))
            sent.extend(punct_tokens(w.tail))

        sent.extend(punct_tokens(se.tail))
        yield [t for t in sent if t.text.strip()]


def simplify(sents, remove_accents=True, join_split=True,
             join_hyphenated=True, punct_tag='PNCT'):
    """
    Simplify the result of ``sents`` parsing:

    * keep only a single annotation per word part;
    * annotate punctuation with ``punct_tag``;
    * join split words into a single token (if ``join_split==True``);
    * join hyphenated words to a single token (if ``join_hyphenated==True``);
    * remove accents (if ``remove_accents==True``).
    """

    def remove_extra_annotations(token):
        """ force token annotations to be a single-element list """
        if token.annotations is None:
            return (token.text, [None])
        return (token.text, [token.annotations[-1]])

    def _combine_tokens(tokens):
        text = "".join(t[0] for t in tokens)
        annotations = [ann for t in tokens for ann in t[1] if ann]
        return (text, annotations)

    def _join_tokens(sent, accum_size, should_accumulate):
        accum = []
        for text, annotations in sent:
            ann = annotations[0]
            if should_accumulate(text, ann, accum):
                accum.append((text, annotations))

                if len(accum) == accum_size:
                    yield _combine_tokens(accum)
                    accum = []
            else:
                if accum:
                    warnings.warn("unconsumed tokens: %s" % accum)
                    for tok in accum:
                        yield tok
                    accum = []
                yield text, annotations

    join_split_tokens = functools.partial(
        _join_tokens,
        accum_size=2,
        should_accumulate = lambda text, ann, accum: ann and ann.joined == 'together'
    )

    join_hyphenated_tokens = functools.partial(
        _join_tokens,
        accum_size=3,
        should_accumulate = lambda text, ann, accum: (ann and ann.joined == 'hyphen') or (accum and text.strip() == '-')
    )

    def fix_punct_tags(sent):
        for text, annotations in sent:
            new_annotations = []
            for ann in annotations:
                if ann is None:
                    ann = Annotation(text, punct_tag, None)
                new_annotations.append(ann)

            yield text, new_annotations


    for sent in sents:
        sent = map(remove_extra_annotations, sent)

        if remove_accents:
            sent = [(t[0].replace('`', ''), t[1]) for t in sent]

        if join_split:
            sent = join_split_tokens(sent)

        if join_hyphenated:
            sent = join_hyphenated_tokens(sent)

        sent = fix_punct_tags(sent)

        yield [Token(*t) for t in sent]


if __name__ == '__main__':
    import sys
    for sent in simplify(parse_xml(sys.argv[1])):
        for tok in sent:
            print(tok)
        print("\n")