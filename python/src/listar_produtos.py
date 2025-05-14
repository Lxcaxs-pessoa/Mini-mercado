from src.conexao import conectar
def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, nome, quantidade, preco_venda FROM produtos")

        produtos = cursor.fetchall()

        if not produtos:
            print("Nenhum produto cadastrado ")
            return
        print("\n=== Lista de Produtos Cadastrados ===")
        print(f"{'ID':<5}{'Nome':<20}{'Qtd':<10}{'Preço Venda':<15}")
        print("-" * 50)

        for prod in produtos:
            id_prod, nome, qtd, preco = prod
            print(f"{id_prod:<5}{nome:<50}{qtd:<10}{preco:<15.2f}")
    
    
    except Exception as e:
        print(f"Erro ao listar os produtos {e}")
    finally:
        cursor.close()
        conn.close()
