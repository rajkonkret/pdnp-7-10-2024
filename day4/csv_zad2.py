import csv

fields = []
rows = []

filename = 'records_2.csv'
# filename = 'records_3.csv'

with open(filename, 'r') as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    print(dialect.delimiter)  # ;
    f.seek(0)  # ustaw odczyt na początek pliku
    # csvreader = csv.reader(f, delimiter=";")
    csvreader = csv.reader(f, delimiter=dialect.delimiter)

    print(csvreader)  # <_csv.reader object at 0x00000216C54B57E0>, iterator
    # next() - odczytuje wartośc i ustawia na następny element
    fields = next(csvreader)
    for row in csvreader:  # pętla wystartuje od drugiego elementu
        # print(row)
        rows.append(row)

print("Fields:", fields)  # Fields: ['name', 'branch', 'year', 'cgpa']
print("Rows:", rows)  # Rows: [['Radek', 'Coe', '2', '9.1']]
# Fields: ['sku;exp_date;price']
# Rows: [['1;today;100'], ['2;today;300'], ['3;tomorrow;200'], ['4;today;100.0'], ['5;today;1000.0']]
# delimiter=";"
# Fields: ['sku', 'exp_date', 'price']
# Rows: [['1', 'today', '100'], ['2', 'today', '300'], ['3', 'tomorrow', '200'], ['4', 'today', '100.0'], ['5', 'today', '1000.0']]
