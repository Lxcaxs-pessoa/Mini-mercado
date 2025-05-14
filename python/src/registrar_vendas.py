from src.conexao import conectar
from datetime import date       

def registrar_vendas(id_produto: int, qt_vendida: int):
    conn = conectar()
    cursor = conn.cursor()
    try:
        # Buscar dados do produto
        cursor.execute(
            "SELECT nome, quantidade, preco_compra, preco_venda FROM produtos WHERE id = ?", 
            (id_produto,)
        )
        row = cursor.fetchone()

        # Se o produto não existir
        if not row:
            print(f"❌ Produto com ID {id_produto} não encontrado.")
            return

        # Desempacotar os dados do produto
        nome, estoque_atual, preco_compra, preco_venda = row

        # Verificar se há estoque suficiente
        if qt_vendida > estoque_atual:
            print(f"❌ Estoque insuficiente! Disponível: {estoque_atual}")
            return

        # Atualizar o estoque
        novo_estoque = estoque_atual - qt_vendida
        cursor.execute(
            "UPDATE produtos SET quantidade = ? WHERE id = ?", 
            (novo_estoque, id_produto,)
        )

        # Inserir venda na tabela
        hoje = date.today()
        cursor.execute(
            "INSERT INTO vendas (id_produto, quantidade_vendida, data_venda) VALUES (?, ?, ?)", 
            (id_produto, qt_vendida, hoje)
        )

        conn.commit()
        print(f"✅ Venda registrada com sucesso: produto '{nome}' (ID {id_produto}), quantidade {qt_vendida}.")

    except Exception as e:
        print(f"❌ Ocorreu um erro ao registrar a venda: {e}")
    finally:
        cursor.close()
        conn.close()
