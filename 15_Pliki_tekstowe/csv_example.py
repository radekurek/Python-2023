import csv

with open('../17_Wykorzystanie_baz_danych/foods.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
