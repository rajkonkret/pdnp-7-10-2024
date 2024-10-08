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

tupla_imiona = "Radek", "Tomek", 'Zenek', 'Marcin', "Ania", "Magda"
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Marcin', 'Ania', 'Magda')
print(type(tupla_imiona))  # <class 'tuple'>

print(tupla_imiona.index("Radek"))  # indeks 0
print(tupla_imiona.count("Zenek"))  # wystepuje 1 raz

print(len(tupla_imiona))  # długość tupli 6

# sorted() - sortowanie kolekcji
# sortowanie krotki zwróci nową listę
print(sorted(tupla_imiona))  # ['Ania', 'Magda', 'Marcin', 'Radek', 'Tomek', 'Zenek']
# nie zmieni samej krotki
print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Marcin', 'Ania', 'Magda')

# rozpakowanie tupli (krotki)
tup = 1, 2
print(type(tup))  # <class 'tuple'>
a, b = 1, 2
print(a, b)  # 1 2
c, d = tup
print(c, d)  # 1 2
tup_2 = 1, 2, 3
# a, b = tup_2  # ValueError: too many values to unpack (expected 2)
a, *b = tup_2  # * worek na pozostałe dane
print(a, b)  # 1 [2, 3]

print(tupla_imiona)  # ('Radek', 'Tomek', 'Zenek', 'Marcin', 'Ania', 'Magda')

# name1,name2,name3 - rozpakowac tuple na trzy zmienne
name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)  # Radek Tomek ['Zenek', 'Marcin', 'Ania', 'Magda']

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Radek ['Tomek', 'Zenek', 'Marcin', 'Ania'] Magda

*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)  # ['Radek', 'Tomek', 'Zenek', 'Marcin'] Ania Magda

lista = list(tupla_imiona)
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Marcin', 'Ania', 'Magda']
print(type(lista))  # <class 'list'>

tupla_lista = tuple(lista)
print(tupla_lista)  # ('Radek', 'Tomek', 'Zenek', 'Marcin', 'Ania', 'Magda')
print(type(tupla_lista))  # <class 'tuple'>
