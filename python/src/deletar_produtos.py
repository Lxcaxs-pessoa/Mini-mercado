from src.conexao import conectar

def excluir_produtos():
    conn = conectar()
    cursor = conn.cursor()

    try:
        produto = input("Digite ID ou Nome do produto que deseja excluir: ").strip()

        if produto.isdigit():
            cursor.execute("SELECT id, nome FROM produtos WHERE id = ?", (int(produto),))
        else:
            cursor.execute("SELECT id, nome FROM produtos WHERE nome LIKE ?", (f"%{produto}%",))

        resultado = cursor.fetchone()

        if not resultado:
            print("❌ Produto não encontrado.")
            return

        id_produto, nome = resultado
        confirmacao = input(f"Tem certeza que deseja excluir o produto '{nome}' (ID: {id_produto})? [s/N]: ").strip().lower()

        if confirmacao != 's':
            print("❌ Exclusão cancelada.")
            return

        cursor.execute("SELECT COUNT(*) FROM vendas WHERE id_produto = ?", (id_produto,))
        vendas_associadas = cursor.fetchone()[0]

        if vendas_associadas > 0:
            print("❌ Este produto possui vendas registradas e não pode ser excluído.")
            return

        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        conn.commit()
        print("✅ Produto excluído com sucesso.")

    except Exception as e:
        print(f"❌ Erro ao excluir o produto: {e}")
    finally:
        cursor.close()
        conn.close()
