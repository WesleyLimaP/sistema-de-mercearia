from datetime import datetime

           
class Categoria:
    def __init__(self, nome):
        self.nome = nome

class Fornecedor:
    def __init__(self, nome, categoria: Categoria, cnpj):
        self.nome = nome
        self.categoria = categoria
        self.cnpj = cnpj
        
         
class Produto:
    def __init__(self, nome, valor: float, categoria: Categoria):
        self.nome = nome
        self.valor = valor
        self.categoria = categoria

    def __hash__(self):
        return hash((self.nome, self.valor))

    def __eq__(self, outro):
        if not isinstance(outro, Produto):
            return NotImplemented
        return self.nome == outro.nome and self.valor == outro.valor
    
class Estoque:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade
         
class Pessoa: 
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoa):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)
        
class Vendas:
    def __init__(self, cliente, produtos: list, total, data = datetime.now()):
        self.cliente = cliente
        self.produtos = produtos
        self.total = total
        self.data = data