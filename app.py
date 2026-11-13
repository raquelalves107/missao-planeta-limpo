
from flask import Flask, render_template, request, jsonify
import joblib
import random

app = Flask(__name__)

# Carregar a inteligência artificial já treinada
modelo = joblib.load("modelo_ia.joblib")

# Desafios do jogo
desafios = [
    {"imagem": "11_separar_lixo.png", "frase": "Separar o lixo para reciclagem.", "correta": "PRESERVA"},
    {"imagem": "12_economizar_energia.png", "frase": "Economizar energia, apagando as luzes.", "correta": "PRESERVA"},
    {"imagem": "13_plantar_cuidar_arvores.png", "frase": "Plantar e cuidar das árvores.", "correta": "PRESERVA"},
    {"imagem": "14_garrafa_reutilizavel.png", "frase": "Usar garrafa reutilizável.", "correta": "PRESERVA"},
    {"imagem": "15_uso_consciente_agua.png", "frase": "Usar a água de forma consciente, sem desperdício.", "correta": "PRESERVA"},

    {"imagem": "16_jogar_lixo_chao.png", "frase": "Jogar lixo no chão.", "correta": "PREJUDICA"},
    {"imagem": "17_torneira_aberta.png", "frase": "Deixar a torneira aberta sem necessidade.", "correta": "PREJUDICA"},
    {"imagem": "18_queimar_lixo.png", "frase": "Queimar lixo, poluindo o ar.", "correta": "PREJUDICA"},
    {"imagem": "19_destruir_arvores.png", "frase": "Derrubar ou destruir as árvores.", "correta": "PREJUDICA"},
    {"imagem": "20_lavar_carro_mangueira.png", "frase": "Desperdiçar muita água lavando o carro com mangueira.", "correta": "PREJUDICA"},

    {"imagem": "21_cultivar_horta.png", "frase": "Cultivar uma horta na escola ou em casa.", "correta": "PRESERVA"},
    {"imagem": "22_usar_lampadas_led.png", "frase": "Usar lâmpadas LED, que gastam menos energia.", "correta": "PRESERVA"},
    {"imagem": "23_reciclar_materiais.png", "frase": "Reciclar materiais como plástico, papel, metal e vidro.", "correta": "PRESERVA"},
    {"imagem": "24_captar_agua_chuva.png", "frase": "Captar a água da chuva para reutilizar.", "correta": "PRESERVA"},
    {"imagem": "25_recuperar_areas_verdes.png", "frase": "Recuperar áreas verdes e plantar novas mudas.", "correta": "PRESERVA"},

    {"imagem": "26_usar_agrotoxicos_excesso.png", "frase": "Usar produtos químicos em excesso, como agrotóxicos.", "correta": "PREJUDICA"},
    {"imagem": "27_descartar_lixo_bueiro.png", "frase": "Descartar lixo nos rios, bueiros ou nas ruas.", "correta": "PREJUDICA"},
    {"imagem": "28_poluir_ar.png", "frase": "Soltar fumaça e poluentes no ar.", "correta": "PREJUDICA"},
    {"imagem": "29_ignorar_vazamento.png", "frase": "Deixar vazamentos de água sem consertar.", "correta": "PREJUDICA"},
    {"imagem": "30_aparelhos_ligados.png", "frase": "Desperdiçar energia, deixando aparelhos ligados sem uso.", "correta": "PREJUDICA"}

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
