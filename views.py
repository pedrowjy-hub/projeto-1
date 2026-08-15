from utils import load_data, load_templates, submit_note, delete_note

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