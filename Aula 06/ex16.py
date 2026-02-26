from rich import print
from rich import inspect

class Funcionario:
    # Atributos de Classe
    empresa = "Curso em Vídeo"

    def __init__(self,nome,setor,cargo):
        # Atributos de instâncias
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f':handshake: Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}'
        


 # Funcionario.empresa = "Hostnet"

c1 = Funcionario('Calebe',"TI","programador")
c1.empresa = "Estudonauta"
print(c1.empresa)
print(c1.apresentacao())

c2 = Funcionario("Pedro",'Administração',"Diretor")
print(c2.apresentacao())
