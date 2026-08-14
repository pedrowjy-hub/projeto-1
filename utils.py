import sqlite3

def load_data():
    with sqlite3.connect('banco.db') as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute('''
            SELECT
            title AS titulo,
            content AS detalhes
            FROM note
        ''')

        return [dict(nota) for nota in cur.fetchall()]


def load_templates(arquivo):
    with open(f'static/templates/{arquivo}','r', encoding='utf-8') as arquivos:
        return arquivos.read()

def submit_note(nota):
    
    with sqlite3.connect('banco.db') as con:
        cur=con.cursor()
        cur.execute(
            'INSERT INTO note (title, content) VALUES (?,?)',
            (nota['titulo'],nota['detalhes'])
        )