import shutil
from pathlib import Path

base_path = Path('ops_example')
base_path_2 = Path('ops_example/D')

# usunięcie katalogu jeśli istnieje
if base_path.exists() and base_path.is_dir():
    shutil.rmtree(base_path)

# utworzenie katalogu
base_path.mkdir()
path_b = base_path / 'A' / 'B'
path_c = base_path / 'A' / 'C'
path_d = base_path / 'A' / 'D'

# path_b.mkdir() # FileNotFoundError: [WinError 3] System nie może odnaleźć określonej ścieżki: 'ops_example\\A\\B'
# parents = True - tworzy pośrednie katalogi
path_b.mkdir(parents=True)
path_c.mkdir()  # bo juz istnieje pośredni katalog "A"

for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, 'w') as stream:
        stream.write(f"Jakaś treść pliku {filename}")

# move - przenosi pliki z katalogu B do katalogu D
# usuneło katalog B
shutil.move(path_b, path_d)
# ściezka do pliku ex1.txt
ex1 = path_d / 'ex1.txt'
# zmiana nazwy dla tego pliku
ex1.rename(ex1.parent / 'ex1_renamed.log')

file_name = 'ex2.txt'
file_path = Path(file_name).resolve()
print(file_path.parent)  # C:\Users\CSComarch\PycharmProjects\pdnp-7-10-2024\day4
print(file_path)  # C:\Users\CSComarch\PycharmProjects\pdnp-7-10-2024\day4\ex2.txt
# C:\Users\CSComarch\PycharmProjects\pdnp-7-10-2024\day4\ops_example\A\D
