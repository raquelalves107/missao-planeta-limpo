
import csv
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

frases = []
categorias = []

# Ler os exemplos de treinamento
with open("dados_treinamento.csv", "r", encoding="utf-8-sig", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        frases.append(linha["frase"])
        categorias.append(linha["categoria"])

# Criar a inteligência artificial
modelo = Pipeline([
    ("vetorizador", TfidfVectorizer(ngram_range=(1, 2))),
    ("classificador", MultinomialNB())
])

# Treinar o modelo
modelo.fit(frases, categorias)

# Salvar o modelo treinado
joblib.dump(modelo, "modelo_ia.joblib")

print("Treinamento concluído com sucesso!")
print(f"Total de frases utilizadas: {len(frases)}")
print("Modelo salvo em modelo_ia.joblib")
