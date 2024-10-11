# sqlite
import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza została podłączona")
except sqlite3.Error as e:
    print("Bład bazy", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")

# Baza została podłączona
# Połaczenie zostało zamknięte
