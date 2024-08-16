from model import Cliente, Categoria, Produto, Fornecedor, Estoque, Vendas
from dao import CategoriaDao, FornecedorDao, ClienteDao, EstoqueDao, VendasDao

class ClienteController:
    def cadastrar_cliente(self, cliente:Cliente):
        clientes = ClienteDao.ler_cliente()
        existe = list(filter(lambda x: x.cpf == cliente.cpf, clientes))
        if existe:
            print("nao foi possivel realizar o cadastro pois o cliente já consta no sistema")
        else:
            ClienteDao.cadatrar_cliente(cliente)
            print('cliente cadastrado com sucesso')
            
    def remover_cliente(self, nome):
        clientes = ClienteDao.ler_cliente()
        cliente = list(filter(lambda x: clientes[x].nome == nome, range(len(clientes))))
        if cliente:
            ClienteDao.remover_cliente(cliente[0])
            print('cliente removido')
        else:
            print("cliente nao encontrado")  
    
    def modificar_cliente(self, antigo, novo):
        clientes = ClienteDao.ler_cliente()
        antigo_cliente_existe = list(filter(lambda x: x.nome == antigo, clientes)) 
        novo_cliente_existe = list(filter(lambda x: x.nome == novo, clientes)) 
        
        if antigo_cliente_existe:
            if not novo_cliente_existe:
                clientes = list(map(lambda x: novo if antigo == x.nome else(x), clientes))
                ClienteDao.modificar_cliente(clientes)
                print('cliente foi modificado com sucesso')
            else:
                print("cliente ja existe no sistema")
        else:
            print("cliente nao encontrado")
            
class EstoqueController:
    def cadastrar_produto(self, prod:Estoque):
        produtos = EstoqueDao.ler_estoque()
        categoria = CategoriaDao.ler_categ()
        existe_produto = list(filter(lambda x: x.produto.nome == prod.produto.nome, produtos))
        existe_categoria = list(filter(lambda x: x.nome == prod.produto.categoria.nome, categoria))
        
        if not existe_produto:
            if existe_categoria:
                EstoqueDao.salvar_produto(prod)
                print('produto cadastrado com sucesso')
            else:
                print("nao foi possivel cadastrar o produto pois a categoria informada nao existe no sistema")
        else:
            print("nao foi possivel realizar o cadastro pois o produto já consta no estoque")
            
    
    def remover_produto(self, nome):
        produtos = EstoqueDao.ler_estoque()
        index = list(filter(lambda x: produtos[x].produto.nome == nome, range(len(produtos))))
        if index:
            EstoqueDao.remover_produto(index[0])
            print('produto removido')
        else:
            print("produto nao encontrado")  
    
    def modificar_produto(self, antigo_nome, novo_nome, categoria, quantidade, preco):
        produtos = EstoqueDao.ler_estoque()
        cat = CategoriaDao.ler_categ()
        categoria_existe = list(filter(lambda x: x.nome == categoria, cat))
        antigo_nome_existe = list(filter(lambda x: x.produto.nome == antigo_nome, produtos)) 
        novo_nome_existe = list(filter(lambda x: x.produto.nome == novo_nome, produtos)) 
        
        if antigo_nome_existe:
            if not novo_nome_existe:
                if categoria_existe:
                    produtos = list(map(lambda x: Estoque(Produto(novo_nome, preco, Categoria(categoria)), quantidade) if x.produto.nome == antigo_nome  else(x), produtos))
                    EstoqueDao.modificar_produto(produtos)
                    print('produto foi modificado com sucesso')
                else:
                    print('categoria nao existe no sistema')
            else:
                print("produto ja existe no sistema")
        else:
            print("produto nao encontrado")
        
    def ler_estoque_controller():
        estoque = EstoqueDao.ler_estoque()
        for i in estoque:
            print(f"{i.produto.nome} - {i.quantidade} em estoque")
        
 
class VendasController:
    def vendasCliente(cliente: Cliente):
        clientes = ClienteDao.ler_cliente()
        clienteCadastrado = list(filter(lambda x: x.cpf == cliente.cpf, clientes ))
        if clienteCadastrado:
            return
        else:
            cli = ClienteController()
            cli.cadastrar_cliente(cliente)
    
    @classmethod
    def atualizar_estoque(cls, produto, quantidade):
        produtoEmEstoque: list[Estoque] = []
        estoque = EstoqueDao.ler_estoque()
        produtoEmEstoque = list(filter(lambda x: x.produto.nome == produto, estoque))
        
        if produtoEmEstoque:
            if quantidade <= produtoEmEstoque[0].quantidade:
                product = Estoque(produtoEmEstoque[0].produto, produtoEmEstoque[0].quantidade- quantidade)
                estoque = list(map(lambda x: product if produto == x.produto.nome else (x), estoque))
                EstoqueDao.atualizar_estoque(estoque)
                return produtoEmEstoque[0].produto
               
            else:
                print('a quantidade excede o estoque')     
        else:
            print('entre com um produto valido')
           
    def calcularTotal(produtos: list):
        total = 0
        produto: Produto = None
        for i in produtos:
            produto = i['produto']
            quantidade = i['quantidade']
            total +=  produto.valor * quantidade
        
        return total

    
        
        
         
    def realizarVenda(venda: Vendas):
       
        VendasDao.realizarVenda(venda)

       
class CategoriaController:
            
    def cadastrar_categ(self, cat: Categoria):
        categoria_list = CategoriaDao.ler_categ()
        existe = list(filter(lambda x: x.nome == cat.nome, categoria_list))
        if existe:
            print('categoria ja existe')
        else:
            CategoriaDao.salvarCateg(cat)
            print('categoria salva')
            
    def remover_categ(self, cat: Categoria):
        existe = list(filter(lambda x: x.nome == cat.nome, CategoriaDao.ler_categ()))
        if existe:
            CategoriaDao.remover_categ(cat)
            estoque = EstoqueDao.ler_estoque()
            estoque = list(map(lambda x: Estoque(Produto(x.produto.nome, x.produto.valor, Categoria('sem categoria')), x.quantidade) if x.produto.categoria.nome == cat.nome else(x), estoque))
            EstoqueDao.modificar_produto(estoque)
            print('categoria removida com sucesso')
            
        else:
            print('categoria nao existe')
            
    def modifcar_categ(self, categoria, nova_categ):
        categoria_list =  CategoriaDao.ler_categ()
        antiga_categ_existente = list(filter(lambda x: x.nome == categoria, categoria_list))
        nova_categ_existente = list(filter(lambda x: x.nome == nova_categ, categoria_list))
        
        if antiga_categ_existente:
            if not nova_categ_existente:
                categoria_list = list(map(lambda x: Categoria(nova_categ) if categoria == x.nome else (x), categoria_list))
                CategoriaDao.modificar_categ(categoria_list)
                estoque = EstoqueDao.ler_estoque()
                estoque = list(map(lambda x: Estoque(Produto(x.produto.nome, x.produto.valor, Categoria(nova_categ)), x.quantidade) if x.produto.categoria.nome == categoria else(x), estoque))
                EstoqueDao.modificar_produto(estoque)
                print("categoria modificada com sucesso")
            else:
                print('nao foi possivel modificar pois a categoria ja consta no sistema')
        else:
            print('categoria nao existe')
                   
           
class FornecedorController:
    
    @staticmethod
    def cadastrar_fornecedor(fornecedor: Fornecedor):
        fornecedor_list = FornecedorDao.ler_fornecedor()
        existe = list(filter(lambda x: x.nome == fornecedor.nome, fornecedor_list))
        if existe:
            print('fornecedor ja existe')
        else:
            FornecedorDao.salvar_fornecedor(fornecedor)
            print('fornecedor salvo') 

    @staticmethod
    def remover_forncedor(nome_fornecedor):
        forneceodoes = FornecedorDao.ler_fornecedor()
        index = list(filter(lambda x: forneceodoes[x].nome == nome_fornecedor, range(len(forneceodoes))))
        if index:
            FornecedorDao.remover_fornecedor(index[0])
            print('fornecedor removido')
        else:
            print("fornecedor nao encontrado")  
        
    def modificar_fornecedor(self, antigo, novo):
        fornecedores = FornecedorDao.ler_fornecedor()
        antigo_fornecedor_existe = list(filter(lambda x: x.nome == antigo, fornecedores)) 
        novo_fornecedor_existe = list(filter(lambda x: x.nome == novo, fornecedores)) 
        
        if antigo_fornecedor_existe:
            if not novo_fornecedor_existe:
                fornecedores = list(map(lambda x: novo if antigo == x.nome else(x), fornecedores))
                FornecedorDao.modificar_fornecedor(fornecedores)
                print('fornecedor foi modificado com sucesso')
            else:
                print("fornecedor ja existe no sistema")
        else:
            print("fornecedor nao encontrado")
   
    
  #----------------------------------------------------------------------------------------------------
  #----------------------------------------------------------------------------------------------------          
class RelatoriosController:
            
    @classmethod
    def relatorio_geral_de_vendas(cls):
        totais = 0
        VendasDao.mostrar_vendas()
        vendas_feitas = VendasDao.ler_vendas()
        for i in vendas_feitas:
            totais += i.total
            
        return totais
    @classmethod
    def produtos_mais_vendidos(cls):
        
        vendas_realizadas = VendasDao.ler_vendas()
        produtos_set = set()
        lista_de_produtos = []
        produtos_mais_vendidos = []
        
        for i in vendas_realizadas:
            produtos = i.produtos
            for j in produtos:
                produto: Produto = j["produto"]
                lista_de_produtos.append(j)
                produtos_set.add(produto)
                
        for i in produtos_set:
            quantidade_de_vendas = [x["quantidade"] for x in lista_de_produtos if x["produto"] == i ]
            quantidade_de_vendas = sum(quantidade_de_vendas)
            produtos_tupla = (i.nome, quantidade_de_vendas)
            produtos_mais_vendidos.append(produtos_tupla)
            
        
        return produtos_mais_vendidos
    
    
    @classmethod
    def clientes_mais_ativos(cls):
              
        vendas_realizadas = VendasDao.ler_vendas()
        clientes_set = set()
        lista_de_clientes = []
        produtos_comprados = []
        
        for i in vendas_realizadas:
            produtos = i.produtos
            clientes_set.add(i.cliente)
            for j in produtos:
                produtos_comprados.append(j)
               
                
        for i in clientes_set:
            total_comprado = [x.total for x in vendas_realizadas if x.cliente == i]
            total_comprado = sum(total_comprado)
            compras_cliente = (i, total_comprado)
            lista_de_clientes.append(compras_cliente)
            
        
        return lista_de_clientes
        
            
                    
    def relatorio_de_vendas_por_data(self, inicio, fim):
        venda = VendasDao.ler_vendas()
        soma = 0
        venda_por_data: list[Vendas] = []
        for i in venda:
            venda_por_data = list(filter(lambda x:  x.data >= inicio and x.data <= fim, venda))

  
        for i in venda_por_data:
            print('------------------------------------------------------')
            print(i.data.strftime("%d/%m/%Y"))
            print(i.cliente)
            produtos = i.produtos
            for j in produtos:
                produto = j ['produto']
                print(produto.nome, j['quantidade'])
            print(f"R${i.total}")
        print("-----------------------------------------------------------")
        
        for i in venda_por_data:
            soma += i.total
        print(f"TOTAL DE VENDAS: R${soma}")