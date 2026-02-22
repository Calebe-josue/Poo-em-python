# Declaração da classe
class Gafanhoto:
    """
Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade.

Para criar uma nova pessoa, use
variavel = Gafanhoto(nome, idade)
    """
    def __init__(self,nome="vazio",idade=0): # Metodo construtor
        # Atributos da instância
        self.nome = nome
        self.idade = idade
        
    # Metodos de instâncias
    def aniversario(self):
        self.idade +=1
    
    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."
    
    def __str__(self):
        return "Vou te mostrar uma coisa..."

print(Gafanhoto.__doc__) # Mostra a documentação da classe