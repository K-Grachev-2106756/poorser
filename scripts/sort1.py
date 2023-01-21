"""@package sort1 docstring
    Используется для сортировки данных в all_data.json
    по актуальной цене. Отсортированные данные
    переписывает в all_data.json.
"""
import json

with open("all_data.json","r", encoding="utf-8") as dat:
        data = json.load(dat)

data = sorted(data, key = lambda el : el["sale_price"])

with open('all_data.json','w', encoding='utf-8') as file:
        json.dump(data, file, indent = 4, ensure_ascii = False)
