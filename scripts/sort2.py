"""@package sort2 docstring
    Используется для сортировки данных в all_data.json
    по размеру скидки. Отсортированные данные
    переписывает в all_data.json.
"""
import json

with open("all_data.json","r") as dat:
        data = json.load(dat)

data = sorted(data, key = lambda el : el["sale_price"]/el["total_price"])

with open('all_data.json','w') as file:
        json.dump(data, file, indent = 4, ensure_ascii = False)