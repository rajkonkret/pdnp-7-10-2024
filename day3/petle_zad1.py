# pętle - daje daje nam mozliwosc wykonania tego samego kodu wielokrotnie
# for - pętla iteracyjna
import random
from turtledemo.penrose import start

from day1.teksty import encode_s

# służy do działanai na liczbach losowych

for i in range(5):  # 0..4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(5):  # _ - niema zmienna
    print("To jest pętla")
    # print(_)

for i in range(20):
    print(i * 2)

print("------")
"""Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100))  # int od 1 do 100
print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # int od 0 do 4
print(random.random())  # 0.9433044189145435, float, od 0 do 0.9999999
print(random.random() * 8)  # 4.402304243598092, od 0 do 7.9999999

lista = [67, 45, 32, 68, 89, 90, 42]
print(random.choice(lista))  # element z listy -> 45

print("------")
# lotto
#
lista_kule = list(range(1, 50))  # od 1 do 49
# print(lista_kule)

lista_wylosowane = []
for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    lista_wylosowane.append(wyn)

print(lista_wylosowane)  # [30, 32, 24, 21, 12, 6]

print(random.choices(lista_kule, k=6))  # [35, 16, 33, 15, 35, 43] losuje  powtórzeniami
print(random.sample(lista_kule, k=6))  # [19, 21, 49, 1, 39, 47]
print(random.sample(lista_kule, 6))  # [23, 44, 31, 29, 39, 25]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehension
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

print(lista_wylosowane)
for c in lista_wylosowane:
    if c > 10:
        print("Większe od 10", c)
    else:
        print("C mniejsze od 10", c)
# Większe od 10 11
# Większe od 10 28
# Większe od 10 34
# C mniejsze od 10 1
# Większe od 10 17
# Większe od 10 15

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(10, 0, -2):  # start, stop, krok
    print(i)
# 10
# 8
# 6
# 4
# 2

for i in range(-10, 0):
    print(i)

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
        print("Tylko dla c = 2")
        print(c)
    print("Przy każdym elemencie pętli")
# Przy każdym elemencie pętli
# Tylko dla c = 2
# 3
# Przy każdym elemencie pętli
# Przy każdym elemencie pętli
# Przy każdym elemencie pętli
# Przy każdym elemencie pętli

imiona = ['Radek', 'Tomek', 'Zenek', 'Ania']
print(imiona)  # ['Radek', 'Tomek', 'Zenek', 'Ania']
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Ania

# 0 Radek
for i in imiona:
    print(imiona.index(i), i)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

for i in range(len(imiona)):  # range(4) -> 0123
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania

# enumerate() - numeruje i zwraca elelmnt kolekcji z numerem
for p in enumerate(imiona):
    print(p)
# (0, 'Radek') -> 0 Radek
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Ania')
for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Ania
for i, o in enumerate(imiona, start=1):  # start=1 - numerujemy od 1
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Ania

ludzie = ['Radek', 'Tomek', 'Zenek', 'Magda']
wiek = [44, 55, 32, 29]
# wypisac to tak Radek 44
for i in ludzie:
    print(i, wiek[ludzie.index(i)])
# Radek 44
# Tomek 55
# Zenek 32
# Magda 29

ludzie = ['Radek', 'Tomek', 'Zenek', 'Magda', "Marek"]
wiek = [44, 55, 32, 29]
# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])  # IndexError: list index out of range

# zip() - łączy elementy kolekcji w pary
for i in zip(ludzie, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Magda', 29)
for l, w in zip(ludzie, wiek):
    print(l, w)
# Radek 44
# Tomek 55
# Zenek 32
# Magda 29

# 0 Radek 44
for i in enumerate(zip(ludzie, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 55))
# (2, ('Zenek', 32))
# (3, ('Magda', 29))
a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = ('Radek', 44)
print(a, c, d)  # 0 Radek 44
x, (y, z) = (0, ('Radek', 44))
print(x, y, z)  # 0 Radek 44
for i, (l, w) in enumerate(zip(ludzie, wiek)):
    print(i, l, w)
# 0 Radek 44
# 1 Tomek 55
# 2 Zenek 32
# 3 Magda 29
