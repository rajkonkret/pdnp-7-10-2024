# słownik dane typu para klucz-wartosc
# {'user' : 'Radek', 'wiek' : 78}
# {"firstName":"John", "lastName":"Doe"}
# słownik jest odwzorowaniem jsona w pythonie
# nie mog sie powtórzyć klucze

# pusty słownik
dictionary = dict()
print(type(dictionary))
print(dictionary)  # {}

dictionary_1 = {}
print(type(dictionary_1))  # <class 'dict'>
print(dictionary_1)  # {}

# dodanie elementów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 38
print(dictionary)  # {'imie': 'Radek', 'wiek': 38}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 38])
# dict_items([('imie', 'Radek'), ('wiek', 38)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 38}

# wypisanie element ze słownika
print(dictionary['imie'])  # Tomek
# print(dictionary['Imie'])  # KeyError: 'Imie', nie ma takiego klucza w słowniku
print(dictionary.get("Imie"))  # zwróci None gdy nie ma klucza w słowniku
print(dictionary.get('Imie', "Default"))  # Default

dictionary.update({'date': '12-12-2024'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 38, 'date': '12-12-2024'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ('z', 6)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 6}

# input() - pobiera dane od użytkownika, zwraca stringa
# tekst = input("Podaj imię")
# print(type(tekst))
# print(tekst)
# Podaj imięRadek
# <class 'str'>
# Radek
# Podaj imię12345
# <class 'str'>
# 12345

# aplikacje kalkulator
# pobrac dwie liczby -> input() x 2
# wyswietlic wynik działania -> print()

# a = input("Podaj pierwszą liczbę")  # str
# b = float(input("Podaj pierwszą liczbę"))
# print(int(a) + b)  # 11.0
# ctrl / - komentarz
# Podaj pierwszą liczbę5
# Podaj pierwszą liczbę6
# 11.0

# napisać aplikacje słownik
# pol - ang
# zdefiniowany słownik
# wyświetlic klucze
# pobrać słowo do przetłumaczenia
# wyswielic wartośc dla klucza
pol_ang = {'kot': 'cat', 'pies': 'dog', 'dach': 'roof'}
print("Mam takie słowa:", pol_ang.keys())
odp = input("Podaj słówko do przetłumaczenia")
print(pol_ang[odp.lower().replace(" ", "")])
print(pol_ang.get(odp.lower().strip()))
print(pol_ang.get(odp.lower().strip(), "nie mo"))
# Mam takie słowa: dict_keys(['kot', 'pies', 'dach'])
# Podaj słówko do przetłumaczeniaK o t
# cat
# None
# nie mo
