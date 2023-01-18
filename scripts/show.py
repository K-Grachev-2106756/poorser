"""@package show docstring
    Используется для форматированного вывода актуальной
    информации о товарах в консоль. Берет информацию из
    all_data.json.
"""
import json

with open("all_data.json","r") as inf:
        data = json.load(inf)

for i in range (len(data)):
    print('='*100)
    
    product = data[i]
    print("productId:\t",product["productId"])
    print("name:\t\t", product["name"])
    print("rating:\t\t", product["rating"])

    print()

    print("total_price:\t", product["total_price"])
    print("sale_price:\t", product["sale_price"])
    print("bonus_rubles:\t", product["bonus_rubles"])

    print()
    properties = product["propertiesPortion"]
    print("propertiesPortion: ")
    for j in range (len(properties)):
        print('\t{0}: '.format(properties[j]["name"]).ljust(30) + properties[j]["value"])
    print()

print('='*100)
print()



