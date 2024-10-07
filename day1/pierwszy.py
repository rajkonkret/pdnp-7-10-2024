# PEP8 - zasady stylistyczne dla kodu
# komentarz
import sys

print()  # wydrukuj/wypisz
# ctrl alt l - formatowanie kodu wg zasad PEP8
print("Nazywam się Radek")
# Nazywam się Radek
# ctrl / - automatyczne komentowanie kodu
print('Nazywam się Radek')
# Nazywam się Radek
# Nazywam się Radek
# print('Radek")
#   File "C:\Users\CSComarch\PycharmProjects\pdnp-7-10-2024\day1\pierwszy.py", line 12
#     print('Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 12)
print("Nazywam się 'radek'")  # Nazywam się 'radek'
print("Nazywam się 'radek'")  # Nazywam się 'radek'
print("Nazywam się 'radek'")  # Nazywam się 'radek'
print("Nazywam się 'radek'")  # Nazywam się 'radek'
print("Nazywam się 'radek'")  # Nazywam się 'radek'
print("Nazywam się 'radek'")  # Nazywam się 'radek'
print("Nazywam się 'radek'")  # Nazywam się 'radek'
# ctrl d - powielanie linii
# Nazywam się 'radek'
# Nazywam się 'radek'
# Nazywam się 'radek'
# Nazywam się 'radek'
# Nazywam się 'radek'
# Nazywam się 'radek'
# Nazywam się 'radek'

# type() - sprawdzenie tupu
print("39")
print(type("39"))  # <class 'str'>, typ tekstowy, stringi

print(39)  # 39
print(type(39))  # <class 'int'>, liczby całkowite
print(39 + 39)  # 78
print("39" + "39")  # konkatenacja, łączenie tekstów 3939
# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str
# Process finished with exit code 1

# w pythonnie jawnie musimy zamieniac typy na odpowiednie do działania
print(int("39") + 39)  # int() - rzutowanie, zamiana na int (liczbę), wynik 78

print("Radek" + str(39))  # str() - rzutowanie, zamiana liczby na str (string, tekst)
# Radek39
print(5 * "4")  # 44444
print("160" * 35)
# 160160160160160160160160160160160160160160160160160160160160160160160160160160160160160160160160160160160

print(160 * 35)  # 5600

# zmienna - pudełko na dane
# przechowuje jeden element
# snake_case
# nazwa zmiennej powinna wskazywac co przechowuje
liczba = 39
print(liczba)  # weż zawartość zmiennej, 39

# typowanie dynamiczne
name = "Radek"
print(name)
print(type(name))
# Radek
# <class 'str'>
name = 90
print(name)  # 90
print(type(name))  # <class 'int'>

# to są tylko podpowiedzi
name: str = "Radek"
print(name)
name = 90
print(name)
# Radek
# 90

age = 38
print(age)
print(type(age))
# 38
# <class 'int'>
print(sys.int_info)
# sys.int_info(
#     bits_per_digit=30,
#     sizeof_digit=4,
#     default_max_str_digits=4300,
#     str_digits_check_threshold=640)
