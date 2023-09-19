'''Задание 2:
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 
10 самых частых. Не учитывать знаки препинания и регистр символов. За основу 
возьмите любую статью из википедии или из документации к языку.
Ввод:
текст отсюда (https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%80%D0%BB%D0%B8,
_%D0%A1%D0%B8%D0%BB%D1%8C%D0%B2%D0%B0%D0%BD%D1%83%D1%81)
Вывод:
Слово "в", 22 раз
Слово "и", 11 раз
Слово "году", 9 раз
Слово "с", 4 раз
Слово "морли", 4 раз
Слово "по", 3 раз
Слово "степень", 3 раз
Слово "института", 3 раз
Слово "был", 3 раз
Слово "памятников", 3 раз'''

COUNTER = 1
my_text = input('Введите текст: ')
print()
my_text = my_text.replace('.', '')
my_text = my_text.replace(',', '')
my_text = my_text.replace(';', '')
my_text = my_text.replace(':', '')
my_text = my_text.replace('(', '')
my_text = my_text.replace(')', '')
my_text = my_text.replace('[', ' ')
my_text = my_text.replace(']', ' ')
my_text = my_text.replace('—', ' ')
my_text = my_text.replace('«', '')
my_text = my_text.replace('»', '')
my_text = my_text = my_text.lower()
my_text_list = my_text.split()
my_dict = {}
for word in my_text_list:
    my_dict[word] = my_dict.get(word, 0) + 1
sorted_my_dict = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
for key, value in sorted_my_dict:
    if COUNTER <= 10:
        print(f'Слов "{key}", {value} раз(-а)')
        COUNTER += 1
    else:
        break
