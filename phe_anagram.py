from collections import defaultdict

word_set = defaultdict(set)


def process(reference):
    """
    process function receives an input argument (input data) and do the pre-processing of the reference data
    :param reference:
    """
    for word in open(reference):
        try:
            word = word.lower().strip()
        except OSError as err:
            print("cannot open a file {}".format(err))
        if word:
            word_set[frozenset(word)].add(word)


def find_anagrams(word):
    """
    This function find the superset of possible anagram words and then filter it out based on the input word

    :param word:
    :return:anagrams of 'word' from the input data that were supplied
    """
    try:
        anagram_output = word_set[frozenset(word)]
        for anagrams in anagram_output:
            if sorted(anagrams) == sorted(word):
                print(anagrams)
    except Exception as err:
        print("Please check the input {}".format(err))


if __name__ == '__main__':
    # words list(total=267751) from https://www.wordgamedictionary.com/sowpods/ is used as a input data
    data = "english.txt"
    process(reference=data)
    input_parm = input("Enter the input word to find anagrams:")
    find_anagrams(word=input_parm)
