'''
Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).

Пример:
checkio(123405) == 120
checkio(999) == 729
checkio(1000) == 1
checkio(1111) == 1
'''

arg = input("Введите число: ")
def my_def(arg):

    multiplication_of_numbers = 1
    for num in arg:
        if num == "0":
            continue
        multiplication_of_numbers *= int(num)
    return multiplication_of_numbers

print("Результат:", my_def(arg))
