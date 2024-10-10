# funkcje zwracające wynik
#  kończy sie słówkime return (zwróć)
# gdy napotka na return wychodzi z funkcji

def dodaj(a, b):
    return a + b


def odejmij(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(6, 89))  # 95
wynik = dodaj(89, 67)
print("Wynik:", wynik)
# Wynik: 156

print(odejmij())  # 0
print(odejmij(1))  # 1
print(odejmij(11, 2))  # 9
print(odejmij(11, 21, 23))  # -33
print(odejmij(b=10, a=9))  # -1
print(odejmij(b=90))  # -90
print(odejmij(1, c=90))  # -89
# print(odejmij(a=90, 1))  # SyntaxError: positional argument follows keyword argument

print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))
print(oblicz_vat(vat=15, cena=1000))

# 1230.0
# 1080.0
# 1150.0

zm = oblicz_vat(1000)
if zm == 1230:
    print("Ok")  # Ok

print(oblicz_vat(1000) + dodaj(90, 78))  # 1398.0
