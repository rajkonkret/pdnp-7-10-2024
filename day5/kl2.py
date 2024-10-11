class Human:
    """
    Klasa Human opisująca człowieka
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    # wypisz_wzrost, wypisz_wiek
    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu")

    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat")

    def ruszaj(self):
        if self.plec == "m":
            print("Ruszyłem w drogę")
        else:
            print("Ruszyłam w drogę")


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Radek", 56, 190, "m")
print(cz1)  # <__main__.Human object at 0x000001F91B8F5C40>
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.imie)
print(cz1.plec)

cz2 = Human("Tamara", 29, 170)
print(cz2.wiek)
print(cz2.wzrost)
print(cz2.imie)
print(cz2.plec)

cz1.powitanie()  # Nazywam się Radek
cz1.wypisz_wiek()
cz2.wypisz_wzrost()
# Nazywam się Radek
# Ma, 56 lat
# Mam 170 cm wzrostu

cz1.ruszaj()
cz2.ruszaj()
# Ruszyłem w drogę
# Ruszyłam w drogę
