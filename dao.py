
from model import *


class ClienteDao:
    
    @staticmethod
    def cadatrar_cliente(cliente: Cliente):
        with open('cliente.txt', 'a') as arq:
            arq.write(f'{cliente.nome}|{cliente.cpf} \n')
            
    @staticmethod  
    def ler_cliente():
        with open('cliente.txt', 'r')as arq:
            clientes: list[Cliente] = []  
            for i in arq:
                linha = i.strip().split('|')
                cliente = Cliente(linha[0], linha[1])
                clientes.append(cliente)
        return clientes
    
    @classmethod
    def remover_cliente(cls, indice):
        clientes = cls.ler_cliente()
        del clientes[indice]
        
        with open('cliente.txt', 'w') as arq:
            for i in clientes:
                arq.write(f'{i.nome}|{i.cpf}\n')
                
                
    @staticmethod         
    def modificar_cliente(clientes: list[Cliente]):
        with open ('cliente.txt', 'w') as arq:
            for i in clientes:
                arq.write(f"{i.nome}|{i.cpf}\n")

                 
class CategoriaDao:
    @staticmethod
    def salvarCateg(categoria: Categoria):
            with open('categoria.txt', 'a') as arq:
                arq.write(f"categoria|{categoria.nome} \n")
                       
    @staticmethod
    def ler_categ():
        with open('categoria.txt', 'r') as arq:
            categorias: list[Categoria] = []
            for i in arq:
                linha = i.strip().split('|')
                categorias.append(Categoria(linha[1]))
                
        return categorias
    
    @classmethod
    def remover_categ(cls, categoria: Categoria):
        categ = cls.ler_categ()
        for i in range(len(categ)):
            if categ[i].nome == categoria.nome:
                del categ[i]
                break
                
        with open('categoria.txt', 'w') as arq:
            for i in categ:
                arq.write(f"categoria|{i.nome} \n")
    
    def modificar_categ( categorias:list[Categoria]):
        with open('categoria.txt', 'w') as arq:
            for i in categorias:
                arq.write(f"categoria|{i.nome} \n")
    
class FornecedorDao:
    @staticmethod
    def salvar_fornecedor(fornecedor: Fornecedor):
        with open('fornecedor.txt', 'a') as arq:
            arq.write(f"{fornecedor.nome}|{fornecedor.categoria.nome}|{fornecedor.cnpj} \n")
              
    @staticmethod  
    def ler_fornecedor():
        with open('fornecedor.txt', 'r')as arq:
            fornecedores: list[Fornecedor] = []  
            for i in arq:
                linha = i.strip().split('|')
                fornecedor = Fornecedor(linha[0], Categoria(linha[1]), linha[2])
                fornecedores.append(fornecedor)
            return fornecedores
    
    @classmethod
    def remover_fornecedor(cls, indice):
        fornecedores = cls.ler_fornecedor()
        del fornecedores[indice]
        
        with open('fornecedor.txt', 'w') as arq:
            for i in fornecedores:
                arq.write(f'{i.nome}|{i.categoria.nome}|{i.cnpj}\n')
    
    @staticmethod         
    def modificar_fornecedor(fornecedores: list[Fornecedor]):
        with open ('fornecedor.txt', 'w') as arq:
            for i in fornecedores:
                arq.write(f"{i.nome}|{i.categoria.nome}|{i.cnpj}\n")
    
            
class EstoqueDao:
    
    @staticmethod
    def salvar_produto(produto: Estoque):
        with open('estoque.txt', 'a') as arq:
            arq.write(f"{produto.produto.nome}|{str(produto.produto.valor)}|{produto.produto.categoria.nome}|{str(produto.quantidade)} \n")      
    
    @staticmethod  
    def ler_estoque():
        with open('estoque.txt', 'r')as arq:
            produtos: list[Estoque] = []  
            for i in arq:
                linha = i.strip().split('|')
                produto = Produto(linha[0], float(linha[1]), Categoria(linha[2]))
                estoque = Estoque (produto, int(linha[3]))
                produtos.append(estoque)
            return produtos
        
    staticmethod    
    def atualizar_estoque(estoque: list[Estoque]):
        with open('estoque.txt', "w") as arq:
            for i in estoque:
                arq.write(f"{i.produto.nome}|{i.produto.valor}|{i.produto.categoria}|{i.quantidade}\n")
        
        
        
    @classmethod
    def remover_produto(cls, index):
        estoque = cls.ler_estoque()
        del estoque[index]
        
        with open('estoque.txt', 'w') as arq:
            for i in estoque:
                arq.write(f"{i.produto.nome}|{str(i.produto.valor)}|{i.produto.categoria.nome}|{str(i.quantidade)}\n")
    
    @staticmethod         
    def modificar_produto(produto: list[Estoque]):
        with open ('estoque.txt', 'w') as arq:
            for i in produto:
                arq.write(f"{i.produto.nome}|{str(i.produto.valor)}|{i.produto.categoria.nome}|{str(i.quantidade)}\n")
                
                
class VendasDao:
    def realizarVenda(venda: Vendas):
        prod: Produto = None
        with open('vendas.txt', "a") as arq:
            arq.write(f"{venda.cliente}|")
            for i in venda.produtos:
                prod = i['produto']
                arq.write(f"{prod.categoria}|{prod.nome}|{prod.valor}|{i['quantidade']}|")
            dataformatada = venda.data.strftime("%d/%m/%Y")
            arq.write(f"{str(venda.total)}|{dataformatada} \n")
        
    def ler_vendas():
        with open("vendas.txt", "r")as arq:
            venda: list[Vendas] = []
            for i in arq:
                linha = i.strip().split("|")
                tamanho = len(linha)
                p = []
                for j in range(0, (tamanho - 6), 4):
                    prod = Produto(linha[j+2], float(linha[j+3]), Categoria(linha[j+1]) )
                    produtos = {"produto":prod, "quantidade":int(linha[j+4])}
                    p.append(produtos)
                v = Vendas(linha[0], p, float(linha[tamanho-2]) )
                v.data = datetime.strptime(linha[tamanho - 1],  "%d/%m/%Y")
                venda.append(v)
                
            return venda
        
    @classmethod
    def mostrar_vendas(cls):
        venda = cls.ler_vendas()
        for i in venda:
            print("--------------------------------------------------------------------------------------")
            print(f"cliente - {i.cliente }")
            print("produtos - ", end=" ")
            for j in i.produtos:
                produto: Produto = None
                produto = j['produto']
                quantidade = j["quantidade"]
                print(f"{produto.categoria.nome} | {produto.nome} | valor R${produto.valor} | {quantidade}")
            print(f"total - {i.total} | data - {i.data}")
            
                
                
            
               
        

    