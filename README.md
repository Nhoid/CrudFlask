# CRUD em Flask
---

Este é um projeto de CRUD (Create, Read, Update, Delete) desenvolvido em Flask, uma framework web em Python. O objetivo deste projeto é fornecer uma aplicação simples e funcional para gerenciar vendas, utilizando uma API RESTful e integração com um banco de dados SQLite.


## Tecnologias Utilizadas

- **Flask (3.0.3)**:
    - Utilizado para criar a API web.

- **PyJWT (tokens JWT)**:
    - Utilizado para a segurança da autenticação de usuários através de tokens JWT.
- **Flask-JWT-Extended**:
    - Utilizado para criar os Token.

- **Flask-RESTful**:
    - Utilizado para facilitar a criação de APIs RESTful com Flask.

- **Werkzeug (3.0.3)**:
    - Utilizado para a criptografia das senhas antes de serem salvas no banco de dados.

- **SQLAlchemy (2.0.30)**:
    - Utilizado para fazer a conexão com o banco de dados SQLite e aproveitar as vantagens do ORM (Object-Relational Mapping).

- **ReportLab (4.2.0)**:
    - Utilizado para a criação do relatório em PDF contendo as vendas realizadas.

- **Marshmallow (3.21.3)**:
    - Utilizado para a criação dos schemas dos modelos, facilitando a validação e serialização dos dados retornados pela API.


## Funcionalidade

1. **Autenticação JWT**
    - Utilização de JWT (JSON Web Tokens) para autenticação de usuários.
    - Registro e login de usuários.
    - Geração de token JWT após o login bem-sucedido.

   ### Endpoints

    - **Registro de Usuário**
        - **URL:** `/auth/register`
        - **Método:** `POST`
        - **Requisição:**
          ```json
          {
            "username": "exemplo",
            "password": "senha123"
          }
          ```
        - **Resposta:**
          ```json
          {
            "message": "Usuário registrado com sucesso."
          }
          ```

    - **Login de Usuário**
        - **URL:** `/auth/login`
        - **Método:** `POST`
        - **Requisição:**
          ```json
          {
            "username": "exemplo",
            "password": "senha123"
          }
          ```
        - **Resposta:**
          ```json
          {
            "Token": "seu_token_jwt"
          }
          ```

2. **CRUD de Vendas**
    - Consulta, adição, edição e exclusão de vendas.
    - Campos necessários para adição e edição: `nome_cliente`, `produto`, `valor`, `data_venda`.

   ### Endpoints

    - **Consulta de Vendas**
        - **URL:** `/sales`
        - **Método:** `GET`
      - **Requisição:** (Requer token JWT no cabeçalho `Authorization: Bearer <seu_token_jwt>`)
        - **Resposta:**
          ```json
          [
            {
              "id": 1,
              "nome_cliente": "Cliente A",
              "produto": "Produto A",
              "valor": 100.0,
              "data_venda": "2024-06-10"
            },
            ...
          ]
          ```

    - **Adicionar Venda**
        - **URL:** `/sales`
        - **Método:** `POST`
      - **Requisição:** (Requer token JWT no cabeçalho `Authorization: Bearer <seu_token_jwt>`)
          ```json
          {
            "nome": "Cliente B",
            "produto": "Produto B",
            "valor": 200.0,
            "data": "2024-06-11"
          }
          ```
        - **Resposta:**
          ```json
          {
            "message": "Venda adicionada com sucesso."
          }
          ```

    - **Editar Venda**
        - **URL:** `/sales/<id>`
        - **Método:** `PUT`
      - **Requisição:** (Requer token JWT no cabeçalho `Authorization: Bearer <seu_token_jwt>`)
          ```json
          {
            "nome": "Cliente C",
            "produto": "Produto C",
            "valor": 300.0,
            "data": "2024-06-12"
          }
          ```
        - **Resposta:**
          ```json
          {
            "message": "Venda atualizada com sucesso."
          }
          ```

    - **Excluir Venda**
        - **URL:** `/sales/<id>`
        - **Método:** `DELETE`
      - **Requisição:** (Requer token JWT no cabeçalho `Authorization: Bearer <seu_token_jwt>`)
        - **Resposta:**
          ```json
          {
            "message": "Venda excluída com sucesso."
          }
          ```
          
3. **Relatório em PDF**
   - Geração de um PDF contendo todas as vendas realizadas em um período específico.
   - Parâmetros: `start_date` (data de início) e `end_date` (data de término).

   ### Endpoint

   - **Geração de Relatório em PDF**
       - **URL:** `/sales/pdf?start_date=dd-mm-yyyy&end_date=dd-mm-yyyy`
       - **Método:** `GET`
       - **Requisição:** (Requer token JWT no cabeçalho `Authorization` com o formato `Bearer <seu_token_jwt>`)
       - **Resposta:** Retorna um arquivo PDF contendo todas as vendas realizadas no período especificado.




## Estrutura do Projeto

- **Banco de Dados**
    - Utilização do banco de dados SQLite.
    - Armazenamento das informações no arquivo `database.db`.

- **Configurações**
    - Definição das configurações no arquivo `config/config.ini`.
    - Variáveis sensíveis como acesso ao banco de dados e segredo para JWT são configuradas aqui.

- **Conexão com Banco de Dados**
    - Estabelecimento da conexão no arquivo `database/database.py`.

- **Modelos de Dados**
    - Definição dos modelos de dados e seus schemas no arquivo `database/models.py`.

- **Lógica dos Endpoints e CRUD de Vendas**
    - Implementação da lógica nos arquivos dentro do diretório `vendas/vendas_controller`.

## Instruções de Execução

1. **Clonagem do Repositório**
    - Execute o comando no terminal:
        ```
        git clone https://github.com/Nhoid/CrudFlask.git
        ```

2. **Navegação até o Diretório do Projeto**
    - Acesse o diretório do projeto:
        ```
        cd CrudFlask
        ```

3. **Configuração do Ambiente Virtual (opcional, mas recomendado)**
    - Crie e ative um ambiente virtual (venv) para isolar as dependências do projeto:
        ```
        python3 -m venv venv
        source venv/bin/activate
        ```

4. **Instalação de Dependências**
    - Instale as dependências listadas no arquivo `requirements.txt`:
        ```
        pip install -r requirements.txt
        ```

5. **Configuração**
    - Configure o arquivo `config/config.ini` com as informações necessárias, como variáveis de acesso ao banco de dados e segredo para JWT.

6. **Execução do Servidor Flask**
    - Inicie o servidor Flask executando o arquivo `app.py`.

7. **Acesso à Aplicação**
    - Acesse a aplicação em seu navegador através do endereço `http://localhost:5000`.
