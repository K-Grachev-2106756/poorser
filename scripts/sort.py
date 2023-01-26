"""@package sort docstring
    Открыв файл «Products.json» можно убедиться, что приходит много
    лишних данных. Также информация о товарах и о ценах приходит не по
    списку ID.  Функция sort() используется для первичной обработки
    информации. Синхронизирует товары и их цены по коду товара. Сохраняет
    нужное в all_data.json.
"""
import json

with open("Products.json","r", encoding="utf-8") as prod:
        Products = json.load(prod)
with open("Prices.json","r", encoding="utf-8") as price:
        Prices = json.load(price)


Prices = sorted(Prices, key = lambda el : el[0])

Products = sorted(Products, key = lambda el : el["productId"])

data = []
for i in range(len(Prices)):
    properties = Products[i]["propertiesPortion"]
    propertiesPortion = []
    for j in range (len(properties)):
        propertiesPortion.append({"name": properties[j]["name"], "value": properties[j]["value"], "measure":properties[j]["measure"]})


    data.append({"productId":Prices[i][0], 
                 "name": Products[i]["name"], 
                 "rating": Products[i]["rating"]["star"], 
                 "total_price": Prices[i][1],
                 "sale_price":Prices[i][2],
                 "bonus_rubles":Prices[i][3],
                 "propertiesPortion": propertiesPortion})

with open('all_data.json','w', encoding='utf-8') as file:
        json.dump(data, file, indent = 4, ensure_ascii = False)
