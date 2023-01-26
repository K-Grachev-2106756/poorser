"""@package sort2 docstring
    Функция sort1() используется для сортировки данных в all_data.json по
    размеру скидки. В зависимости от настроек пользователя может быть
    вызвана или не вызвана С++ кодом. Отсортированные данные
    перезаписываются в all_data.json в том же формате.
"""
import json

with open("all_data.json","r", encoding="utf-8") as dat:
        data = json.load(dat)

data = sorted(data, key = lambda el : el["sale_price"]/el["total_price"])

with open('all_data.json','w', encoding='utf-8') as file:
        json.dump(data, file, indent = 4, ensure_ascii = False)