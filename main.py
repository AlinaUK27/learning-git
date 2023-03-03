print("Cписок покупок")
shopping_dict = {"пекарня":['хліб', 'булочки', 'пончик'],
"продуктовий": ['морква', 'селера', 'рукола']
}
shopping_dict ["господарчий"] = ["відро", "швабра"]
del shopping_dict ["пекарня"]

for keys, values in shopping_dict.items():
    print(f"Заходжу в {keys.title()}, купую тут такі товари:{values.__str__().title()}")
  
value2 = shopping_dict["продуктовий"]
value3 = shopping_dict["господарчий"]
print(f"Разом купую {len(value2) + len(value3)} товарів")


