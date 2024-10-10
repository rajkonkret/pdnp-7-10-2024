# funkcje lambda
# skrócony zakres funkcji
# zwraca wynik
# lambda jako funkcja anonimowa
def odejmij(a, b):
    return a - b


print(odejmij(8, 23))  # -15

odejmij2 = lambda a, b: a - b
print(odejmij2(10, 6))  # 4

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie
# pomnożyc kazdy element przez 2 i wypisac
lista = [1, 2, 3, 10, 20, 30, 60, 100, 300, 500]
lista_wyn = []
for i in lista:
    lista_wyn.append(i * 2)

print(lista_wyn)  # [2, 4, 6, 20, 40, 60, 120, 200, 600, 1000]
print([i * 2 for i in lista])  # [2, 4, 6, 20, 40, 60, 120, 200, 600, 1000]

lista_wyn_2 = []


def zmien(x):
    return x * 2


for i in lista:
    lista_wyn_2.append(zmien(i))

print(lista_wyn_2)  # [2, 4, 6, 20, 40, 60, 120, 200, 600, 1000]

# map() -  funkcje wyzszego rzędu
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 20, 40, 60, 120, 200, 600, 1000]

# zastosowanie lambdy jako funkcji anonimowej
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 6, 20, 40, 60, 120, 200, 600, 1000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 14, lista))}")
# Zastosowanie map(): [4, 8, 12, 40, 80, 120, 240, 400, 1200, 2000]
# Zastosowanie map(): [14, 28, 42, 140, 280, 420, 840, 1400, 4200, 7000]
