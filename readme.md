FastAPI IBBI
Descrição

Este projeto é uma aplicação de controle de vendas de e-commerce construída com FastAPI. Utiliza SQLAlchemy como ORM para interação com o banco de dados SQLite e implementa autenticação JWT para proteger rotas sensíveis.
Funcionalidades

    Cadastro de Usuários: Endpoint para registro de novos usuários.
    Autenticação: Login para obtenção de token de acesso JWT.
    Gerenciamento de Categorias: CRUD para categorias de produtos.
    Gerenciamento de Produtos: CRUD para produtos associados a categorias.
    Segurança: Rotas protegidas por autenticação JWT.
    Persistência de Dados: Utiliza SQLite para armazenamento de dados.

Pré-requisitos

    Python 3.7+
    Pip (gerenciador de pacotes do Python)
    Ambiente virtual (recomendado para isolamento de dependências)

Instalação

    Clone o repositório:

    bash

git clone https://github.com/seu-usuario/FastApi_IBBI.git
cd FastApi_IBBI

Crie e ative um ambiente virtual (opcional, mas recomendado):

bash

python -m venv venv
source venv/bin/activate   # No Windows use `venv\Scripts\activate`

Instale as dependências:

bash

    pip install -r requirements.txt

Configuração

    Banco de Dados SQLite:

    O projeto utiliza SQLite como banco de dados padrão. A configuração está definida no arquivo app/database.py. Você pode modificar a URL do banco de dados conforme necessário.

    Chave Secreta JWT:

    A chave secreta JWT está definida no arquivo app/auth.py. Modifique a variável SECRET_KEY conforme necessário para sua aplicação em produção.

Executando a Aplicação

    Inicie a aplicação usando Uvicorn:

    bash

    uvicorn app.main:app --reload

    Acesse a API em http://127.0.0.1:8000.

Uso

    Documentação da API:

    A documentação interativa da API está disponível em /docs. Por exemplo, após iniciar a aplicação, abra http://127.0.0.1:8000/docs no navegador para explorar e testar os endpoints disponíveis.

    Endpoints Disponíveis:
        /register: Endpoint para registro de novos usuários.
        /token: Endpoint para obter token de acesso JWT (login).
        /categories/: CRUD para categorias de produtos.
        /products/: CRUD para produtos associados a categorias.

Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias, correções ou novas funcionalidades.
Licença

Este projeto é licenciado sob a MIT License. Consulte o arquivo LICENSE para mais detalhes.
Observações:

    Modificações Necessárias: Personalize as seções conforme necessário para refletir melhor seu projeto específico.
    Links e URLs: Certifique-se de ajustar URLs e comandos de acordo com a estrutura e configuração real do seu projeto.
    Instruções de Instalação e Execução: Se houver dependências específicas que não estão listadas em requirements.txt, certifique-se de adicioná-las.
    Documentação da API: O FastAPI gera automaticamente uma documentação interativa com Swagger UI, acessível em /docs após iniciar a aplicação.