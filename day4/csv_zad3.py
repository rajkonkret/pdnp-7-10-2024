import pandas

# pip install pandas

data = pandas.read_csv('records_3.csv', delimiter=";")

print(data)
#    sku  exp_date   price
# 0    1     today   100.0
# 1    2     today   300.0
# 2    3  tomorrow   200.0
# 3    4     today   100.0
# 4    5     today  1000.0

print(data.columns)
# Index(['sku', 'exp_date', 'price'], dtype='object')
print(data.values)
# [[1 'today' 100.0]
#  [2 'today' 300.0]
#  [3 'tomorrow' 200.0]
#  [4 'today' 100.0]
#  [5 'today' 1000.0]]
