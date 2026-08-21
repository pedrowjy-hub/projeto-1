import sqlite3

class Note:
    def __init__(self,id,title,content):
        self.id = id
        self.title = title
        self.content = content


def load_data():
    with sqlite3.connect('banco.db') as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute('''
            SELECT
            id,
            title AS titulo,
            content AS detalhes,
            favorite
            FROM note
            ORDER BY favorite DESC
        ''')

        return [dict(nota) for nota in cur.fetchall()]


def load_templates(arquivo):
    with open(f'static/templates/{arquivo}','r', encoding='utf-8') as arquivos:
        return arquivos.read()

def submit_note(nota):
    
    with sqlite3.connect('banco.db') as con:
        cur = con.cursor()
        cur.execute(
            'INSERT INTO note (title, content) VALUES (?,?)',
            (nota['titulo'],nota['detalhes'])
        )

def delete_note(note_id):

    with sqlite3.connect('banco.db') as con:
        cur = con.cursor()
        cur.execute(
            'DELETE FROM note WHERE id = ?',
            (note_id,)
        )

def load_note(note_id):
    with sqlite3.connect('banco.db') as con:
        con.row_factory = sqlite3.Row
        cur=con.cursor()
        cur.execute(
            'SELECT id,title,content FROM note WHERE id = ?',
            (note_id,)
        )
        nota = cur.fetchone()
        return Note(nota['id'],nota['title'],nota['content'])

def save_note(title,content,note_id):

    with sqlite3.connect('banco.db') as con:
        cur = con.cursor()
        cur.execute(
            'UPDATE note SET title = ?, content = ? WHERE id =?',
            (title,content,note_id)
        )

def favorite_note(note_id):

    with sqlite3.connect('banco.db') as con:
        cur = con.cursor()
        cur.execute(
            'UPDATE note SET favorite = NOT FAVORITE WHERE id=?',
            (note_id,)
        )
