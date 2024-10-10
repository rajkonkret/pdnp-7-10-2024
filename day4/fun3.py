a = 10  # globalne
b = 10


def dodaj():
    a = 7  # zasięg lokalny, nie wpływa na globalną zmienną
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # używa globalnych zmiennych


def dodaj3():
    global a  # użyj globalnego a
    a = 9  # wpływa na globalne a
    b = 89  # zmienna lokalna
    print(a + b)


print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=10 (globalna)
dodaj()  # 15
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=10 (globalna)
dodaj2()  # 20
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=10 (globalna)
dodaj3()  # 98
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=9 (globalna)
# shift alt strzalka w dól - przesunięcie linijki w dół
dodaj2()  # 19
print(f"Wartość a z góry {a=} (globalna)")  # Wartość a z góry a=9 (globalna)
