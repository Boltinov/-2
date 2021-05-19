products, order = [], 1
while True:
    title = input("введите название товара : ")
    price = input('введите цену товара :')
    amount = input('введите количество :')
    unit = input('введите еденицы измерения')
    products.append((order, {'title': title,
                             'price': price,
                             'amount': amount,
                             'unit': unit}))
    order += 1
    ask = input('завершено форматирование списка? (y/n)')
    if ask == 'y':
        break
analitika = {'title': [],
             'price': [],
             'amount': [],
             'unit': set()}
for nomer, opisanie in products:
    analitika['title'].append(opisanie['title'])
    analitika['price'].append(opisanie['price'])
    analitika['amount'].append(opisanie['amount'])
    analitika['unit'].add(opisanie['unit'])

print(products)
print(analitika)
