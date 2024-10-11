class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        # hermetyzacja
        # ustawienie pola jako prywatne
        # mozna odczytac tylko wewnatrz klasy
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Jadę z szybkością {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10  # predkosc = predkosc - 10
        self.__zmien_bieg()

    # metoda prywatna
    def __zmien_bieg(self):
        print("zmiana biegu")


car = Car("Syrenka", 1980)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# po oznaczeniu pola jako prywatne
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
# print(car.__predkosc)  # 50
car.licznik()  # Jadę z szybkością 50 km/h
# car.__predkosc = 0
# enkapsulacja - hermetyzowanie pół i wystawianie odpowiednich metod do odczytu i zapisu
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()
# # Jadę z szybkością 0 km/h
# Jadę z szybkością 50 km/h
# zmiana biegu
# zmiana biegu
# zmiana biegu
# zmiana biegu
# zmiana biegu
# Jadę z szybkością 0 km/h
