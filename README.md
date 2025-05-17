# 🛒 MiniMercado

Um sistema simples de controle de **estoque e cálculo de lucros**, desenvolvido em **Python** com conexão ao **SQL Server**. Ideal para pequenos negócios que desejam organizar suas operações com praticidade e controle.

---

## 📌 Funcionalidades

- Cadastro e consulta de produtos
- Controle de estoque
- Cálculo de lucro por venda
- Integração com banco de dados SQL Server
- Código limpo e modular com boas práticas

---

## ⚙️ Tecnologias Utilizadas

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" width="40" />
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" width="40" />

- Python 3.x !
- SQL Server
- [pyodbc](https://github.com/mkleehammer/pyodbc)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- SQLite (para versão alternativa local)
- VS Code

---

## 🧩 Estrutura do Projeto

```
Minimercado/
│
├── src/                     # Código-fonte
│   ├── conexao.py           # Conexão com SQL Server via pyodbc
│   └── main.py              # Arquivo principal de execução
│
├── venv/                    # Ambiente virtual (ignorado pelo Git)
├── .env                     # Variáveis de ambiente (não subir para o Git)
├── requisitos.txt           # Dependências do projeto
└── README.md                # Documentação
```

---

## 📥 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/minimercado.git
cd minimercado
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requisitos.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com os dados da sua conexão:

```env
DRIVER=ODBC Driver 18 for SQL Server
SERVER=LUCAS\SQLEXPRESS
DATABASE=mercado
```



### 5. Execute o projeto

```bash
python src/main.py
```

---

## ✅ Exemplo de saída

```bash
Conectado com sucesso!
```

---

## 📌 Requisitos

- Python 3.8 ou superior
- SQL Server instalado
- ODBC Driver 18 for SQL Server
- Biblioteca `pyodbc` instalada corretamente

---

## 📫 Contato

Desenvolvido com dedicação por **Lucas Carlos Pessoa**.  
Se quiser trocar ideias, sugestões ou colaborações, estou à disposição!

---

⭐ Se você curtir o projeto, deixe uma estrela no repositório!
