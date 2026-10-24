
import joblib

# Carregar a inteligência artificial treinada
modelo = joblib.load("modelo_ia.joblib")

print("🌎 MISSÃO PLANETA LIMPO")
print("Digite uma atitude ambiental para testar a IA.")
print("Digite sair para encerrar.\n")

while True:
    frase = input("Digite uma atitude: ")

    if frase.lower().strip() == "sair":
        break

    resultado = modelo.predict([frase])[0]

    print(f"Classificação da IA: {resultado}\n")
