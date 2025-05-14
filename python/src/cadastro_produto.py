from src.conexao import conectar
def cadastrar_produto(nome:str,preco_compra:float, preco_venda:float, quantidade:int):
    conn = conectar()
    cursor = conn.cursor()
    sql = """INSERT INTO produtos (nome, preco_compra, preco_venda, quantidade) VALUES (?,?,?,?);"""
    cursor.execute(sql, (nome, preco_compra, preco_venda, quantidade))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Ok produto '{nome}' cadastrado com sucesso")