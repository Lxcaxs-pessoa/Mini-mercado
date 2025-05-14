from src.conexao import conectar
def buscar_produto():
    conn = conectar()
    cursor = conn.cursor()

    try:
        termo  = input("Digite o nome ou ID do produto que deseja buscar: ").strip()

        if termo.isdigit():
            cursor.execute("SELECT id, nome, quantidade, preco_venda FROM produtos WHERE id = ?",(int(termo),))
        else:
            cursor.execute("SELECT id, nome, quantidade, preco_venda FROM produtos WHERE nome LIKE ?",(f"%{termo}%",))
        
        resultados = cursor.fetchall()

        if not resultados:
            print("❌ Nenhum produto encontrado com esse critério ")
            return
        
        print("\n=== Resultado da Busca ===")
        print(f"{'ID':<5}{'Nome':<20}{'Qtd':<10}{'Preço Venda':<15}")
        print("-" * 50)

        for prod in resultados:
            id_, nome, qt, preco = prod
            print(f"{id_:<5}{nome:<20}{qt:<10}{preco:<15.2f}")
        
    except Exception as e:
        print(f"Erro ao buscar produto: {e}")
    finally:
        cursor.close()
        conn.close()