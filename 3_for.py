"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


import numpy

phone_sold_list = [
  {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
  {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
  {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]  

def main(phone_sold_list):
  sum_all_phones_sold = 0

  for product in phone_sold_list:
    sum_phones = sum(product['items_sold'])
    avg_phones_sold = int(numpy.mean(product['items_sold']))
    sum_all_phones_sold += sum_phones
    print(f"Всего продали {product['product']}  - {sum_phones}")
    print(f"В среднем продали {product['product']}  - {avg_phones_sold}\n")

  print(f"Всего проданных товаров - {sum_all_phones_sold}\n")
  
  avg_all_items_sold = sum_phones / len(phone_sold_list)
  print(f"В среднем продаж всех товаров - {int(avg_all_items_sold)}")
  
if __name__ == "__main__":
    main(phone_sold_list)