"""
Keywords implementation.
"""
import nltk
import string
from pymorphy3 import MorphAnalyzer


class Keywords:
    """
    Class to find keywords
    """

    def __init__(self, text: str) -> None:
        """
        Initialize class instance.
        """
        self._text = text

    def get_normal_form(self, word: str) -> str:
        """
        Determine the initial form of words.
        """
        morph = MorphAnalyzer()
        return morph.parse(word)[0].normal_form

    def load_stop_words(self) -> list:
        """
        Download stop words for Russian language.
        """
        nltk.download('stopwords')
        return nltk.corpus.stopwords.words('russian')

    def split_into_words(self) -> list:
        """
        Create a list of text words.
        """
        text = self._text.lower().translate(str.maketrans('', '', f'{string.punctuation}«»—')).split()
        return [word for word in text if word not in self.load_stop_words()]

    def create_dictionary(self, words: list) -> dict:
        """
        Create a word frequency dictionary.
        """
        word_frequency = {}
        for word in words:
            normal_form = self.get_normal_form(word)
            if normal_form not in word_frequency:
                word_frequency[normal_form] = 0
            word_frequency[normal_form] += 1
        return word_frequency

    def make_sorted_words(self, dictionary: dict) -> str:
        """
        Sort the dictionary and return the first five words.
        """
        sorted_words = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[:5]
        return ', '.join([item[0] + ' ' + str(item[1]) for item in sorted_words])

    def get_message(self) -> str:
        """
        Write a message about the keywords of the text.
        """
        return (f'Ключевые слова: '
                f'{self.make_sorted_words(self.create_dictionary(self.split_into_words()))}')
