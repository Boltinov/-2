month_num = int(input("введите номер месяца"))
while Truemonth_num = int(input("введите номер месяца"))
while True:
    if month_num in [ 1 , 2, 3 , 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        month_correct = month_num
        break
    else: int(input("введите порядковый номер месяца от 1 до 12 включительно"))
month_dict = {12: "зима декабрь" ,1: "зима январь", 2: "зима февраль" ,
              3: "весна март" , 4: "весна апрель", 5: "весна май",
              6: "лето июнь" , 7: "лето июль" , 8: "лето август" ,
              9: "осень сентябрь,в школу пора", 10: "осень октябрь", 11: "осень ноябрь"}
month_list = list(month_dict.values())
print(month_dict.get(month_correct))
print(month_list[month_correct])

