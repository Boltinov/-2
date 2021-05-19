# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

arg1 = int(input('введите первое число'))
arg2 = int(input('введите второе число'))
arg3 = int(input('введите третье число'))

def my_func(arg1, arg2, arg3):
    list = [arg1, arg2, arg3]
    return sum(sorted(list)[1:])

print(my_func(arg1, arg2,arg3))


