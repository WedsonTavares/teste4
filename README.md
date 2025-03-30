Teste 4 Intuitive Care
Este projeto é uma aplicação web que interage com um servidor Python para realizar buscas em uma lista de cadastros de operadoras. Ele foi desenvolvido usando Vue.js no frontend e Flask no backend.

Funcionalidades
Busca de Operadoras:

Permite buscar operadoras de saúde e odontologia com base em um termo textual.
Exibe informações como:
Nome Fantasia
Modalidade
Cidade e Estado
Telefone
API Backend:

Desenvolvida em Python com Flask.
Rota /buscar:
Realiza buscas textuais no arquivo CSV de operadoras.
Retorna os registros mais relevantes.
Frontend:

Desenvolvido em Vue.js.
Interface simples e responsiva para realizar buscas e exibir resultados.
Testes com Postman:

Coleção de requisições configurada no arquivo api-collection.json.
Permite testar a API diretamente no Postman.



GitHub Copilot
Aqui está um exemplo de um arquivo README.md claro e bem estruturado para o seu projeto:

Teste Intuitive Care
Este projeto é uma aplicação web que interage com um servidor Python para realizar buscas em uma lista de cadastros de operadoras. Ele foi desenvolvido usando Vue.js no frontend e Flask no backend.

Funcionalidades
Busca de Operadoras:

Permite buscar operadoras de saúde e odontologia com base em um termo textual.
Exibe informações como:
Nome Fantasia
Modalidade
Cidade e Estado
Telefone
API Backend:

Desenvolvida em Python com Flask.
Rota /buscar:
Realiza buscas textuais no arquivo CSV de operadoras.
Retorna os registros mais relevantes.
Frontend:

Desenvolvido em Vue.js.
Interface simples e responsiva para realizar buscas e exibir resultados.
Testes com Postman:

Coleção de requisições configurada no arquivo api-collection.json.
Permite testar a API diretamente no Postman.



Estrutura do Projeto

Teste 4/
├── backend/
│   ├── app.py                # Servidor Flask
│   ├── dados/
│   │   └── Relatorio_cadop.csv # Arquivo CSV com os dados
│   └── requirements.txt      # Dependências do Python
├── frontend/
│   ├── public/
│   │   └── index.html        # HTML principal
│   ├── src/
│   │   ├── components/
│   │   │   └── Search.vue    # Componente Vue para busca
│   │   ├── styles/
│   │   │   └── index.css     # Estilos globais
│   │   ├── App.vue           # Componente principal
│   │   ├── main.js           # Ponto de entrada do Vue.js
│   │   
│   ├── package.json          # Configuração do npm
│   └── node_modules/         # Dependências do Node.js 
├── postman/
│   └── api-collection.json   # Coleção do Postman para testar a API

├── .gitignore(ignorar venv e node_modules)
└── README.md                 # Documentação do projeto




Como rodar o projeto

1. Backend

-Navegue até a pasta backend
-Certifique-se de que o Python 3 está instalado.
-Crie e ative um ambiente virtual:

python -m venv venv

venv\Scripts\activate  


- Isntale as dependências: 

pip install -r backend/requirements.txt


-Execute o comando:
python backend/app.py

clique no link do servidor local.


2. Frontend

-Certifique-se de que o Node.js está instalado.
-Navegue até a pasta frontend:

npm install

npm run serve


-acesse o link do servidor local


Testando a API no Postman
Importe o arquivo api-collection.json no Postman:
Caminho: api-collection.json
Teste as requisições disponíveis, como:
Buscar Operadoras - 3S
Buscar Operadoras - UNIMED
Buscar Operadoras - ODONTO


