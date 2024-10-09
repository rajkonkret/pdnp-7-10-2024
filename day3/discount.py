from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2024-10-09
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2024-10-09 14:26:24.041392

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2024-10-10

print(time.time())
print(today.day)
print(time.hour)
# 14:32:04.854074
# 9
# 14

formatted_date = datetime.now().strftime("%d/%m/%Y")
print(formatted_date)  # 09/10/2024
print(type(formatted_date))  # <class 'str'>

# 14:45
formatted_time = datetime.now().strftime("%H:%M")
print(formatted_time)  # 14:40

formatted_time_12h = datetime.now().strftime("%I:%M %p")
print(formatted_time_12h)  # 02:41 PM

# zamiana stringa z datą na typ datatime
data_object = datetime.strptime("09/10/2024", "%d/%m/%Y")
print(data_object)  # 2024-10-09 00:00:00
print(type(data_object))  # <class 'datetime.datetime'>

products = [
    {'sku': 1, 'exp_date': today, 'price': 100},
    {'sku': 2, 'exp_date': today, 'price': 300},
    {'sku': 3, 'exp_date': tomorrow, 'price': 200},
    {'sku': 4, 'exp_date': today, 'price': 100.00},
    {'sku': 5, 'exp_date': today, 'price': 1000.00},
]

for p in products:
    # print(p) # {'sku': 1, 'exp_date': datetime.date(2024, 10, 9), 'price': 100}
    # print(p['exp_date'])

    if p['exp_date'] != today:
        continue
    p['price'] *= 0.8  # price = price * 0.8
    print(f"""Price for sku {p['sku']}
    is now {p['price']}""")
