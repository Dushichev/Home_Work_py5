#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


text = 'не выходи из комнаты, абв не совершай ошибку абв, зачем тебе солнце абв, если ты куришь шипку абв"'

def delite_abv(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = delite_abv(text)
print(text)