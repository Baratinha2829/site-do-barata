from flask import Flask, render_template, redirect

app = Flask(__name__)

# Lista de cursos direto no código
cursos = [
    {
        "id": 1,
        "nome": "Como criar sites com HTML e CSS",
        "link": "https://kirvano.com.br/cursos/html-css"
    },
    {
        "id": 2,
        "nome": "Curso de Python para Iniciantes",
        "link": "https://kirvano.com.br/cursos/python-iniciante"
    },
    {
        "id": 3,
        "nome": "Curso de Design no Canva",
        "link": "https://kirvano.com.br/cursos/design-canva"
    }
]

@app.route('/')
def index():
    return render_template('index.html', cursos=cursos)

@app.route('/curso/<int:curso_id>')
def acessar_curso(curso_id):
    curso = next((c for c in cursos if c['id'] == curso_id), None)
    if curso:
        return redirect(curso['link'])
    return "Curso não encontrado", 404

if __name__ == '__main__':
    app.run(debug=True, port=5050, host="0.0.0.0")
