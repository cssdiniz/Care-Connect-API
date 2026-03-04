**Care Connect API**

**Descrição**

A Care Connect API é uma aplicação desenvolvida para conectar pessoas que necessitam de serviços de cuidador a profissionais de confiança cadastrados na plataforma.

A API permite o cadastro, consulta, atualização e remoção de cuidadores, além da busca por cidade, facilitando a localização de profissionais conforme a necessidade do usuário.

**Tecnologias Utilizadas**
- Python
  
- Flask
  
- Flask-CORS
  
- SQLAlchemy
  
- SQLite

**Arquitetura**

A API segue o padrão REST e utiliza:

- Flask para gerenciamento das rotas HTTP
  
- SQLAlchemy como ORM para manipulação do banco de dados
  
- SQLite como banco de dados relacional

A aplicação opera por padrão na porta 5000.

**Instalação e Execução**

**1. Clonar o repositório**

git clone <url-do-repositorio>

cd care-connect

**2. Instalar as dependências**

pip install flask flask-cors sqlalchemy

**3. Executar a aplicação**

python app.py

A API estará disponível em:

http://127.0.0.1:5000

**Modelo de Dados**

Tabela: usuarios

Campo	|Tipo |	Descrição

|id	| Integer |	Identificador único do usuário
| :--- | :---: |
nome	String	Nome do cuidador
email	String	Email do cuidador
telefone	String	Telefone para contato
cidade	String	Cidade de atuação
valor	Numeric	Valor cobrado por dia
experiencia	Text	Descrição da experiência profissional
