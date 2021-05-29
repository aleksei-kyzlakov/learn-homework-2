# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count("а"))


# Вывести количество гласных букв в слове
word = 'Архангельск'
print(len([1 for letter in word.lower() if letter in "аяэеыиоёую"]))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
print("{:.2}".format(len(sentence.replace(" ", "")) / len(sentence.split())))