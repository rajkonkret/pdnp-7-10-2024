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
