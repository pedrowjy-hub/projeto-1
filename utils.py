import json

def load_data(arquivo):
    with open(f'static/data/{arquivo}', 'r', encoding='utf-8') as arquivos:
        return json.load(arquivos)

def load_templates(arquivo):
    with open(f'static/templates/{arquivo}','r', encoding='utf-8') as arquivos:
        return arquivos.read()

def submit_note(arquivo, nota):
    notas = load_data(arquivo) 
    notas.append(nota)

    with open(f'static/data/{arquivo}', 'w', encoding='utf-8') as arquivos:
        json.dump(notas, arquivos,indent=4)
