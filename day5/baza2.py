# sqlite
import sqlite3

try:
    # conn = sqlite3.connect('baza_danych.db')
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    print("Baza została podłączona")

    query = '''
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary REAL NOT NULL);
    '''
    # REAL - -> float

    c.execute(query)
    conn.commit()

    insert = """
    INSERT INTO developers (id,name,salary) VALUES (1,'Radek','10000');
    """
    c.execute(insert)
    conn.commit()

    select = """
    SELECT * FROM developers;
    """
    for row in c.execute(select):
        print(row)  # (1, 'Radek', 10000.0)

except sqlite3.Error as e:
    print("Bład bazy", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")

# Baza została podłączona
# Połaczenie zostało zamknięte
# Baza została podłączona
# (1, 'Radek', 10000.0)
# Połaczenie zostało zamknięte
