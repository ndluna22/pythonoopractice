from wordfinder import WordFinder
import random


class SpecialWordFinder(WordFinder):
    """For blank lines and special comments

     >>> newwords_file = SpecialWordFinder("newwords.txt")
        3 words read
    """

    def __init__(self, txt):

        newwords_file = open(txt, "r")  # opens txt file.

        self.words = self.parse(newwords_file)  # txt file to string

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]

    def random(self):
        """Return random word."""

        return random.choice(self.words)  # picks random word
