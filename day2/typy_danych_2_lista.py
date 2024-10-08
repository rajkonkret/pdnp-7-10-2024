# Kolekcje
# lista - przechowuje wiele danych, różnego typu
# zachowuje kolejnść przy dodawaniu elementów

# pusta lista
lista = []  # nawiasy kwadratowe są charakterystyczne dla listy
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)  # []
print(type(pusta_lista))  # <class 'list'>

# append() - dodanie lementó do listy
lista.append("Radek")
lista.append("Zenek")
lista.append("Tomek")
lista.append("Marek")
lista.append("Ania")
lista.append("Magda")
print(lista)
# ['Radek', 'Zenek', 'Tomek', 'Marek', 'Ania', 'Magda']
#     0        1        2         3       4       5
#     -6      -5        -4       -3      -2      -1
print(len(lista))  # długośc listy 6
print(lista[0])  # Radek
print(lista[2])  # Tomek
print(lista[4])  # Ania

# print(lista[9]) # IndexError: list index out of range

print(lista[len(lista) - 1])  # Magda
print(lista[-1])  # Magda
print(lista[-2])  # Ania

# wyświetlenie fragmentu listy (slicowanie)
print(lista[0:3])  # [start:stop] -> 012, ['Radek', 'Zenek', 'Tomek']
print(lista[:3])  # ['Radek', 'Zenek', 'Tomek']
print(lista[2:])  # ['Tomek', 'Marek', 'Ania', 'Magda'], indeksy 2345
print(lista[2:5])  # ['Tomek', 'Marek', 'Ania'] indeksy 234
print(lista[2:10])  # ['Tomek', 'Marek', 'Ania', 'Magda']
print(lista[10:20])  # []
print(lista[2:3])  # ['Tomek'] tylko indeks 2
print(lista[:])  # ['Radek', 'Zenek', 'Tomek', 'Marek', 'Ania', 'Magda']
print(lista[3:3])  # []

print(lista[-2:0])  # [4:0], []
print(lista[0:-2])  # [0:4], ['Radek', 'Zenek', 'Tomek', 'Marek']

lista_15 = list(range(15))  # 0..14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[0:15:2])  # [start:stop:step], [0, 2, 4, 6, 8, 10, 12, 14]
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14]
print(lista_15[-10])  # liczba 5
