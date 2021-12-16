'''
Даны два списка чисел (можно сгенерировать при помощи генератора случайных чисел). Посчитайте, сколько уникальных чисел
содержится одновременно как в первом списке, так и во втором.
- Примечание.
Эту задачу можно решить в одну строчку.
Множество использовать нельзя
'''

import random


lst1 = [random.randint(1, 100) for _ in range(10)]
lst2 = [random.randint(1, 100) for _ in range(20)]
print(lst1, lst2) # Добавил для наглядности в коде
lst3 = []
for el in lst1 + lst2:
    if el not in lst3:
        lst3.append(el)
# print(lst3) # Добавил для наглядности в коде
print("Количество уникальных чисел в двух списках:", len(lst3))
print("Количество уникальных чисел в двух списках:",len([i for i in [*lst1, *lst2] if [*lst1, *lst2].count(i) == 1]))


# import random
# from collections import Counter
# print(lst1, lst2) # Добавил для наглядности в коде
# lst4 = Counter(lst1 + lst2)
# print("Количество уникальных чисел в двух списках:", len(lst4))