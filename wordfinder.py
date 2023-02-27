"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Word Finder: finds random words from a dictionary

    >>> words_file = WordFinder("words.txt")
        3 words read

    >>> words_file.random() 
        "random word"
    """

    def __init__(self, txt):

        words_file = open(txt, "r")  # opens txt file.

        self.words = self.parse(words_file)  # txt file to string

        num_words = len(self.words)

        print(f"{num_words} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        for word in dict_file:  # loop to return word in txt file
            return word

    def random(self):
        """Return random word."""

        return random.choice(self.words)  # picks random word
