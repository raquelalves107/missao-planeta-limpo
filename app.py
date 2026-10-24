
from flask import Flask, render_template, request, jsonify
import joblib
import random

app = Flask(__name__)

# Carregar a inteligência artificial já treinada
modelo = joblib.load("modelo_ia.joblib")

# Desafios do jogo
desafios = [
    {"imagem": "01_plantar_arvore.png", "frase": "Plantar uma árvore.", "correta": "PRESERVA"},
    {"imagem": "02_separar_reciclaveis.png", "frase": "Separar materiais recicláveis.", "correta": "PRESERVA"},
    {"imagem": "03_recolher_lixo_parque.png", "frase": "Recolher lixo do parque.", "correta": "PRESERVA"},
    {"imagem": "04_apagar_luzes.png", "frase": "Apagar as luzes ao sair da sala.", "correta": "PRESERVA"},
    {"imagem": "05_cuidar_animais.png", "frase": "Cuidar dos animais.", "correta": "PRESERVA"},
    {"imagem": "06_jogar_lixo_rio.png", "frase": "Jogar lixo no rio.", "correta": "PREJUDICA"},
    {"imagem": "07_torneira_aberta.png", "frase": "Deixar a torneira aberta.", "correta": "PREJUDICA"},
    {"imagem": "08_desperdicar_papel.png", "frase": "Desperdiçar papel.", "correta": "PREJUDICA"},
    {"imagem": "09_queimar_lixo.png", "frase": "Queimar lixo.", "correta": "PREJUDICA"},
    {"imagem": "10_destruir_plantas.png", "frase": "Destruir plantas do jardim.", "correta": "PREJUDICA"}
]

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/desafios")
def listar_desafios():
    lista = desafios.copy()
    random.shuffle(lista)
    return jsonify([
        {"imagem": d["imagem"], "frase": d["frase"]}
        for d in lista
    ])

@app.route("/responder", methods=["POST"])
def responder():
    dados = request.get_json()
    frase = dados.get("frase", "")
    escolha = dados.get("escolha", "")

    desafio = next((d for d in desafios if d["frase"] == frase), None)

    if desafio is None or escolha not in ["PRESERVA", "PREJUDICA"]:
        return jsonify({"erro": "Resposta inválida"}), 400

    previsao_ia = modelo.predict([frase])[0]
    correta = desafio["correta"]

    return jsonify({
        "acertou": escolha == correta,
        "resposta_correta": correta,
        "classificacao_ia": previsao_ia
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
