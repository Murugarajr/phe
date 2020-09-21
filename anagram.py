from collections import defaultdict

word_set = defaultdict(set)

# worlds list from https://www.wordgamedictionary.com/english-word-list/download/english.txt
for word in open("english.txt"):
    word = word.lower().strip()
    if word:
        word_set[frozenset(word)].add(word)


def find(word):
    return word_set[frozenset(word)]


input_word = "rescued"
anagram_output = find(input_word)
print(anagram_output)

is_anagram = lambda x1, x2: sorted(x1) == sorted(x2)
# print([is_anagram(input_word, x2) for x2 in anagram_output])
for x2 in anagram_output:
    if is_anagram(input_word, x2):
        print(x2)
