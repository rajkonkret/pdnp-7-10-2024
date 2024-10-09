# while - petla sterowana warunkiem

# pętla nieskończona
# while True:
#     print("komunikat 1 !")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break  # przerwanie pętli

print(licznik)  # 11

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")

# password = input("Podaj hasło")
# while password != "secret":
#     password = input("Błedne hasło. Podaj ponownie")
# print("Hasło prawidłowe")

lista = []
lista_int = []
while True:
    #  A string is numeric if all characters in the string are numeric
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)
print(lista_int)
# ['1', '2', '3']
# [1, 2, 3]

# usunięcie wszystki elemntów z listy bez tracenia kolejności
my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
element_to_remove = 5
while element_to_remove in my_list:
    my_list.remove(element_to_remove)

print(my_list)  # [1, 2, 3, 4, 6]
