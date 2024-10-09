# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# w zależności od warunek (True False) wykona jedną lub drugą częśc programu (blok)
# warunek musi zwrócić typ bool
# if
from day2.typy_danych_2_lista import lista

odp = True
print(bool(odp))  # True
odp = False
if odp:
    # blok wykonywany po if gdy warunek spełniony
    # wcięcie 4 spacje
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
# True
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
print("Dalsza częśc programu")

odp = "Radek"
print(bool(odp))  # True
if odp:
    print("Radek")  # Radek

if odp == "Radek":
    print("Nadal Radek")  # Nadal Radek

if odp == "Tomek":
    print("To jest Tomek")
else:  # w przeciwym przypadku, zachowanie domyślne
    print("To nie jest Tomek")

# Nadal Radek
# To nie jest Tomek

# napisac aplikację test z...
# zadać pytanie
# pobrać odpowiedź od użytkownika
# w zależności od odowiedzi wypisać wynik pozytywny/negatywny
# fuzz buzz

# punkty = 0
# odp = input("Podaj rok Chrztu Polski")  # str
# if odp == '966':
#     print("Brawo")
#     punkty += 1  # punkty = punkty + 1
# else:
#     print("Musisz się uczyć dalej")
#
# print("Punkty", punkty)
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi {rabacik}")  # Rabat wynosi 25

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# if zarobki < 10000:
#     podatek = 0
# elif zarobki < 40000:
#     podatek = 0.2
# elif zarobki < 100000:  # od 10000 do 99999
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# print(f"Podatek wynosi {podatek * zarobki}")
# dodac podatek 0.2 dla przedziału 10000 do 39999

# zasymulujemy system zbierania logów
# zmienne będą przechowywac dane
# email, console, inny
# dla console: "Stało się coś strasznego"
# email: "System email"
# jesli log będzie z systemu email to:
# dopisz do listy błedów opis tego błedu
# error, medium, inny
#
lista_b = []
system_alert = "email"
error = "error"

if system_alert == "console":
    print("Stało się coś strasznego")
elif system_alert == 'email':
    print("System email")
    if error == "error":
        lista_b.append("Bład Krytyczny")
    elif error == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("Inny")
else:
    print("Nie znam takiego systemu")

print(lista_b)
