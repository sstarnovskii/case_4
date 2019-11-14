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


# TODO: make function to distinguish russian and english. (Sergey)

# TODO: make functions to count: cyllables, words and sentences.

# TODO: deal with textblob and dostoevsky modules.

# TODO: (one of the last ones): count Flash index.
