"""
Tonality implementation.
"""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from keywords import Keywords


class Tonality:
    """
    Class for determining the tonality.
    """

    def __init__(self, text: str, path: str) -> None:
        """
        Initialize class instance.
        """
        self._text = text
        self._keywords = Keywords(self._text)
        self._count_vect = CountVectorizer()
        self._path = path

    def model_training(self) -> MultinomialNB():
        """
        Preprocess texts and train the model.
        """
        df = pd.read_csv(self._path)
        df['text'] = df['text'].str.lower()
        df['text'] = df['text'].str.replace('[^\w\s]', '')
        df['text'] = df['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in
                                                          (self._keywords.load_stop_words())]))
        x = df['text'].values
        y = df['tone'].values
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
        x_train_dtm = self._count_vect.fit_transform(x_train)
        clf = MultinomialNB().fit(x_train_dtm, y_train)
        return clf

    def get_message(self, clf) -> str:
        """
        Write a message about the tonality of the text.
        """
        x_text = self._count_vect.transform([self._text])
        sentiment = clf.predict(x_text)
        if sentiment[0] == 0:
            return f"Тональность: текст нейтральный"
        elif sentiment[0] == 1:
            return f"Тональность: текст положительный"
        else:
            return f"Тональность: текст негативный"
