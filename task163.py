"""
Во входном файле (вы можете читать данные из файла input.txt) записан текст.
Словом считается последовательность непробельных подряд идущих символов.
Слова разделены одним или большим числом пробелов или символами конца строки.
Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в
этом тексте ранее
"""


dictOfWords = {}
with open('input.txt', encoding='utf8') as file:
    for line in file:
        newStr = line.split()
        for word in newStr:
            if word not in dictOfWords:
                dictOfWords[word] = -1
            dictOfWords[word] += 1
            print(dictOfWords[word], end=' ')
