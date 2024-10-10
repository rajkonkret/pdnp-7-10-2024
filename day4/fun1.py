# funkcje - możliwość wykonania kodu w dowolnym momencie
# funkcja musi byc najpierw zadeklarowana
# w miejscu deklaracji funkcja sie  nie wykonuje
# żeby uruchomić funkcję należy ją wywołac


# funkce niezwracające wyniku
a = 6
b = 8


# deklaracja funkcji
# funkcja bez argumentów
# PEP8 sugeruje aby definicja funkcji była oddzielona od reszty programu dwoma pustymi liniami
def dodaj():
    print(a + b)


def dodaj2(a, b):  # funkcja posiada dwa obowiązkowe argumenty
    print(a + b)


def odejmij(a, b, c=0):  # argument c ma wartość domyślną
    print(a - b - c)


# wywołanie funkcji
# nazwa i nawiasy ()
dodaj()  # 14
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(10, 76)  # 86

# przekazywanie argumentów po pozycji
odejmij(1, 2)  # -1, c=0
odejmij(1, 2, 8)  # -9, c=8

# przekazywanie argumentów po nazwie
odejmij(b=9, c=10, a=90)  # 71
odejmij(b=90, a=10)  # -80

# mieszany
odejmij(1, c=90, b=87)  # -176

# argumenty pozycyjne muszą być przed nazwanymi
# odejmij(a=10, 4, 5) # SyntaxError: positional argument follows keyword argument
# Tabnine, Copilot, AI Assistance Pycharm - sztuczna inteligacja do wspomagania pisania kodu

print(dodaj())  # wypisz wynik dziłania funkcji
# 14
# None

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# print(dodaj() + dodaj2(7, 89))
