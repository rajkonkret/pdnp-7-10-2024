# Kolekcje
# lista - przechowuje wiele danych, różnego typu
# zachowuje kolejnść przy dodawaniu elementów
from day1.formaty import liczba

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

# nadpisanie elemntu listy
lista[3] = "Mikołaj"
print(lista)  # ['Radek', 'Zenek', 'Tomek', 'Mikołaj', 'Ania', 'Magda']

# dopisanie elementu do listy na konkretnym miejscu
lista.insert(1, "Marcin")
print(lista)  # ['Radek', 'Marcin', 'Zenek', 'Tomek', 'Mikołaj', 'Ania', 'Magda']
print(len(lista))  # 7

# sprawdzanie indeksu dla elementu, indeks pierwszego wystąpienia
print(lista.index("Tomek"))  # indeks numer 3 (miejsce 4)

# usunięcie elementu, pierwszego wystąpienia
lista.append("Zenek")
lista.append("Zenek")
print(lista)  # ['Radek', 'Marcin', 'Zenek', 'Tomek', 'Mikołaj', 'Ania', 'Magda', 'Zenek', 'Zenek']
lista.remove("Zenek")
print(lista)  # ['Radek', 'Marcin', 'Tomek', 'Mikołaj', 'Ania', 'Magda', 'Zenek', 'Zenek']
print(lista.remove("Zenek"))  # None
print(lista)  # ['Radek', 'Marcin', 'Tomek', 'Mikołaj', 'Ania', 'Magda', 'Zenek']

# usunięcie po indeksie, zwraca co usunełą
print(lista.pop(5))  # Magda
print(lista)
print(lista.pop(-2))  # Ania
print(lista.pop())  # Zenek, ostatni element z listy

a = 1
b = 2
a = b
print(a, b)  # 2 2
b = 7
print(a, b)  # 2 7

lista_2 = lista  # a = b, kopia refernecji (adresu w pamięci)
lista_copy = lista.copy()  # kopia elementów listy
print(lista_2, lista)
# ['Radek', 'Marcin', 'Tomek', 'Mikołaj'] ['Radek', 'Marcin', 'Tomek', 'Mikołaj']
lista.clear()  # usunięcie elementów listy lista, b = 7
print(lista_2, lista)  # [] []
# obie listy wskazują na ten sam adres w pamięci
print(id(lista_2))  # 2630006149504
print(id(lista))  # 2630006149504

print(lista_copy)  # ['Radek', 'Marcin', 'Tomek', 'Mikołaj']
print(id(lista_copy))  # 2630009552640

liczby = [54, 999, 34, 22, 12.34, 687]
print(liczby)  # [54, 999, 34, 22, 12.34, 687]
print(type(liczby))  # <class 'list'>

liczby.sort()  # sortowanie listy (zmienia bazową)
print(liczby)  # [12.34, 22, 34, 54, 687, 999], zamieniana jest bazowa lista

liczby = [54, 999, 34, 22, 12.34, 687, "A"]
print(liczby)  # [54, 999, 34, 22, 12.34, 687, 'A']

# liczby.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

lista_osob = ['radek', 'ola', 'lena', 'agata', 'zenek']
lista_osob.sort()
print(lista_osob)  # ['agata', 'lena', 'ola', 'radek', 'zenek']

lista_osob.reverse()  # odwrócenie listy
print(lista_osob)  # ['zenek', 'radek', 'ola', 'lena', 'agata']

lista_osob.sort(reverse=True)  # sortowanie i odwrócenie
print(lista_osob)  # ['zenek', 'radek', 'ola', 'lena', 'agata']

liczby[3] = 666
print(liczby[0:3])  # [54, 999, 34]
print(liczby[-2])  # 687
print(liczby)  # [54, 999, 34, 666, 12.34, 687, 'A']

print(liczby.pop(2))  # usuniecie elemntu o indeksie 2, liczba 34
liczby.remove(54)  # usuniecie liczby 54 z listy
print(liczby)  # [999, 666, 12.34, 687, 'A']

del liczby
# print(liczby)  # NameError: name 'liczby' is not defined. Did you mean: 'liczba'?

tekst = "Pyt hon."
lista1 = list(tekst)
print(lista1)  # ['P', 'y', 't', ' ', 'h', 'o', 'n', '.'] rozpakowanie sekwencji

lista2 = [tekst]
print(lista2)  # ['Pyt hon.']

krotka = tuple(lista_copy)  # tuple() rzutownie na krotkę (tuplę)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # ('Radek', 'Marcin', 'Tomek', 'Mikołaj')
