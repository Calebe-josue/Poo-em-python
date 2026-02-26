from rich import print
from rich.table import Table

class Produto:

    tabela = Table(title="Produto")
    tabela.add_column("Nome",justify="center")
    tabela.add_column("Preço",justify='center')

    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    
    def etiqueta(self):
        Produto.tabela.add_row(f"{self.nome}",f"{self.preco:,.2f}")
        return Produto.tabela


prod1 = Produto("Iphone",10000)
print(prod1.etiqueta())