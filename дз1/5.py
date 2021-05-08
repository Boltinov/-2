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
print("прибыль на одного сотрудника составляет " , ps)

