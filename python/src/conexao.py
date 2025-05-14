import pyodbc

def conectar():
    conexao = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=LUCAS\\SQLEXPRESS;"
        "DATABASE=mercado;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    return conexao

def main():
    conn = conectar()
    print("Conectado com sucesso!")
    conn.close()

main()
