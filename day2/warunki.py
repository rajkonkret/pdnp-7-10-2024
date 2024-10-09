# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# w zależności od warunek (True False) wykona jedną lub drugą częśc programu (blok)
# warunek musi zwrócić typ bool
# if
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

punkty = 0
odp = input("Podaj rok Chrztu Polski")  # str
if odp == '966':
    print("Brawo")
    punkty += 1  # punkty = punkty + 1
else:
    print("Musisz się uczyć dalej")

print("Punkty", punkty)
# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
