# Case-study #4
# Developers:   Drachev Nikita (),
#               Starnovskiy Sergey (),
#               Zhuravlev Alexander ()

import local as lc
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

# TODO(Aleksandr Zhuravlev): make functions to count: letters, cyllables, words and sentences.


def syllables_count_ru():
#   Function counting quantity of syllables in the whole text for russian language
    vowels = 'еыаоэяуиюУЕЫАОЭЯИЮ'
    syllables = 0
    for _ in txt:
        if vowels.find(_)!=-1:
            syllables += 1
    return syllables


def words_count_universal():
    words = txt.split(' ')
    words_count = len(words)
    return words_count


def sentence_count_universal():
    sentence_count = 0
    for _ in txt:
        if _ == '.' or _ == '!' or _ == '?':
            sentence_count += 1
    return (sentence_count)


def asl_count_ru():
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
    asl = words_count/sentence_count
    asw = syllables / words_count
    fre = 206.835 - (1.3 * asl) - (60.1 * asw)
    return fre


def syllables_count_en():
#   Function counting quantity of syllables in the whole text for russian language
    vowels = 'euioaEUIOA'
    syllables = 0
    for _ in txt:
        if vowels.find(_)!=-1:
            syllables += 1
    return syllables


def asl_count_en():
#function counting
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
# function counting average sentence length for english language
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
#function counting flash index for english language
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
    asl = words_count/sentence_count
    asw = syllables / words_count
    fre = 206.835 - (1.015 * asl) - (84.6 * asw)
    return fre

if lang_ru == True:
    print('Предложений:', sentence_count_universal())
    print('Слов:', words_count_universal())
    print('Слогов:', syllables_count_ru())
    print('Средняя длина предложения в словах:', asl_count_ru())
    print('Средняя длина слова в слогах:', asw_count_ru())
    print('Индекс удобочитаемости Флеша:', flash_index_ru())
else:
    print('Предложений:', sentence_count_universal())
    print('Слов:', words_count_universal())
    print('Слогов:', syllables_count_en())
    print('Средняя длина предложения в словах:', asl_count_en())
    print('Средняя длина слова в слогах:', asw_count_en())
    print('Индекс удобочитаемости Флеша:', flash_index_en())

# TODO: deal with textblob and dostoevsky modules.

# TODO: (one of the last ones): count Flash index.
