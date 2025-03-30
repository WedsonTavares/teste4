from flask import Flask, request, jsonify  # Importa o Flask para criar o servidor e as funções para lidar com requisições e respostas JSON
from flask_cors import CORS  # Importa o CORS para permitir requisições de diferentes origens
import pandas as pd  # Importa o pandas para manipulação de dados
import os  # Importa o módulo os para lidar com caminhos de arquivos

# Cria uma instância do Flask
app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas, permitindo que o frontend acesse o backend

# Define o caminho absoluto para o arquivo CSV
csv_path = os.path.join(os.path.dirname(__file__), 'dados', 'Relatorio_cadop.csv')

try:
    # Tenta carregar o arquivo CSV, ignorando linhas problemáticas
    df = pd.read_csv(csv_path, on_bad_lines='skip', delimiter=';').fillna('')  # Substitui valores nulos por strings vazias
    df['Nome_Fantasia'] = df['Nome_Fantasia'].str.strip().fillna('')  # Remove espaços extras e substitui valores nulos na coluna 'Nome_Fantasia'
    print("Colunas disponíveis no DataFrame:", df.columns.tolist())  # Exibe as colunas disponíveis no DataFrame
    print("Valores na coluna Nome_Fantasia:", df['Nome_Fantasia'].tolist())  # Exibe os valores da coluna 'Nome_Fantasia'
except Exception as e:
    # Caso ocorra um erro ao carregar o CSV, exibe o erro e cria um DataFrame vazio
    print(f"Erro ao carregar o arquivo CSV: {e}")
    df = pd.DataFrame()  # Cria um DataFrame vazio para evitar falhas no restante do código

# Define a rota '/buscar' para lidar com requisições GET
@app.route('/buscar', methods=['GET'])
def buscar():
    # Obtém o parâmetro 'termo' da URL (exemplo: /buscar?termo=exemplo)
    termo = request.args.get('termo', '')
    
    # Verifica se o DataFrame está vazio (caso o CSV não tenha sido carregado corretamente)
    if df.empty:
        return jsonify({"erro": "Arquivo CSV não pôde ser carregado ou está vazio."}), 500  # Retorna um erro 500 com uma mensagem

    # Filtra o DataFrame para encontrar registros onde 'Nome_Fantasia' contém o termo buscado (case-insensitive)
    resultados = df[df['Nome_Fantasia'].str.contains(termo, case=False, na=False)].to_dict(orient='records')
    
    # Retorna os resultados como uma resposta JSON
    return jsonify(resultados)

# Ponto de entrada principal do programa
if __name__ == '__main__':
    # Exibe uma mensagem indicando que o servidor está rodando e como acessá-lo
    print("Servidor rodando! Acesse: http://127.0.0.1:5000/buscar?termo=exemplo")
    app.run(debug=True)  # Inicia o servidor Flask no modo debug
    