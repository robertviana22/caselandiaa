from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    nome = request.form['nome']
    telefone = request.form['telefone']

    with open('dados.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([nome, telefone])

    return "Cadastro realizado com sucesso! ✅"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
