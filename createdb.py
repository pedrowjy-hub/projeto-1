import sqlite3
import json

con = sqlite3.connect('banco.db')
cur = con.cursor()
cur.execute('''
    CREATE TABLE note(
    id INTEGER PRIMARY KEY,
    title TEXT,
    content TEXT,
    favorite BOOLEAN NOT NULL DEFAULT FALSE)
''')

with open('notes.json','r', enconding = 'utf-8') as arquivo:
    notas = json.load(arquivo)

    cur.executemany(
        'INSERT INTO note (title, content), (?,?)',
        [(nota['titulo'],nota['detalhes']) for nota in notas]
    )

con.commit()
con.close()
