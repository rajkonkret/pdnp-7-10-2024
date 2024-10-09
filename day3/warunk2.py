# od Pythona 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.lower().strip():
    case "python":
        lista.append("Znam Pythona")
    case "java":
        lista.append("Znam Jave")
    case _:
        print("nie znam takiego języka")

print(lista)
