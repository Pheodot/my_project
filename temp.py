'''
Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).

Пример:
checkio(123405) == 120
checkio(999) == 729
checkio(1000) == 1
checkio(1111) == 1
'''

# arg = input("Введите число: ")
# def my_def(arg):
#
#     multiplication_of_numbers = 1
#     for num in arg:
#         if num == "0":
#             continue
#         multiplication_of_numbers *= int(num)
#     return multiplication_of_numbers
#
# print("Результат:", my_def(arg))


# a = 123405 # == 120
# b = 999 # == 729
# c = 1000 # == 1
# d = 1111 # == 1
#
# def my_def(arg):
#
#     multiplication_of_numbers = 1
#     for num in str(arg):
#         if num == "0":
#             continue
#         multiplication_of_numbers *= int(num)
#     return multiplication_of_numbers
#
# num1 = my_def(a)
# num2 = my_def(b)
# num3 = my_def(c)
# num4 = my_def(d)
#
# print(num1)
# print(num2)
# print(num3)
# print(num4)

# name1 = "Tom"
# height1 = 1.80
# weight1 = 80
#
# name2 = "Katy"
# height2 = 1.70
# weight2 = 80
#
# name3 = "Bob"
# height3 = 2
# weight3 = 150
#
# def bmi_calculator(name, height, weight):
#     bmi = weight / (height ** 2)
#
#     print("Индекс массы тела: " + str(bmi))
#
#     if bmi < 25:
#         return name + " не имеет лишний вес"
#     else:
#         return name + " имеет лишний вес"
#
# bmi1 = bmi_calculator(name1, height1, weight1)
# bmi2 = bmi_calculator(name2, height2, weight2)
# bmi3 = bmi_calculator(name3, height3, weight3)
#
# print(bmi1)
# print(bmi2)
# print(bmi3)

# miles = int(input("Введите количество миль: "))
# def miles_converter(miles):
#     return miles * 1.609
#
# print(miles_converter(miles))

# a = int(input("Введите число: "))
# def is_even(a):
#     if a % 2 == 0:
#         return "Это чётное число"
#     else:
#         return "Это нечётное число"
# print(is_even(a))
#
# a = int(input("Введите число: "))
# def is_even(a):
#     return "Это чётное число" if a % 2 == 0 else "Это нечётное число"
# print(is_even(a))

# x = int(input())
# def conv(x):
#     return str(x) + " miles = " + str(x*1.609) + " km"
# print(conv(x))
import random

slovar = {1: "Иванов Иван Иванович", 2: "Сергеев Сергей Сергеевич", 3: "Петров Пётр Петрович"}
print(random.choice(list(slovar.values())))
