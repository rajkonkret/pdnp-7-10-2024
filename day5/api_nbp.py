import requests

# REST API
# pip install requests
url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"

# HTTP GET
response = requests.get(url)
print(response)  # <Response [200]>
# 200 - ok
# 3xx - ostrzeżenia, przekierowania itd
# 4xx - 404 błedny adres, 400 Bad Request - błądd w parametrach
# 5xx  - błędy serwera

print(response.text)  # json jako tekst
data = response.json()  # zamiana jsona na słownik
print(type(data))
print(data)  # <class 'dict'>
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '199/A/NBP/2024', 'effectiveDate': '2024-10-11', 'mid': 3.9204}]}
# kod waluty i kurs
print(data.keys())
# dict_keys(['table', 'currency', 'code', 'rates'])
print(data['code'])  # USD
print(data['rates'])  # [{'no': '199/A/NBP/2024', 'effectiveDate': '2024-10-11', 'mid': 3.9204}]
print(data['rates'][0])  # {'no': '199/A/NBP/2024', 'effectiveDate': '2024-10-11', 'mid': 3.9204}
print(data['rates'][0]['mid'])  # 3.9204
