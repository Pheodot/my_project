'''
Написать функцию arithmetic,
принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними.
Функция должна вернуть результат вычислений зависящий от третьего

аргумент +, сложить их;
если —, то вычесть;
* — умножить;
/ — разделить (первое на второе).
В остальных случаях вернуть строку "Неизвестная операция".
'''

def arithmetic(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    else:
        return "Неизвестная операция"

first = int(input("Введите первое число : "))
second = int(input("Введите второе чиcло : "))
operation = input("Введите знак + (плюс), - (минус), * (умножить), / (делить) ")

print(arithmetic(first, second, operation))
