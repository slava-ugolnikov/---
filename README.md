# Chatbot for text analysis

This chatbot in Telegram would provide you with text analysis in Russian. It can asses readability, affective state of an author and identify keywords of a text.
You can check how it workds now here https://t.me/Ling22FPLBot or use our code for your own projects!

## requirements
Before implementing the code be sure to install all the libraries and submodules.

## Readability
It is assessed by Flesch–Kincaid formula for automated readability analysis:
FRE = 206,835 − 1,52 × ASL − 65,14 × ASW, where ASL is an average sentence length and ASW is an average number of syllables per word.

Libraries & submodules: Re.

## Affective state
Sentiment analysis is conducted automatically, too. Though, two versions are presented. One is made by our command and the other is made by using dostoevsky library.

Libraries & submodules: Pandas, Sklearn, Dostoevsky.

## Keywords
Keywords in this project are the most frequent words of the text. 

Libraries & submodules: NLTK, String, Pymorphy3.

## Recommendations
Since this code is designed for Telegram chats, the text length is limited. Try not to analyze texts longer than 10-15 sentences.

## Authors 
This chat would have not been introduced to this world without work of Abramova Ulyana, Borodina Sofya, Kramkova Maria, Mokina Marina and Ugolnikov Vyacheslav.
