from src.conexao import conectar

def listar_vendas():
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT vendas.id, produtos.nome, produtos.preco_venda, vendas.quantidade_vendida, vendas.data_venda FROM vendas JOIN produtos ON vendas.id_produto = produtos.id ORDER BY vendas.data_venda DESC")
        
        vendas = cursor.fetchall()

        if not vendas:
            print ("Nenhuma venda cadastrada ")
            return
        print("\n=== Lista de Vendas Cadastradas ===")
        print(f"{'ID':<5}{'Nome':<20}{'Qtd':<10}{'Preço Venda':<15}")
        print("-" * 50)

        for venda in vendas:
            id_venda, nome, preco_venda, quantidade_vendida, data_venda = venda
            print(f"{id_venda:<5}{nome:<50}{preco_venda:<10.2f}{quantidade_vendida:<10}{data_venda:<15.2f}")

    except Exception as e:
        print(f"Erro ao listar as vendas {e}")
    finally:
        cursor.close()
        conn.close()