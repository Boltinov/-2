# # : 1
a = 10
b = 20
c = a + b
print(c)

name = input("введите ваше имя")
age = input("введите ваш возраст")
s = input("ваше любимое число")

print('привет ' + name , "вам " + age, "лет")
print("ваше любимое число " + s)

# : 2
time = int(input("введите время в секундах"))
print(time , "секунд это")
hours = time // 3600
minutes = (time - hours * 3600) // 60
second = time - (hours * 3600 + minutes * 60)
print(hours, "часов", minutes , "минут", second , "секунд")

#3
n = int(input("введите любое число "))
number = str(n)
n1 = number + number
n2 = number + number + number
print(str(n), "+", str(n1), "+", str(n2))
plus = n + int(n1) + int(n2)
print(plus)

#4
n = int(input("введите ваше целое число"))
a = n%10
n = n//10
while n > 0:
    if n%10 > a:
        a = n%10
    n = n//10
print("самая большая цифра в вашем числе будет ", a)

#:5
sales = int(input("введите вашу выручку"))
invest = int(input("введите ваши издержки"))
if sales > invest:
    print("вы в плюсе!")
    a = sales - invest
    rent = a / sales * 100
    print("выша прибыль составила" , a ,"  а  рентабельность " , int(rent) , "%")
elif sales < invest:
    print("вы в минусе")
    b = invest - sales
    print("выш убыток составляет " , b)
else:
    print("сработали в ноль")

person = int(input("введите количество сотрудников в вашей компании"))
ps = int(a / person)
print("прибыль на одного сотрудника составляет " , ps , "рубля")

#6
a = float(input("введите количество километов,которое пробежал спортсмен за первый день"))
b = float(input("какое расстояние спортмен должен пробегать"))
print("каждый день спортсмен набирает 10% к тому расстоянию которое он пробегает ")
day = int(1)
while a < b:
    a = a * 1.1
    day += 1
    if a >= b:
        break
print("спортсмен достигнет результата на %.d день тренировок" % day)
