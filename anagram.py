import nltk
from collections import defaultdict

wordlist = nltk.corpus.words.words('en')
anagrams = defaultdict(list)

anagrams = nltk.Index((''.join(sorted(w)), w) for w in wordlist)
print("Anagrams: {}".format(anagrams["aent"]))

# testing anagrams
# is_anagram = lambda x1, x2: sorted(x1) == sorted(x2)
