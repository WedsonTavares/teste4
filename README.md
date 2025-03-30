Teste 4 Intuitive Care

Funcionalidades
1. Busca de Operadoras
Permite pesquisar operadoras de saúde e odontologia com base em um termo textual.

Exibe informações detalhadas das operadoras, incluindo:

Nome Fantasia

Modalidade

Cidade e Estado



2. API Backend (Flask)
Desenvolvida em Python com o framework Flask.

Rota /buscar:

Realiza buscas textuais no arquivo CSV de operadoras.

Retorna os registros mais relevantes conforme o termo de pesquisa.

3. Frontend (Vue.js)
Desenvolvido em Vue.js para uma interface interativa e responsiva.

Permite realizar buscas e visualizar os resultados de forma simples e eficiente.

4. Testes com Postman
Coleção de requisições configurada no arquivo api-collection.json.

Facilita o teste da API diretamente no Postman.

Como Rodar o Projeto
1. Backend
Navegue até a pasta backend.

Certifique-se de que o Python 3 está instalado.

Crie e ative um ambiente virtual:

No Windows, execute: python -m venv venv e venv\Scripts\activate.

No macOS/Linux, execute: python -m venv venv e source venv/bin/activate.

Instale as dependências com o comando: pip install -r requirements.txt.

Execute o servidor Flask com o comando: python app.py.

O backend estará rodando localmente. Abra o link do servidor local no navegador.

2. Frontend
Certifique-se de que o Node.js está instalado.

Navegue até a pasta frontend.

Instale as dependências do frontend com o comando: npm install.

Inicie o servidor de desenvolvimento com o comando: npm run serve.

Acesse o link do servidor local para interagir com a aplicação.

Testando a API no Postman
Importe a coleção de requisições no Postman, localizando o arquivo api-collection.json na pasta postman.

Teste as requisições disponíveis, como:

Buscar Operadoras - 3S

Buscar Operadoras - UNIMED

Buscar Operadoras - ODONTO

Essas requisições permitem testar a rota /buscar da API com diferentes parâmetros.

Tecnologias Utilizadas
Backend:

Python 3

Flask

Biblioteca pandas para manipulação de arquivos CSV

Frontend:

Vue.js

CSS moderno com design responsivo


Outras ferramentas:

Postman para testar a API


Sinta-se à vontade para contribuir com este projeto! Se você quiser sugerir melhorias ou corrigir problemas, basta criar um fork do repositório, fazer suas modificações e enviar um pull request.
