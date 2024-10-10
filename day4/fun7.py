dictionary = {}


def connect(**opcje):  # ** dowolna ilosc argumentów po nazwie
    global dictionary
    print(opcje)
    print(type(opcje))  # <class 'dict'>
    dictionary = opcje


connect(a=10)
connect(a=10, b=100, name="Radek", start=1)  # {'a': 10, 'b': 100, 'name': 'Radek', 'start': 1}
print(dictionary)  # {'a': 10, 'b': 100, 'name': 'Radek', 'start': 1}


def all_params(*args, **kwargs):
    print(args, kwargs)


all_params(1, 2, 3, 4)
all_params(1, 2, 3, 4, a=90, b=90, name="Radek")
all_params(name="Radek", start=1)
# (1, 2, 3, 4) {}
# (1, 2, 3, 4) {'a': 90, 'b': 90, 'name': 'Radek'}
# () {'name': 'Radek', 'start': 1}
