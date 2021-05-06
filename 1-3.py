a = 10
b = 20
c = a + b
print(c)

name = input("введите ваше имя")
age = input("введите ваш возраст")
s = input("ваше любимое число")

print('привет '+ name , "вам " + age, "лет")
print("ваше любимое число " + s)

time = int(input("введите время в секундах"))
print(time, "секунд это")
hours = time // 3600
minutes = (time - hours * 3600) // 60
second = time - (hours * 3600 + minutes * 60)
print(hours ,"часов", minutes ,"минут", second , "секунд")
