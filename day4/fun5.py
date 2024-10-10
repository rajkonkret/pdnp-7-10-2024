# stworzyc funkcję kantor
# funkcja ma zawierac dwie funkcje wewnętrzne eur, usd
# w zależnosci od parametru ma zwrócic jedną z tych funkcji
# możliwośc przekazania dowolnej kwoty do funkcji wewnętzrnych
# ładnie wypisac
def kantor(waluta):
    def eur(kwota=0):
        print(f"wymieniam {kwota} eur na {kwota * 4.31:.2f} pln.")

    def usd(kwota=0):
        print(f"wymieniam {kwota} usd na {kwota * 3.98:.2f} pln.")

    if waluta == "eur":
        return eur  # zwracamy adres funkcji
    elif waluta == 'usd':
        return usd
    else:
        return None


kantor_usd = kantor('usd')
if kantor_usd:
    kantor_usd(1000)

kantor_eur = kantor('eur')
if kantor_eur:
    kantor_eur(5000)

# wymieniam 1000 usd na 3980.00 pln.
# wymieniam 5000 eur na 21550.00 pln.
