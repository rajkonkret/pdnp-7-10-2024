# wyjątki
# błedy podczas wykonywania programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp-7-10-2024\day3\wyjatki.py", line 4, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
print(6 / 9)  # 0.6666666666666666

try:
    # print(5 / 0)
    # print("A" + 9)
    # print(int("A"))
    raise KeyError("Bład klucza")  # rzucamy wyjątek jawnie
    wynik = 90 / 34
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Bład typu")
except ValueError:
    print("Bład wartości")
except Exception as e:  # przechwytuje pozostałe wyjątki, e przechwytuje komunikat błedu
    print("Błąd", e)
else:  # gdy nie ma błedu
    print("Wynik", wynik)
finally:
    print("Zakończyłem obliczenia")

print("Program nadal działa")
# try except [else finally]

# Nie dziel przez zero
# Program nadal działa
# Bład typu
# Program nadal działa
# Bład wartości
# Program nadal działa
# Błąd 'Bład klucza'
# Program nadal działa
# Wynik 2.6470588235294117
# Program nadal działa
# Wynik 2.6470588235294117
# Zakończyłem obliczenia
# Program nadal działa
# Bład wartości
# Zakończyłem obliczenia
# Program nadal działa
# 0.6666666666666666
# Błąd 'Bład klucza'
# Zakończyłem obliczenia
# Program nadal działa
