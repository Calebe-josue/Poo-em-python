from rich import print
from rich.panel import Panel

class Churrasco:
    # Atributos de Classe
    consumo_padrao:float = 0.400 # Cada pessoa come em média 400g de carne
    preco_kg:float = 82.40 # Cada Kg de carne custa R$82.40

    def __init__(self,titulo,qnt):
        # Atributos de instância
        self.titulo = titulo
        self.qnt = qnt

    def __str__(self):
        return f"Esse é {self.titulo} com {self.qnt} pessoas participando."
    

    def calcular_qnt_carne(self) -> float:
        return self.qnt * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qnt_carne() * Churrasco.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.qnt

    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.qnt} convidados[/]"
        conteudo += f"\nCada participante comerá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_kg:,.2f}"
        conteudo += f"\nRecomendo comprar [blue]{self.calcular_qnt_carne():.3f}Kg[/] de carne"
        conteudo += f"\nO custo total será de [green]R${self.calcular_custo_total():,.2f}[/]"
        conteudo += f"\nCada pessoa pagará [yellow]R${self.calcular_custo_individual():,.2f}[/] para participar."
        painel = Panel(conteudo, title=self.titulo)
        print(painel)


pes1 = Churrasco('Churras dos Amigos',15)
pes1.analisar()


c2 = Churrasco("Festa do fim de ano", 80)
c2.analisar()