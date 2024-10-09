# działania z plikami
# context manager
# with - context manager w pythonie
# open() - praca z plikami
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
from typing import final

with open('test.log', 'w', encoding='utf-8') as fh:  # filehandler
    fh.write("Powitanie\n")
    fh.write("Drugie\n")
    fh.write("Kolejne\n")

# 'x' - sprawdza czy plik istnieje
# FileExistsError: [Errno 17] File exists: 'test.log'
# with open('test.log', 'x', encoding='utf-8')) as f:
#     f.write("Zapisz\n")

# 'w' - kasuje plik jessli istniał!
with open('test.log', 'w', encoding='utf-8') as file:
    file.write("Nadpisane\n")

# "a" - dopisanie do pliku
with open('test.log', 'a', encoding='utf-8') as f:
    f.write("Dopisane\n")
    f.write("Dopisane\n")
    f.write("Dodane\n")
    f.write("Dodane\n")
    f.write("Dośdane\n")

# "r" - odczytanie pliku
with open('test.log', 'r', encoding='utf-8') as f:
    lines = f.read()

print(lines)
