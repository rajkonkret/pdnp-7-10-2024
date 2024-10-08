# krotka - kolekcja niemutowalna
# pozwala efektywniej zarzadzac pamięcią
# krotka jednoelementowa - stała - zmienna

tupla = "Radek"
print(type(tupla))  # <class 'str'>

tupla_2 = ("Radek")
print(type(tupla_2))  # <class 'str'>

# przecinek wyznacza tuplę
tupla_3 = "Radek",
print(type(tupla_3))  # <class 'tuple'>
print(tupla_3)  # ('Radek',)

# PEP8 zaleca aby jedoelementową tuple tworzyc z nawiasami ()
tupla_4 = ('Radek',)
print(type(tupla_4))  # <class 'tuple'>
print(tupla_4)  # ('Radek',)

tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)

# tupla jest niemutowalna, nie da się dokonać zmian
# tupla_liczby[2] = 123  # TypeError: 'tuple' object does not support item assignment

del tupla_liczby  # usunięcie całej tupli
# print(tupla_liczby)  # NameError: name 'tupla_liczby' is not defined