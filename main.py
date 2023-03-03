print("Cписок покупок")
shopping_dict = {"пекарня":['хліб', 'булочки', 'пончик'],
"продуктовий": ['морква', 'селера', 'рукола']
}
shopping_dict ["господарчий"] = ["відро", "швабра"]
for keys, values in shopping_dict.items():
    print(f"Заходжу в {keys.title()}, купую тут такі товари:{values.__str__().title()}")
  
value1 = shopping_dict["пекарня"]
value2 = shopping_dict["продуктовий"]
value3 = shopping_dict["господарчий"]
print(f"Разом купую {len(value1) + len(value2) + len(value3)} товарів")


