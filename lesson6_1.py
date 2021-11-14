'''
В единственной строке записан текст. Для каждого слова из данного текста, подсчитайте сколько раз оно встречалось в
этом тексте.
Использовать словарь! Без сторонних модулей!
'''

my_keys = ('смартфон', 'телевизор', 'планшет', 'смартфон', 'монитор', 'телевизор', 'компьютер', 'планшет', 'смартфон')
my_dict = {}
my_dict = my_dict.fromkeys(my_keys, 0)

for word in my_keys:
    if my_dict.get(word) is not None:
        my_dict[word] += 1

print(my_dict)


# Ещё интересный вариант как можно решить
# input_text = 'смартфон, телевизор, планшет, смартфон, монитор, телевизор, компьютер, планшет, смартфон'
# words_counter = {}
# for word in input_text.split(", "):
#     try:
#         words_counter[word] += 1
#     except KeyError:
#         words_counter[word] = 1
# print(words_counter)
