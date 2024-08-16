import os, os.path
from model import Cliente
from model import Categoria
from model import Produto
from model import Fornecedor
from model import Vendas
from controller import FornecedorController
from controller import VendasController
from model import Estoque
from controller import CategoriaController
from controller import ClienteController
from controller import EstoqueController
from controller import RelatoriosController
import datetime

def cria_arquivo(*args):
    for i in args:
        if not os.path.exists(i):
            with open (i, 'w') as arq:
                arq.write("")
                
cria_arquivo("categoria.txt", "fornecedor.txt", "estoque.txt", "cliente.txt", "vendas.txt")




#######################################################################################################
def tela_de_vendas():
    os.system("cls")
    #colocar a lista de produtos salvos em estoque
    
    produtosList = []
    nome = input('entre com o nome do cliente')
    cpf = input('entre com cpf')
    cliente = Cliente(nome, cpf)
    VendasController.vendasCliente(cliente)
    
    while True:
        
        EstoqueController.ler_estoque_controller()
        nomeProuto = input('entre com o nome do produto')
        quantidade = int(input('entre com a quantidade'))
        produto = VendasController.atualizar_estoque(nomeProuto, quantidade)
        
        if not produto:
            continue
        
        produtodict = {'produto': produto, 'quantidade': quantidade}
        produtosList.append(produtodict)
        
        sair = int(input(('sair? (S = 1 / N - 0)')))
        
        os.system("cls")
        
        if sair:
            break

    
    venda = Vendas(cliente.nome, produtosList, VendasController.calcularTotal(produtosList))
    VendasController.realizarVenda(venda)
        
      
#######################################################################################################
def proximaTela(nome):
    
    os.system('cls')
    
    print("------------------------")
    print(f"1- cadastrar {nome}")
    print(f"2- remover {nome}")
    print(f"3- modificar {nome}")
    print("-------------------------")
    option = int(input("escolha uma das opcções acima "))
    
    if option == 1:
         
        if(nome == 'cliente'):
            nome_pessoa = input(f"nome do {nome} ")
            cpf = (input("cpf "))
            cliente = Cliente(nome_pessoa, cpf.strip())
            controller = ClienteController()
            controller.cadastrar_cliente(cliente)
        elif(nome == 'produto'):
            
            nome_produto = input("entre com o nome do produto ")
            preco = float(input("entre com o valor do produto "))
            categoria = input("entre com a categoria ")
            produto = Produto (nome_produto, preco, Categoria(categoria) )
            quantidade = int(input('entre com a quantidae em estoque'))
            estoque = Estoque (produto, quantidade)
            controller = EstoqueController()
            controller.cadastrar_produto(estoque)
            
        elif(nome == 'categoria'):
            nome_categoria = input("digite o nome da categoria ")
            categoria = Categoria(nome_categoria.strip())
            cadastro = CategoriaController()
            cadastro.cadastrar_categ(categoria)
           
        elif nome == 'fornecedor':
            nome_fornecedor =input("entre com o nome do fornecedor")
            categoria = input('entre com a categoria')
            cnpj = input('entre com o cnpj')
            fornecedor = Fornecedor(nome_fornecedor, Categoria(categoria), cnpj)
            
            controller = FornecedorController()
            controller.cadastrar_fornecedor(fornecedor)
            
    elif option == 2:
        
        if nome == 'cliente':
            cliente_a_ser_removido = input(f"qual {nome} deseja remover?")
            controller = ClienteController()
            controller.remover_cliente(cliente_a_ser_removido)
        
            
        elif nome == 'categoria':
            nome_cat = input("digite o nome da categoria a ser removida")
            cat = CategoriaController()
            cat.remover_categ(Categoria(nome_cat))
            
        
        elif nome == 'fornecedor':
            nome_fornecedor = input("digite o nome do fornecedor a ser removido")
            controller = FornecedorController()
            controller.remover_forncedor(nome_fornecedor)
        
        elif nome == 'produto':
            produto = input("entre com o produto desejado para ser removido")
            controller = EstoqueController()
            controller.remover_produto(produto)
            
    elif option == 3:
        if nome == 'categoria':
            antiga_categoria = input("entre com o nome da categoria a ser modificada ")
            nova_categoria = input("entre com a nova categoria ")
            categ = CategoriaController()
            categ.modifcar_categ(antiga_categoria, nova_categoria)
        
        elif nome == 'cliente':
            antigo = input("entre com o nome do cliente que deseja ser alterado")
            novo = input('entre com o nome do novo cliente')
            cpf = input("entre com o novo cpf")
            novo_cliente = Cliente(novo, cpf)
            controller = ClienteController()
            controller.modificar_cliente(antigo, novo_cliente)
        
        elif nome == 'fornecedor':
            antigo = input("entre com o nome do fornecedor que deseja ser alterado")
            novo = input('entre com o nome do novo fornecedor')
            cnpj = input("entre com o cnpj do novo fornecedor")
            categoria = input('entre com a categoria')
            novo_fornecedor = Fornecedor(novo,Categoria(categoria), cnpj)
            controller = FornecedorController()
            controller.modificar_fornecedor(antigo, novo_fornecedor)
            
        elif nome == 'produto':
            produto = input('entre com o nome do produto que deseja alterar')
            novo_nome = input('entre com o nome do novo produto')
            preco = float(input('entre com o valor'))
            cat = input('entre com a categoria')
            quantidade = int(input('entre com a quantidade'))
            controller = EstoqueController()
            controller.modificar_produto(produto, novo_nome, cat, quantidade, preco)
            
            
                
 ###########################################################################   
def tela_de_relaltorios():
    
    os.system('cls')
    print("1- relatorio geral de vendas")
    print("2- relatorio de vendas por data")
    print("3- relatorio de produtos mais vendidos")
    print("4-  relatorio de clientes que mais compram")
    
    esocolha = 0
    while True:
        try:
            esocolha = input("escolha uma das opções acima")
        except ValueError:
            print("erro de entrada")
        else:
            break
        
    if esocolha == "1":
        relatorio = RelatoriosController.relatorio_geral_de_vendas()
        print("------------------------------------")
        print(f"TOTAL: {relatorio}")
    
    
    if esocolha == '2':
        data_inicio = datetime
        data_fim = datetime
        inicio = input('entre com o incio da data (dd/mm/yyyy)')
        fim = input('entre com o final da data')
        relatorio = RelatoriosController()
        inicio = data_inicio.datetime.strptime(inicio, "%d/%m/%Y")
        fim = data_fim.datetime.strptime(fim, "%d/%m/%Y")
        relatorio.relatorio_de_vendas_por_data(inicio,fim )

    
    if esocolha == "3":
        os.system("cls")
        print("---------------------------------------")
        print("PRODUTOS MAIS VENDIDOS")
        produtos_mais_vendidos = RelatoriosController.produtos_mais_vendidos()
        produtos_mais_vendidos.sort(reverse= True, key= lambda x: x[1])
        for i in produtos_mais_vendidos:
            print(i)
    
    if esocolha == "4":
        os.system('cls')
        print('-----------------------------------------')
        print('clientes mais rentaveis')
        clientes = RelatoriosController.clientes_mais_ativos()
        clientes.sort(reverse= True, key= lambda x: x[1])
        for i in clientes:
            print(i)
        
            
    
    
        

######## TELA PRINCIPAL ################

while True:
    print("-------- MERCEARIA DO WESLEY -----------")
    print("MENU:")
    print("1- configurações de produtos")
    print("2- configurações de clientes")
    print("3- configurações de fornecedor")
    print("4- configurações de categoria")
    print("5- acessar caixa")
    print("6- relatorio de vendas")
    print("7- sair")
    
    options = int(input("escolha uma das opções acima"))
    if options == 1:
        proximaTela('produto')
    elif options == 2:
        proximaTela('cliente')
    elif options == 3:
        proximaTela('fornecedor')
    elif options == 4:
        proximaTela("categoria")
    elif options == 5:
        tela_de_vendas()
    elif options == 6:
        tela_de_relaltorios()
    elif options == 7:
        break
    else:
        print("opção invalida")