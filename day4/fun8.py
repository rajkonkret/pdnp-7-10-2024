# funkcje lambda
# skrócony zakres funkcji
# zwraca wynik
# lambda jako funkcja anonimowa
def odejmij(a, b):
    return a - b


print(odejmij(8, 23))  # -15

odejmij2 = lambda a, b: a - b
print(odejmij2(10, 6))  # 4

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły
