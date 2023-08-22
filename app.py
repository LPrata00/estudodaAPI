from flask import Flask, jsonify, request, Response, make_response
import psycopg2

app = Flask(__name__)

usuarios = [
    {
        'cpf': 76342,
        'nome': 'Luan',
        'data nascimento': '17/04/2000'
    },

    {
        'cpf': 12854,
        'nome': 'Mario',
        'data nascimento': '07/08/2001'
    },

    {
        'cpf': 76452,
        'nome': 'Victoria',
        'data nascimento': '29/09/2000'
    }
]

@app.route('/usuarios', methods = ['GET'])
def obter_usuarios():
    return make_response(jsonify(usuarios))


@app.route('/usuarios', methods = ['POST'])
def incluir_usuario():
    novo_usuairo = request.get_json()
    usuarios.append(novo_usuairo)

    return make_response(jsonify(usuarios))

app.run(port = 5000, host = 'localhost', debug= True)