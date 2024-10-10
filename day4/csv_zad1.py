# plik csv - dane oddzielone znakiem podziału (,;tab|)
# 1,john,2000,sales
# 11,Andrew,5000,finance
# 21,Mark,8000,hr
import csv

fields = ['name', 'branch', "year", 'cgpa']
row = ['Radek', 'Coe', 2, '9.1']

dictionary = dict(zip(fields, row))
print(dictionary)
# {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'}

filename = 'records.csv'

with open(filename, 'w', newline='') as csv_f:
    csvwriter = csv.writer(csv_f)  # narzędzie do zapisywania plików csv
    csvwriter.writerow(fields)  # zapisanie wiersza
    csvwriter.writerow(row)  # zapisanie wiersza
# name,branch,year,cgpa
# Radek,Coe,2,9.1

filename = 'records_2.csv'
with open(filename, 'w', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()  # zapisujemy nazwy kolumn
    csvwriter.writerow(dictionary)  # zapisujemy dane

products = [
    {'sku': 1, 'exp_date': 'today', 'price': 100},
    {'sku': 2, 'exp_date': 'today', 'price': 300},
    {'sku': 3, 'exp_date': 'tomorrow', 'price': 200},
    {'sku': 4, 'exp_date': 'today', 'price': 100.00},
    {'sku': 5, 'exp_date': 'today', 'price': 1000.00},
]

# fields_product = ['sku', 'exp_date', 'price']
# ta pętla domyślnie podstawia klucze
fields_product = [k for k in products[0]]
print(fields_product)  # ['sku', 'exp_date', 'price']
filename = 'records_3.csv'
with open(filename, 'w', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields_product, delimiter=";")
    csvwriter.writeheader()  # zapisujemy nazwy kolumn
    csvwriter.writerows(products)  # zapisujemy dane z listy products
# delimiter=";" - znak podziału
# newline='' - ominiecie problemu podwójnego znaku końca linii
