user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001
print(type(wersja))  # <class 'float'>, zmiennoprzecinkowe
liczba = 456123789567  # int
print(type(liczba))  # <class 'int'>

print("Witaj %s, masz teraz %d lat." % (user, wiek))
# %s - string
# %d liczba

# ten sposób sprawdza typy
# print("Witaj %d, masz teraz %s lat." % (user, wiek))
#           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
# TypeError: %d format: a real number is required, not str
print("Witaj %(user)s, Lubię Cię %(user)s" % {"user": user})
# Witaj Tomek, Lubię Cię Tomek

print("Witaj {}, masz teraz {} lat.".format(user, wiek))  # Witaj Tomek, masz teraz 39 lat.

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
# f - fstring, tekst sformatowany

print("Uzywamy wersji Pythona %i" % 3)  # Uzywamy wersji Pythona 3
print("Uzywamy wersji Pythona %f" % 3)  # Uzywamy wersji Pythona 3.000000
print("Uzywamy wersji Pythona %f" % 3.9)  # Uzywamy wersji Pythona 3.900000
print("Uzywamy wersji Pythona %.2f" % 3.9)  # Uzywamy wersji Pythona 3.90
print("Uzywamy wersji Pythona %.1f" % 3.9)  # Uzywamy wersji Pythona 3.9
print("Uzywamy wersji Pythona %.0f" % 3.9)  # Uzywamy wersji Pythona 4 - zaokrągli
print("Uzywamy wersji Pythona %.f" % 3.9)  # Uzywamy wersji Pythona 4
print("Uzywamy wersji Pythona %.f" % 3.9 * 2)  # Uzywamy wersji Pythona 4Uzywamy wersji Pythona 4
print("Uzywamy wersji Pythona %.f" % (3.9 * 2))  # Uzywamy wersji Pythona 8
# zaokrągla przy wyświetlaniu
print("Wynik = %.2f" % 3.876)  # Wynik = 3.88
x = 3.14
print("Zero miejsc po przecinku %.f" % x)
print("X nadal się nie zmienia", x)
# Zero miejsc po przecinku 3
# X nadal się nie zmienia 3.14

y = round(x)
print("x=", x, "y=", y)  # x= 3.14 y= 3
print(f"{x=}, {y=}")  # x= 3.14 y= 3
x = 3.1416
print(round(x, 2))  # 3.14

print(f"Uzywamy wersji python {wersja}")  # Uzywamy wersji python 3.900001
print(f"Uzywamy wersji python {wersja:.1f}")  # Uzywamy wersji python 3.9
print(f"Uzywamy wersji python {wersja:.2f}")  # Uzywamy wersji python 3.90
print(f"Uzywamy wersji python {wersja:.0f}")  # Uzywamy wersji python 4
# print(f"Uzywamy wersji python {wersja:.f}")  # ValueError: Format specifier missing precision

print(f"{user:>10}")  # "     Tomek"
print(f"{user:<15}")  # "Tomek          "
print(f"{user:^20}")  # "       Tomek        "

print(liczba)  # 456123789567
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 456,123,789,567
print(f"Nasza duża liczba {liczba:_}")  # Nasza duża liczba 456_123_789_567
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))  # Nasza duża liczba 456.123.789.567
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))  # Nasza duża liczba 456 123 789 567

# 1500000000000
liczba_2 = 1_500_000_000_000
print(type(liczba_2))  # <class 'int'>
print(liczba_2)  # 1500000000000
