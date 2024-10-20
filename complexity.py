"""
Text difficulty level implementation.
"""
import re


class Complexity:
    """
    Class for determining the difficulty of understanding the text
    """

    def __init__(self, text: str) -> None:
        """
        Initialize class instance.
        """
        self._text = text

    def processing_text(self) -> tuple:
        """
        Process user text.
        """
        text = self._text.replace('?', '.').replace('!', '.')
        list_sentences = text.split('. ')
        length_text = len(list_sentences)
        average_sentence_length = 0
        for sentence in list_sentences:
            list_words = sentence.split()
            average_sentence_length += len(list_words) / length_text
        list_words = [word.lower() for word in text.split() if re.search('[аеёиоуыэюя]', word.lower())]
        average_number_syllables_word = 0
        for word in list_words:
            average_number_syllables_word += len([letter for letter in word
                                                  if letter in 'аеёиоуыэюя']) / len(list_words)
        return average_sentence_length, average_number_syllables_word

    def calculate_fres(self, asl: int, asw: int) -> float:
        """
        Calculate Flesch reading ease score.
        """
        return 206.835 - 1.52 * asl - 65.14 * asw

    def determine_complexity(self, fres: float) -> str:
        """
        Assess the level of difficulty in understanding the text.
        """

    def get_message(self) -> str:
        """
        Write a message about the complexity of the text.
        """
        criteria = self.processing_text()
        average_sentence_length = criteria[0]
        average_number_syllables_word = criteria[1]
        fres = self.calculate_fres(average_sentence_length, average_number_syllables_word)
        return (f'Средняя длина предложения в словах: {round(average_sentence_length, 2)}\n'
                f'Средняя длина слова в слогах: {round(average_number_syllables_word, 2)}\n'
                f'Индекс сложности текста: '
                f'{round(fres, 2)}\n'
                f'{self.determine_complexity(fres)}')
