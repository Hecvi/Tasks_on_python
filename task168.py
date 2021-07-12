"""
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к
парному ему слову. Все слова в словаре различны. Для одного данного слова
определите его синоним. Программа получает на вход количество пар синонимов
N. Далее следует N строк, каждая строка содержит ровно два слова-синонима.
После этого следует одно слово. Эту задачу можно решить и без словарей
(сохранив все входные данные в списке), но решение со словарем будет более
простым
"""


def findWord(dictOfWords, word):
    for k, v in dictOfWords.items():
        if k == word:
            return print(v)
        elif v == word:
            return print(k)


dictOfWords = {}
for i in range(int(input())):
    key, value = input().split()
    dictOfWords[key] = value
word = input().strip()
findWord(dictOfWords, word)
