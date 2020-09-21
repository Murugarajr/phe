from collections import defaultdict

word_set = defaultdict(set)


def process(reference):
    """
    process function receives an input argument (input data) and do the pre-processing of the reference data
    :param reference:
    """
    for word in open(reference):
        word = word.lower().strip()
        if word:
            word_set[frozenset(word)].add(word)


def find_anagrams(word):
    """
    This function find the superset of possible anagram words and then filter it out based on the input word

    :param word:
    :return:anagrams of 'word' from the input data that were supplied
    """
    anagram_output = word_set[frozenset(word)]
    for anagrams in anagram_output:
        if sorted(anagrams) == sorted(word):
            print(anagrams)


if __name__ == '__main__':
    # words list(total=144884) from https://www.wordgamedictionary.com/english-word-list/download/english.txt is
    # used as a input data
    data = "english.txt"
    process(reference=data)
    input_parm = input("Enter the input word to find anagrams:")
    find_anagrams(word=input_parm)
