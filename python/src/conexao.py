import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

def conectar():
    conexao = pyodbc.connect(
        f"DRIVER={{{os.getenv('DRIVER')}}};"
        f"SERVER={os.getenv('SERVER')};"
        f"DATABASE={os.getenv('DATABASE')};"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    return conexao

def main():
    conn = conectar()
    print("Conectado com sucesso!")
    conn.close()
