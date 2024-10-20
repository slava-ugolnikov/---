"""
Telebot implementation.
"""
import telebot
from complexity import Complexity
from tonality import Tonality
from keywords import Keywords


bot = telebot.TeleBot('') #telebot api
path = '' #path to texts for training the model


@bot.message_handler(content_types=['text'])
def send_messages(message) -> None:
    """
    Write a response to the user.
    """
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет! Я бот, который анализирует текст.\n"
                                               "Отправьте мне текст, и я определю его сложность для понимания, "
                                               "тональность и ключевые слова.\n"
                                               'И да, продолжая наш диалог, Вы принимаете пользовательское соглашение')
    elif message.text == "/help":
        bot.send_message(message.from_user.id, 'Ссылка на инстукцию: ')
    else:
        complexity = Complexity(message.text)
        bot.send_message(message.from_user.id, complexity.get_message())
        tonality = Tonality(message.text, path)
        bot.send_message(message.from_user.id, tonality.get_message(tonality.model_training()))
        keywords = Keywords(message.text)
        bot.send_message(message.from_user.id, keywords.get_message())


bot.polling(none_stop=True, interval=0)
