from utils import load_data, load_templates, submit_note

def index():
    note_template = load_templates('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_templates('index.html').format(notes=notes)

def submit(titulo, detalhes):
    nota={'titulo':titulo, 'detalhes':detalhes}
    submit_note(nota)

    return 

