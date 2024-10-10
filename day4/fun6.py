# stworzyć funkcję obliczającą średnią

def srednia(name=None, *cyfry):  # * - dowolna liczba argumentów pozycyjnych
    print(cyfry)  # (1, 2, 3, 4, 5) krotka
    count = len(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
    except Exception as e:
        print("Błąd", e)
    else:
        print(f"Średnia dla ucznia {name}, wynosi {avg}")
    finally:
        print("Kolejny uczeń")


srednia()
srednia(1, 2, 3, 4, 5)
# ()
# Błąd division by zero
# (1, 2, 3, 4, 5)
# Średnia wynosi 3.0
# ()
# Błąd division by zero
# Kolejny uczeń
# (1, 2, 3, 4, 5)
# Średnia wynosi 3.0
# Kolejny uczeń
srednia("Radek", 4, 5, 6, 5, 5, 4)
# # ("Radek", 4, 5, 6, 5, 5, 4) -> name, oceny
# name, *cyfry = ("Radek", 4, 5, 6, 5, 5, 4)
# ()
# Błąd division by zero
# Kolejny uczeń
# (2, 3, 4, 5)
# Średnia dla ucznia 1, wynosi 3.5
# Kolejny uczeń
# (4, 5, 6, 5, 5, 4)
# Średnia dla ucznia Radek, wynosi 4.833333333333333
# Kolejny uczeń
