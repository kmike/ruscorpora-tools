# -*- coding: utf-8 -*-
"""
Python wrapper for tags used in http://www.ruscorpora.ru/
"""
from __future__ import absolute_import, unicode_literals

# Часть речи:
POS_TAGS = frozenset([
    'S',            # существительное (яблоня, лошадь, корпус, вечность)
    'A',            # прилагательное (коричневый, таинственный, морской)
    'NUM',          # числительное (четыре, десять, много)
    'A-NUM',        # числительное-прилагательное (один, седьмой, восьмидесятый)
    'V',            # глагол (пользоваться, обрабатывать)
    'ADV',          # наречие (сгоряча, очень)
    'PRAEDIC',      # предикатив (жаль, хорошо, пора)
    'PARENTH',      # вводное слово (кстати, по-моему)
    'S-PRO',        # местоимение-существительное (она, что)
    'A-PRO',        # местоимение-прилагательное (который, твой)
    'ADV-PRO',      # местоименное наречие (где, вот)
    'PRAEDIC-PRO',  # местоимение-предикатив (некого, нечего)
    'PR',           # предлог (под, напротив)
    'CONJ',         # союз (и, чтобы)
    'PART',         # частица (бы, же, пусть)
    'INTJ',         # междометие (увы, батюшки)

    'ANUM',         # XXX: так на самом деле называется 'A-NUM'
    'NONLEX',
])

# Род:
GENDERS = frozenset([
    'm',    # мужской род (работник, стол)
    'f',    # женский род (работница, табуретка)
    'm-f',  # «общий род» (задира, пьяница)
    'n',    # средний род (животное, озеро)
])

# Одушевленность:
ANIMACY = frozenset([
    'anim', # одушевленность (человек, ангел, утопленник)
    'inan', # неодушевленность (рука, облако, культура)
])

# Число:
NUMBERS = frozenset([
    'sg', # единственное число (яблоко, гордость)
    'pl', # множественное число (яблоки, ножницы, детишки)
])

# Падеж:
CASES = frozenset([
    'nom',  # именительный падеж (голова, сын, степь, сани, который)
    'gen',  # родительный падеж (головы, сына, степи, саней, которого)
    'dat',  # дательный падеж (голове, сыну, степи, саням, которому)
    'acc',  # винительный падеж (голову, сына, степь, сани, который/которого)
    'ins',  # творительный падеж (головой, сыном, степью, санями, которым)
    'loc',  # предложный падеж ([о] голове, сыне, степи, санях, котором)
    'gen2', # второй родительный падеж (чашка чаю)
    'acc2', # второй винительный падеж (постричься в монахи; по два человека)
    'loc2', # второй предложный падеж (в лесу, на оси)
    'voc',  # звательная форма (Господи, Серёж, ребят)
    'adnum', # счётная форма (два часа, три шара)
])

# Краткая/полная форма:
SHORT_FULL = frozenset([
    'brev', # краткая форма (высок, нежна, прочны, рад)
    'plen', # полная форма (высокий, нежная, прочные, морской)
])

# Степень сравнения:
DEGREES_OF_COMPARISON = frozenset([
    'comp',     # сравнительная степень (глубже)
    'comp2',    # форма «по+сравнительная степень» (поглубже)
    'supr',     # превосходная степень (глубочайший)
])

# Вид:
ASPECTS = frozenset([
    'pf',  # совершенный вид (пошёл, встречу)
    'ipf', # несовершенный вид (ходил, встречаю)
])

# Переходность:
TRANSITIVITY = frozenset([
    'intr', # непереходность (ходить, вариться)
    'tran', # переходность (вести, варить)
])

# Залог:
VOICES = frozenset([
    'act',  # действительный залог (разрушил, разрушивший)
    'pass', # страдательный залог (только у причастий: разрушаемый, разрушенный)
    'med',  # медиальный, или средний залог (глагольные формы на -ся: разрушился и т.п.)
])

# Форма (репрезентация) глагола:
VERB_FORMS = frozenset([
    'inf',      # инфинитив (украшать)
    'partcp',   # причастие (украшенный)
    'ger',      # деепричастие (украшая)
])

# Наклонение:
GRAMMATICAL_MOODS = frozenset([
    'indic',    # изъявительное наклонение (украшаю, украшал, украшу)
    'imper',    # повелительное наклонение (украшай)
    'imper2',   # форма повелительного наклонения 1 л. мн. ч. на -те (идемте)
])

# Время:
TENSES = frozenset([
    'praet', # прошедшее время (украшали, украшавший, украсив)
    'praes', # настоящее время (украшаем, украшающий, украшая)
    'fut',   # будущее время (украсим)
])

# Лицо:
PERSONS = frozenset([
    '1p', # первое лицо (украшаю)
    '2p', # второе лицо (украшаешь)
    '3p', # третье лицо (украшает)
])

# Прочие признаки:
OTHER_GRAMMEMES = frozenset([
    'persn',    # личное имя (Иван, Дарья, Леопольд, Эстер, Гомер, Маугли)
    'patrn',    # отчество (Иванович, Павловна) famn — фамилия (Николаев, Волконская, Гумбольдт)
    'zoon',     # кличка животного (Шарик, Дочка)
    '0',        # несклоняемое (шоссе, Седых)

    # в справке почему-то нет

    'obsc', # ругательство
    'famn', # фамилия

])

# В корпусе со снятой грамматической омонимией предусмотрен ряд помет,
# указывающих на нестандартность и/или особенности записи входящей
# в Корпус словоформы:
NON_STANDARD_GRAMMEMES = frozenset([
    # отсутствие особенностей
    'normal',

    # («Аномальная форма») — различного рода морфологические аномалии, возможные
    # у устаревших или просторечных нелитературных форм (три дни при нормативном три
    # дня, ляжь при нормативном ляг)
    'anom',

    # («Искаженная форма»)  — орфографическое и/или фонетическое искажение слова, часто
    # передающее различные особенности произношения (дэвушка, това’ищи, про-хо-ди, низнаю).
    'distort',

    # («Цифровая запись»)  — запись числительного, числительного-прилагательного или
    # прилагательного (полностью или частично) при помощи цифр (73, LXXIII, 73-й, 22-летний). Для
    # этих словоформ в поле «Лексема» также употребляется цифровая запись; число и падеж
    # указываются только в тех случаях, когда выписано окончание (типа 14-му).
    'ciph',

    # («Инициал»)  — запись вида «заглавная буква с точкой» (М., Р.). В поле «Лексема» инициал
    # не раскрывается; грамматические признаки не указываются.
    'INIT',

    # («Сокращение»)  — сокращенная запись (тов., гг., ч.). В поле «Лексема» сокращение (кроме
    # инициалов) раскрывается, указывается грамматическая форма, соответствующая контексту.
    # Специально отметим, что акронимы вроде ООН, вуз и усеченные слова вроде зав, зам,
    # записываемые без точки и не раскрываемые при чтении, не получают пометы abbr и трактуются
    # как обычные слова (склоняемые или несклоняемые).
    'abbr',

])

# Граммемы, которые отсутствуют в корпусе, но могут быть приписаны
# этим пакетом:
CUSTOM_GRAMMEMES = frozenset([
    'PNCT', # граммема для пунктуации
])

ALLOWED_GRAMMEMES = (POS_TAGS | GENDERS | ANIMACY | NUMBERS | CASES |
                     SHORT_FULL | DEGREES_OF_COMPARISON | ASPECTS |
                     TRANSITIVITY | VOICES | VERB_FORMS | GRAMMATICAL_MOODS |
                     TENSES | PERSONS | OTHER_GRAMMEMES |
                     NON_STANDARD_GRAMMEMES | CUSTOM_GRAMMEMES)


class Tag(object):
    def __init__(self, tag):
        self._tag = tag

        # Example: V,ipf,intr,act=n,sg,praet,indic
        self._grammemes = self._split_to_grammemes(tag)
        self._grammeme_set = frozenset(self._grammemes)

        self._assert_grammemes_are_valid(self._grammeme_set)

    @property
    def POS(self):
        return self._grammemes[0]

    @property
    def gender(self):
        return self._grammatical_feature(GENDERS)

    @property
    def animacy(self):
        return self._grammatical_feature(ANIMACY)

    @property
    def number(self):
        return self._grammatical_feature(NUMBERS)

    @property
    def case(self):
        return self._grammatical_feature(CASES)

    @property
    def short_full(self):
        return self._grammatical_feature(SHORT_FULL)

    @property
    def degree_of_comparison(self):
        return self._grammatical_feature(DEGREES_OF_COMPARISON)

    @property
    def aspect(self):
        return self._grammatical_feature(ASPECTS)

    @property
    def transitivity(self):
        return self._grammatical_feature(TRANSITIVITY)

    @property
    def voice(self):
        return self._grammatical_feature(VOICES)

    @property
    def verb_form(self):
        return self._grammatical_feature(VERB_FORMS)

    @property
    def mood(self):
        return self._grammatical_feature(GRAMMATICAL_MOODS)

    @property
    def tense(self):
        return self._grammatical_feature(TENSES)

    @property
    def person(self):
        return self._grammatical_feature(PERSONS)

    def __contains__(self, grammeme):
        if grammeme in self._grammeme_set:
            return True
        else:
            if grammeme in ALLOWED_GRAMMEMES:
                return False
            else:
                raise ValueError("Grammeme is unknown: %s" % grammeme)

    def __eq__(self, other):
        if isinstance(other, Tag):
            return other._grammeme_set == self._grammeme_set

        grammemes = frozenset(self._split_to_grammemes(other))
        self._assert_grammemes_are_valid(grammemes)

        return grammemes == self._grammeme_set

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self): # XXX: this is incorrect in Python 2.x
        return "Tag(%r)" % self._tag

    def __str__(self): # XXX: this is incorrect in Python 2.x
        return self._tag

    def _assert_grammemes_are_valid(self, grammemes):
        unknown_grammemes = grammemes - ALLOWED_GRAMMEMES
        if unknown_grammemes:
            msg = "Unknown grammemes: %s" % str(unknown_grammemes)
            raise ValueError(msg)

    def _grammatical_feature(self, feature_set):
        grammemes = feature_set & self._grammeme_set
        if not grammemes:
            return None
        return next(iter(grammemes))

    @classmethod
    def _split_to_grammemes(cls, tag_txt):
        return tag_txt.replace('=', ',').split(',')

