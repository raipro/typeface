import jellyfish
from fuzzywuzzy import fuzz


s = input("Enter string ")
file = input("Enter file ")

f = open(file)
for it in f:
    # print(it)
    it = it.strip()
    if fuzz.ratio(jellyfish.soundex(s),jellyfish.soundex(it)) == 100:
        print(it)


