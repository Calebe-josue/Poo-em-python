from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick
        self.jogos = []

    def add_favoritos(self,nome) -> list[str]:
        self.jogos.append(nome)
        


    def ficha(self) -> str:
        conteudo = f"Nome Real: {self.nome}"
        conteudo += "\nJogos favoritos:"
        self.jogos.sort()
        for i in self.jogos:
            conteudo += f"\n{i}"
        painel = Panel(conteudo,title=f"jogador<{self.nick}>")
        print(painel)


j1 = Gamer("Fabricio da Silva","detonator2025")
j1.add_favoritos("Mario Bros.")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()