'''
Написать функцию square,
принимающую 1 аргумент — сторону квадрата,
и возвращающую 3 значения (с помощью кортежа):
• периметр квадрата
• площадь квадрата
• диагональ квадрата.
'''

# Длинный вариант
def square(side_of_a_square):
    perimeter = side_of_a_square * 4
    square = side_of_a_square ** 2
    diagonal = (side_of_a_square ** 2) * 2
    diagonal = diagonal ** 0.5

    return perimeter, square, diagonal

my_input = square(int(input("Введите сторону квадрата: ")))
print(my_input)

# Короткий вариант
def square(side_of_a_square):
    return (4 * side_of_a_square, side_of_a_square ** 2, (2 * side_of_a_square ** 2) ** .5)

my_input = square(int(input("Введите сторону квадрата: ")))

print(my_input)
