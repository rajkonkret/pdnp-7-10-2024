# pętle - daje daje nam mozliwosc wykonania tego samego kodu wielokrotnie
# for - pętla iteracyjna
import random

# służy do działanai na liczbach losowych

for i in range(5):  # 0..4
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(5):  # _ - niema zmienna
    print("To jest pętla")
    # print(_)

for i in range(20):
    print(i * 2)

print("------")
"""Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100))  # int od 1 do 100
print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(5))  # int od 0 do 4
print(random.random())  # 0.9433044189145435, float, od 0 do 0.9999999
print(random.random() * 8)  # 4.402304243598092, od 0 do 7.9999999
