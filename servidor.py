from flask import Flask, render_template_string, request, redirect
import views

app = Flask(__name__)

app.static_folder = 'static'

@app.route('/')
def index():

    
    return render_template_string(views.index())

@app.errorhandler(404)
def page_not_found(erro):
    return 'Página ou recurso não encontrado', 404

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_form():
    id_nota = request.form.get('id')

    views.delete(id_nota)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
