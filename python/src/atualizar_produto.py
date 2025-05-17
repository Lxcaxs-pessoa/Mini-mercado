from src.conexao import conectar

def atualizar_produto():
    conn = conectar()
    cursor = conn.cursor()
    try:
        produto_id = int(input('Digite o ID do produto que vai ser alterado: '))

        cursor.execute('SELECT id, nome, quantidade, preco_venda, preco_compra FROM produtos WHERE id = ?', (produto_id,))
        resultado = cursor.fetchall()
        
        if not resultado:
            print("❌ Produto não encontrado.")
            return
        
        print("\nProduto encontrado:")
        for prod in resultado:
            print(f"ID: {prod[0]}, Nome: {prod[1]}, Quantidade: {prod[2]}, Preço Venda: {prod[3]}, Preço Compra: {prod[4]}")

        print("\nDigite os novos dados (pressione Enter para manter o valor atual):")

        novo_nome = input("Novo nome: ").strip()
        nova_qtd = input("Nova quantidade: ").strip()
        novo_preco_venda = input("Novo preço de venda: ").strip()
        novo_preco_compra = input("Novo preço de compra: ").strip()

        # Pegando os valores antigos se o usuário não digitou nada
        nome_final = novo_nome if novo_nome else resultado[0][1]
        qtd_final = int(nova_qtd) if nova_qtd else resultado[0][2]
        preco_venda_final = float(novo_preco_venda) if novo_preco_venda else resultado[0][3]
        preco_compra_final = float(novo_preco_compra) if novo_preco_compra else resultado[0][4]

        cursor.execute("""
            UPDATE produtos 
            SET nome = ?, quantidade = ?, preco_venda = ?, preco_compra = ?
            WHERE id = ?
        """, (nome_final, qtd_final, preco_venda_final, preco_compra_final, produto_id))

        conn.commit()
        print("✅ Produto atualizado com sucesso.")

    except Exception as e:
        print(f"❌ Erro ao atualizar o produto: {e}")
    finally:
        cursor.close()
        conn.close()
