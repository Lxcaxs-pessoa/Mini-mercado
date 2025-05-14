from src.cadastro_produto import cadastrar_produto
from src.registrar_vendas import registrar_vendas  
from src.listar_vendas import listar_vendas
from src.listar_produtos import listar_produtos
from src.relatorio_lucros import relatorio_lucros
from src.buscar_produto import buscar_produto
from src.atualizar_produto import atualizar_produto
from src.deletar_produtos import excluir_produtos
def cadastrar_produto_interativamente():
    nome = input("Digite um nome de um produto: ")

    if not nome:
        print("❌ Nome do produto não pode estar vazio. ")
        from src.cadastro_produto import cadastrar_produto


def cadastrar_produto_interativamente():
    nome = input("Digite um nome de um produto: ")

    if not nome:
        print(" Nome do produto não pode estar vazio. ")
        return

    try:
        preco_compra = float(input("Digite o preço da compra: "))
        if preco_compra <= 0:
            print(" O preço de compra não pode ser menor ou igual a zero ")
            return
    except ValueError:
        print(" Preço de compra inválido ")
        return

    try:
        preco_venda = float(input("Digite o preço da venda: "))
        if preco_venda <= 0:
            print(" O preço de venda não pode ser menor ou igual a zero ")
            return
    except ValueError:
        print(" Preço de venda inválido ")
        return
    try:
        quantidade = int(input("Informe a quantidade: "))
        if quantidade < 0:
            print(" A quantidade não pode ser negativa")
            return
    except ValueError:
        print(" Quantidade inválida ")
        return



def main(): 
    while True: 
        print("""
=== MiniMercado ===
1 - Cadastrar produto
2 - Registrar venda
3 - Listar produtos
4 - Listar vendas
5 - Relatório de lucros
6 - Buscar produto
7 - Atualizar produto
8 - Excluir produto
              
0 - Sair
""")  

        opc = input("Escolha uma opção: ").strip()  
        if opc == "1":
     
            nome = input("Digite o nome do produto: ") 
            preco_compra = float(input("Digite o preço de compra: "))
            preco_venda = float(input("Digite o preço de venda: ")) 
            quantidade = int(input("Quantidade inicial: "))  

            cadastrar_produto(nome, preco_compra, preco_venda, quantidade)

        elif opc == "2":
          
            pid = int(input("ID do produto: "))
            qt_v = int(input("Quantidade vendida: "))
            registrar_vendas(pid, qt_v)
        
        elif opc == "3":
            listar_produtos()

        elif opc == "4":
            listar_vendas()

        elif opc == "5":
            relatorio_lucros()

        elif opc == "6":
            buscar_produto()

        elif opc == "7":
            atualizar_produto()    

        elif opc == "8":
            excluir_produtos()
                    
        elif opc == "0":
            print("Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
