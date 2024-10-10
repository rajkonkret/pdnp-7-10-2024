# {"firstName":"John", "lastName":"Doe"}
# dane typu klucz wartość
# używany do komunikacji pomiędzy sytemami w internecie
# w pythonie dane json zamieniją się na słownik
import json

person_dict = {'name': "Radek", 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

# {"name": "Radek", "age": 40, "czy_pali": null}
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f)

# upiększenie
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4)
    # {
    #     "name": "Radek",
    #     "age": 40,
    #     "czy_pali": null
    # }

# sortowanie kluczy
with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

# wczytanie pliku
with open('nasze_dane.json', 'r') as f:
    data = json.load(f)

print(data)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>
print(data['name'])  # Radek

# zamiana słownika na json
json_text = json.dumps(data)
print(type(json_text))  # <class 'str'>
print(json_text)  # {"age": 40, "czy_pali": null, "name": "Radek"}

# zamiana jsona na słownik
dict_json = json.loads(json_text)
print(dict_json)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(dict_json))  # <class 'dict'>

# wypisac ze słownika klucze i wartosci ustawiając znak sep
for key, value in dict_json.items():
    print(key, value, sep=" <=> ")
# age <=> 40
# czy_pali <=> None
# name <=> Radek
