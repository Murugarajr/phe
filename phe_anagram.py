from collections import defaultdict

word_set = defaultdict(set)


def process(reference):
    for word in open(reference):
        word = word.lower().strip()
        if word:
            word_set[frozenset(word)].add(word)


def find_anagrams(word):
    anagram_output = word_set[frozenset(word)]
    for anagrams in anagram_output:
        if sorted(anagrams) == sorted(word):
            print(anagrams)


if __name__ == '__main__':
    # words list from https://www.wordgamedictionary.com/english-word-list/download/english.txt is used as a data
    data = "english.txt"
    process(reference=data)
    input_parm = input("Enter input word to find anagrams:")
    find_anagrams(word=input_parm)

