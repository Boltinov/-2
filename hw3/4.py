# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
# выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

x = float(input('введите дробное положительное число'))
y = int(input('введите отрицательное целое число'))

def my_funk(x, y):
    return 1 if y == 0 else my_funk(x, y + 1) * 1 / x
# через рекурсию, 2*3 = 2*2*2 если 2*-3 то 1/(2*2*2)!!!!!!!!!!!!!!

print(my_funk(x ,y))



