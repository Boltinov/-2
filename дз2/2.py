a = int(input("введите целое число"))
b = float(input("введите дробное число"))
c = input("введите текст")
d = int(input("введите число целое еще"))
e = input("введите свой возраст")
spisok = [a, b, c, d, e]
print(spisok)
q = 0
for i in range(int(len(spisok)/2)):
    spisok[q], spisok[q + 1] = spisok[q + 1], spisok[q]
    q += 2
    print(spisok)






