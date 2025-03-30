from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Caminho absoluto para o arquivo CSV
csv_path = os.path.join(os.path.dirname(__file__), 'dados', 'Relatorio_cadop.csv')

try:
    # Tenta carregar o CSV, ignorando linhas problemáticas
    df = pd.read_csv(csv_path, on_bad_lines='skip', delimiter=';').fillna('')
    df['Nome_Fantasia'] = df['Nome_Fantasia'].str.strip().fillna('')  # Remove espaços extras e valores nulos
    print("Colunas disponíveis no DataFrame:", df.columns.tolist())  # Depuração
    print("Valores na coluna Nome_Fantasia:", df['Nome_Fantasia'].tolist())  # Depuração
except Exception as e:
    print(f"Erro ao carregar o arquivo CSV: {e}")
    df = pd.DataFrame()  # Cria um DataFrame vazio para evitar falhas

@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('termo', '')
    if df.empty:
        return jsonify({"erro": "Arquivo CSV não pôde ser carregado ou está vazio."}), 500

    # Busca na coluna Nome_Fantasia
    resultados = df[df['Nome_Fantasia'].str.contains(termo, case=False, na=False)].to_dict(orient='records')
    return jsonify(resultados)

if __name__ == '__main__':
    print("Servidor rodando! Acesse: http://127.0.0.1:5000/buscar?termo=exemplo")
    app.run(debug=True)