from src.conexao import conectar
import csv
from datetime import datetime

def relatorio_lucros():
    conn =  conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT produtos.preco_compra, produtos.preco_venda, vendas.quantidade_vendida, produtos.nome FROM vendas JOIN produtos ON vendas.id_produto = produtos.id")

        lucros = cursor.fetchall()

        if not lucros:
            print("Nenhuma venda encontrada !")
            return
        print("\n=== Relatório de Lucros ===")
        print(f"{'Produto':<20}{'Lucro Unit.':<15}{'Qtd':<8}{'Lucro Total':<15}")
        print("-" * 60)
         
        lucro_geral = 0
        relatorio = []

        # Para cada venda, calcula o lucro e exibe
        for preco_compra, preco_venda, qtd_vendida, nome in lucros:
            lucro_unitario = preco_venda - preco_compra
            lucro_total = lucro_unitario * qtd_vendida
            lucro_geral += lucro_total

            print(f"{nome:<20}R$ {lucro_unitario:<13.2f}{qtd_vendida:<8}R$ {lucro_total:<13.2f}")
            relatorio.append([nome, preco_compra, preco_venda, qtd_vendida, lucro_unitario, lucro_total])
        print("-" * 70)
        print(f"💰 {'Lucro Total Geral:':<55} R$ {lucro_geral:.2f}")

        data_str = datetime.now().strftime("%y-%m-%d_%H-%M%S")
        nome_arquivo = f"relatorio_lucros_{data_str}.csv"

        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Produto", "Preço compra", "Quantidade Vendida", "Lucro Unitário", "Lucro total"])
            writer.writerows(relatorio)
         
        print(f"\n✅ Relatório exportado com sucesso para: {nome_arquivo}")
    
    except Exception as e:
        print(f"❌ Erro ao gerar relatório de lucros: {e}")
    finally:
        cursor.close()
        conn.close()


    
