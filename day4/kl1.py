# klasa - element programowania obiektowego
# klasa - szablon, przepis
# wyznacza minimum cech jakie ma posiadać obiekt
# obiekt (instancja) jest zbudowany wg szablonu
# klasa musi byc najpierw zdefiniowana
# definicja nie uruchamia klasy
# budowanie obiektu uruchaamia metod e inicjalizującą
# po stworzeniu obiektu możemy na nim wykonywac metody zdefiniowane w klasie
# # paradygmaty programowania obiektowego
# hermetyzacja, dziedziczenie, polimorfizm, abstrakcja
# pola (zmienne - przechowują stan obiektu)
# metody (funkcje)


# deklaracja klasy
# PEP8 zaleca by nazwy klas były z dużej litery
# komentarz jest traktowany jako dokumentacja
class Human:
    """
    Klasa Human w Pythonie
    """

    imie = ""
    wiek = None
    plec = "k"


# tworzenie obiektu klasy Human
cz1 = Human()
print(cz1)  # <__main__.Human object at 0x0000019B74C8D730>
print(Human.__doc__)  # Klasa Human w Pythonie
print(print.__doc__)
# cd day4 przejscie do katalogu day4
# pydoc -b - uruchomienie serwera z dokumentacją
# pydoc -w kl1  - stworzenie pliku z dokumentacją dla pliku kl1.py
print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)
# k
# None
cz1.wiek = 29
cz1.imie = "Anna"
print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)
# k
# 29
# Anna
cz2 = Human()
cz2.imie = "Radek"
cz2.plec = "m"
cz2.wiek = 45
print(cz2.plec)
print(cz2.wiek)
print(cz2.imie)
# m
# 45
# Radek
