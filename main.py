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
else:
    lang_en = True


# TODO: make functions to count: letters, cyllables, words and sentences.

# TODO: deal with textblob and dostoevsky modules.

# TODO: (one of the last ones): count Flash index.
