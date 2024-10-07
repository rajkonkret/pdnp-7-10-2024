tekst = "Witaj Świecie"
print(tekst)  # Witaj Świecie
print(type(tekst))  # <class # 'str'>

# wszystko jest obiektem
# teksty są niemutowalne
tekst.upper()
""" Return a copy of the string converted to uppercase. """
print(tekst)  # Witaj Świecie
print(tekst.upper())  # WITAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WITAJ ŚWIECIE
print(tekst)  # Witaj Świecie - oryginał nie jest zmieniany

# zamienic na małe litery
tekst_lower = tekst.lower()
print(tekst_lower)
print(tekst.lower())
# witaj świecie
# witaj świecie

# Witaj Świecie
# 0123456789....
print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("j", 0, 4))  # indeksy 0123 -> literka "j" jest 0 razy
# Wita
# 0123

# duże małe litery mają znaczenie
print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

tekst_zamiana = "Witaj dobry Świecie"
# __old, __new - podpowiedzi z Pycharm, nie przepisujemy
print(tekst_zamiana.replace("dobry ", ""))  # Witaj  Świecie, Witaj Świecie

# strip() - usunie białe znaki(spacje końcowe i wiodące)
print(tekst.removesuffix("Świecie").strip())  # "Witaj"

print(tekst[4])  # indeks nr 4 -> "j"

encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie'
# \b dane typu bajtowego
# \xc5\x9a - \x zapis szesnatkowy liczby -> 197
print(type(encode_s))  # <class 'bytes'>
print(encode_s.decode('utf-8'))  # Witaj Świecie

imie = "Radek"
# f - fstring, string sforamtowany
tekst_format = f"Mam na imię {imie} i lubię pythona."
print(tekst_format)  # Mam na imię Radek i lubię pythona.
tekst_format = f"\tMam na imię {imie}\n i lubię pythona.\b"
print(tekst_format)
# "	    Mam na imię Radek
#  i lubię pythona"
# \t - tabulator
# \n - nowa linia
# \b - backspace

starszy = "Witaj %s!"  # %s - string
print(starszy % imie)  # Witaj Radek!
print("Witaj %s!" % imie)  # Witaj Radek!

print("Witaj {}".format(imie))  # Witaj Radek

print("Witaj", imie)  # Witaj Radek

print("""Tekst
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy"
