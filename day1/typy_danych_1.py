import sys

wiek = 47
rok = 2024
temp = 36.6

print(temp)
print(type(temp))  # <class 'float'>

print(wiek * rok)  # 95128
print(wiek - rok)  # -1977
print(wiek + rok)  # 2071
print(wiek / rok)  # 0.023221343873517788 -> float
print(rok // wiek)  # 43, częśc całkowita  z dzielenia
print(rok % wiek)  # 3, reszta z dzielenia (modulo)
print(10 % 3)  # 3 całe i reszty 1

print(wiek ** rok)  # potęgowanie

# len() - długość zbioru
print(len(str(wiek ** rok)))  # długosć 3385
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit
# print(len(str(wiek ** rok ** 2)))

print(54 - 5 * 43 + 8 / 2 + 8 / 2)  # -153.0
print(54 - 5 * 43 + (8 / 2 + 8) / 2)  # -155.0

# Przy liczbach float mamy bład zaokrąglenia
print(0.2 + 0.8)  # 1.0 -> float
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
# For example, in a floating-point arithmetic with five base-ten digits of precision,
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# decimal
print(sys.float_info)
# sys.float_info(
#     max=1.7976931348623157e+308
#     , max_exp=1024, max_10_exp=308,
#     min=2.2250738585072014e-308,
#     min_exp=-1021, min_10_exp=-307,
#     dig=15, mant_dig=53,
#     epsilon=2.220446049250313e-16,
#     radix=2, rounds=1)

print(f"Sprawdzenie zmiennej {temp} {wiek}")

print(f"""
{wiek}
    {temp}""")
# Sprawdzenie zmiennej 36.6 47
# "47
#     36.6"

# typ logiczny
# prawda fałsz
# True False -  z dużej litery
# 1 - prawda, 0 - fałsz

czy_znasz_pythona = False
print(czy_znasz_pythona)  # False
print(type(czy_znasz_pythona))  # <class 'bool'>, typ logiczny

print(int(True))  # 1
print(int(False))  # 0

print(bool(1))  # bool() rzutowanie na typ logiczny, True
print(bool(100))  # True
print(bool(-10))  # True
print(bool("radek"))  # True

print(bool(0))  # False
print(bool(""))  # False
print(bool(None))  # False, None - nic, stan nieokreslony, odpowiednik null w innych systemach

print(bool(" "))  # True
print(bool())  # False

# działąnia logiczne
# and -> i
# Expression    Evaluates to
# True and True    True
# True and False    False
# False and True    False
# False and False    False
# The or Operator’s Truth Table:
#
print(False and True)  # False
print(False and False)  # False

# or -> lub
# Expression    Evaluates to
# True or True    True
# True or False    True
# False or True    True
# False or False    False
# The not Operator’s Truth Table:
#

print(False or True)  # True
print(False or False)  # False

# negacja
# Expression    Evaluates to
# not True    False
# not False   True
print(not True)  # False

a = 8
b = 6
# wyniki porównań zwracją bool (typ logiczny)
print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 8 > 6 = True
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 8 < 6 = False
print(f"Porównanie {a <= b = }")  # Porównanie a <= b = False
print(f"Porównanie {a >= b = }")  # Porównanie a >= b = True
print(f"Porównanie {a} == {b} = {a == b}")  # czy a równa się b Porównanie 8 == 6 = False
print(f"Porównanie {a} != {b} = {a != b}")  # Porównanie 8 != 6 = True, czy różne
