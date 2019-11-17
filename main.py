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
    glasnye = 'еыаоэяиюёУЕЫАОЭЯИЮЁ'
    syllables= 0
    for _ in range(len(txt)):
        if glasnye.find(txt[_])!=-1:
            syllables += 1
    return (syllables)

print(syllables_count_ru())

def words_count_ru():
    words = txt.split(' ')
    words_count= len(words)
    return (words_count)

def sentence_count_universal():
    sentence_count = 0
    for _ in range(len(txt)):
        if txt[_] == '.' or txt[_] == '!' or txt[_] == '?':
            sentence_count +=1
    return (sentence_count_universal)

def flash_index_ru():
    glasnye = 'еыаоэяиюёУЕЫАОЭЯИЮЁ'
    syllables = 0
    sentence_count = 0
    for _ in range(len(txt)):
        if glasnye.find(txt[_]) != -1:
            syllables += 1
        words = txt.split(' ')
        words_count = len(words)
        if txt[_] == '.' or txt[_] == '!' or txt[_] == '?':
            sentence_count +=1
        asl=words_count/sentence_count
        asw=words_count/syllables
        fre=206.835 - (1.3 * asl) - (60.1 * asw)
        return (fre)


# TODO: deal with textblob and dostoevsky modules.

# TODO: (one of the last ones): count Flash index.
