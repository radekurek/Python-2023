import csv


class FoodItem:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f'FoodItem({self.id}, "{self.name}", {self.price})'


food_items = []

with open('foods.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        item = FoodItem(**row)
        print(item)