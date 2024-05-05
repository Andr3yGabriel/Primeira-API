from flask import Flask, make_response, jsonify, request
from bd import Familia


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/Familia', methods=['GET'])
def get_familia():
    return make_response( 
        jsonify(
            "Arvore Genealógica",
            Familia
        )
    )


@app.route('/Familia', methods=['POST'])
def aumentar_familia():
    familiar = request.json
    Familia.append(familiar)
    return make_response(
        jsonify(
            "Novo familiar adicionado",
            familiar
        )
    )


app.run()
