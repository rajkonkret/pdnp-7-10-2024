dictionary = {'imie': "Radek", 'nazwisko': 'Kowalski'}
print(type(dictionary))  # <class 'dict'>

# wyswietlenie klucze
for i in dictionary:
    print(i)
# imie
# nazwisko

for k in dictionary.keys():
    print(k)
# imie
# nazwisko

# wyswietlenie wrtości
for v in dictionary.values():
    print(v)
# Radek
# Kowalski

# wyswietlenie par
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
#  sep
#         string inserted between values, default a space.
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski
print("Radek", end="")
print("Tomek")  # RadekTomek, end="\n"
print("Aneta")
# RadekTomek
# Aneta

pol_ang = {'kot': 'cat', 'pies': 'dog', 'dach': 'roof'}
ang_pol = {}

for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)  # {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}

print({value: key for key, value in pol_ang.items()})
# {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}
