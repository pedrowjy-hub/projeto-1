from utils import load_data, load_templates, submit_note, delete_note, load_note, save_note

def index():
    note_template = load_templates('components/note.html')
    notes_li = [
        note_template.format(id=dados['id'],title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_templates('index.html').format(notes=notes)

def submit(titulo, detalhes):
    nota={'titulo':titulo, 'detalhes':detalhes}
    submit_note(nota)

    return 

def delete(id_nota):

    delete_note(id_nota)
    return 

def edit(id_nota):
    nota = load_note(id_nota)

    return load_templates('edit.html').format(id=nota.id,titulo=nota.title,detalhes=nota.content)

def save(id_nota,title,content):
    save_note(title,content,id_nota)
    return 