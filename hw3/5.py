def summ():
    a = 0
    while True:
        list = input('введите числа через пробел, для выхода из программы нажмите q').split()
        for el in list:
            if el == 'q':
                return a
            else:
                try:
                    a += int(el)
                except ValueError:
                    print('нажмите q для выхода из программы')
        print(f'сумма ваших чисел = {a}')
print(summ())


