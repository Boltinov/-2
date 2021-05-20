# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
# результат вычисления произведения всех элементов списка. Подсказка: использовать функцию reduce().

from functools import reduce

def my_list(el1, el2):
    return el1 * el2

new_list = [el for el in range(100, 1001, 2) ]
print(f'Список четных значений {[el for el in range(100, 1001) if el % 2 == 0]}')
print(f'произведение всех четных чисел от 100 до 1000 = {reduce(my_list, [el for el in range(100, 1001, 2) if el % 2 == 0])}')

# print(reduce(lambda a, b: a * b, [x for x in range(100, 1001, 2)]))