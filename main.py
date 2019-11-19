# Case-study #4
# Developers:   Drachev Nikita (0),
#               Starnovskiy Sergey (65),
#               Zhuravlev Alexander (30)

import local as lc
from textblob import TextBlob

lang = input(lc.INPUT)
while lang != '2' and lang != '1':
    print(lc.ERROR)
    lang = input(lc.INPUT)
if lang == '1':
    import local_en as lc
else:
    import local_ru as lc

txt = input(lc.INPUT)

# Finding language of the text.
count_ru = 0
count_en = 0
for i in range(0, len(txt)):
    if 97 <= ord(txt[i]) <= 122 or 65 <= ord(txt[i]) <= 90:
        count_en += 1
    elif 1072 <= ord(txt[i]) <= 1103 or 1040 <= ord(txt[i]) <= 1071:
        count_ru += 1

if count_ru > count_en:
    lang_ru = True
    lang_en = False
else:
    lang_en = True
    lang_ru = False


def syllables_count_ru():
    # Function counts quantity of syllables in the text for russian language.
    vowels = 'еыаоэяуиюУЕЫАОЭЯИЮ'
    syllables = 0
    for _ in txt:
        if vowels.find(_) != -1:
            syllables += 1
    return syllables


def words_count_universal():
    # Function counts number of words for any language.
    words = txt.split(' ')
    words_count = len(words)
    return words_count


def sentence_count_universal():
    # Function counts number of sentences for any language.
    sentence_count = 0
    for _ in txt:
        if _ == '.' or _ == '!' or _ == '?':
            sentence_count += 1
    return sentence_count


def asl_count_ru():
    # Function counts average sentence length for russian language.
    vowels = 'еыаоэуяиюёУЕЫАОЭЯИЮЁ'
    syllables = 0
    sentence_count = 0
    for _ in txt:
        if vowels.find(_) != -1:
            syllables += 1
        words = txt.split(' ')
        words_count = len(words)
        if _ == '.' or _ == '!' or _ == '?':
            sentence_count += 1
    asl = words_count / sentence_count
    return asl


def asw_count_ru():
    # Function counts average syllables per word for russian language.
    vowels = 'еыаоэуяиюёУЕЫАОЭЯИЮЁ'
    syllables = 0
    sentence_count = 0
    for _ in txt:
        if vowels.find(_) != -1:
            syllables += 1
        words = txt.split(' ')
        words_count = len(words)
        if _ == '.' or _ == '!' or _ == '?':
            sentence_count += 1
    asw = syllables / words_count
    return asw


def flash_index_ru():
    # Function counts flash index for russian language.
    vowels = 'еыаоэуяиюёУЕЫАОЭЯИЮЁ'
    syllables = 0
    sentence_count = 0
    for _ in txt:
        if vowels.find(_) != -1:
            syllables += 1
        words = txt.split(' ')
        words_count = len(words)
        if _ == '.' or _ == '!' or _ == '?':
            sentence_count += 1
    asl = words_count / sentence_count
    asw = syllables / words_count
    fre = 206.835 - (1.3 * asl) - (60.1 * asw)
    return fre


def syllables_count_en():
    # Function counts syllables in the text for english language.
    vowels = 'euioaEUIOA'
    syllables = 0
    for _ in txt:
        if vowels.find(_) != -1:
            syllables += 1
    return syllables


def asl_count_en():
    # Function counts average sentence length for english language.
    vowels = 'euioaEUIOA'
    syllables = 0
    sentence_count = 0
    for _ in txt:
        if vowels.find(_) != -1:
            syllables += 1
        words = txt.split(' ')
        words_count = len(words)
        if _ == '.' or _ == '!' or _ == '?':
            sentence_count += 1
    asl = words_count / sentence_count
    return asl


def asw_count_en():
    # Function counts average syllables per word for english language.
    vowels = 'euioaEUIOA'
    syllables = 0
    sentence_count = 0
    for _ in txt:
        if vowels.find(_) != -1:
            syllables += 1
        words = txt.split(' ')
        words_count = len(words)
        if _ == '.' or _ == '!' or _ == '?':
            sentence_count += 1
    asw = syllables / words_count
    return asw


def flash_index_en():
    # Function counts flash index for english language.
    vowels = 'euioaEUIOA'
    syllables = 0
    sentence_count = 0
    for _ in txt:
        if vowels.find(_) != -1:
            syllables += 1
        words = txt.split(' ')
        words_count = len(words)
        if _ == '.' or _ == '!' or _ == '?':
            sentence_count += 1
    asl = words_count / sentence_count
    asw = syllables / words_count
    fre = 206.835 - (1.015 * asl) - (84.6 * asw)
    return fre


# Using TextBlob to analyze english text.
if lang_en:
    analysis = TextBlob(txt)

if lang_ru:
    print(lc.SENT, sentence_count_universal())
    print(lc.WORDS, words_count_universal())
    print(lc.CYLS, syllables_count_ru())
    print(lc.ASL, asl_count_ru())
    print(lc.ASW, asw_count_ru())
    print(lc.FLASH, flash_index_ru())
    if flash_index_ru() > 80:
        print(lc.EZ)
    elif flash_index_ru() > 50:
        print(lc.SIMPLE)
    elif flash_index_ru() > 25:
        print(lc.HARDER)
    else:
        print(lc.HARD)
else:
    print(lc.SENT, sentence_count_universal())
    print(lc.WORDS, words_count_universal())
    print(lc.CYLS, syllables_count_en())
    print(lc.ASL, asl_count_en())
    print(lc.ASW, asw_count_en())
    print(lc.FLASH, flash_index_en())
    if flash_index_en() > 80:
        print(lc.EZ)
    elif flash_index_en() > 50:
        print(lc.SIMPLE)
    elif flash_index_en() > 25:
        print(lc.HARDER)
    else:
        print(lc.HARD)
    print(lc.OBJKV, (1 - round(analysis.sentiment.subjectivity, 2)) * 100, '%', sep='')
    if analysis.sentiment.polarity > 0.5:
        print(lc.KEY, lc.POSITIVE)
    elif -0.5 <= analysis.sentiment.polarity <= 0.5:
        print(lc.KEY, lc.NEUTRAL)
    else:
        print(lc.KEY, lc.NEGATIVE)
