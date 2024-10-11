from abc import ABC, abstractmethod


# klasa abstrakcyjna
class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc, "km/h")

    @abstractmethod  # dekorator oznaczający klasę abstrakcyjną
    def wydaj_odglos(self):
        pass


# dziedziczenie -
class Kura(Ptak):
    """
    Kura dziedziczy po klasie Ptak
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # musimy użyc konstruktor z klasy wyższej, super()

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko ko ko ko")

    def dziobanie(self):
        print("Idę sobie podziobać")


class Orzel(Ptak):
    """
    Orzel
    """

    def wydaj_odglos(self):
        print("Kir kier kier kir")

    def polowanie(self):
        print("Rozpoczynam polowanie")


class Sowa(Ptak):
    """
    Kalsa Sowa
    """


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł", 45)
# or1.latam()  # Tu Orzeł Lecę z szybkością 45
# kur1 = Ptak("Kura", 0)
# kur1.latam()
# Tu Orzeł Lecę z szybkością 45 km/h
# Tu Kura Lecę z szybkością 0 km/h
print("-----")
or2 = Orzel("Orzeł Bielik", 50)
or2.latam()
kur2 = Kura("Kura domowa")
kur2.latam()
# Tu Orzeł Bielik Lecę z szybkością 50 km/h
# Tu Kura domowa Ja nie latam

or2.wydaj_odglos()
kur2.wydaj_odglos()
# Kir kier kier kir
# Ko ko ko ko ko ko
or2.polowanie()
kur2.dziobanie()
# Rozpoczynam polowanie
# Idę sobie podziobać

# sowa = Sowa("Sowa", 20)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\pdnp-7-10-2024\day5\kl3.py", line 88, in <module>
#     sowa = Sowa("Sowa", 20)
#            ^^^^^^^^^^^^^^^^
# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'

# polimorfizm - obiekty różnych klas mają wspolne cechy i metody
lista = [or2, kur2]  # obiekty różnych klas
for i in lista:
    i.wydaj_odglos()
    i.latam()
# Kir kier kier kir
# Tu Orzeł Bielik Lecę z szybkością 50 km/h
# Ko ko ko ko ko ko
# Tu Kura domowa Ja nie latam
