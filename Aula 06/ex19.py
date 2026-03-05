class Livro:
    def __init__(self,titulo,paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.abrir = 1

    def __str__(self):
        return f"Você acabou de abrir o livro '{self.titulo}' que tem {self.paginas} páginas no total. Você agora está na página 1"
    def avancar_paginas(self,pag):
        if pag+self.abrir>self.paginas:
            print(f'Você avançou {self.paginas-self.abrir} paginas e chegou ao final do livro!')
        else: 
            self.abrir += pag
            print(f"Você acaba de avançar {pag} paginas, você está na pagina {self.abrir}")



l1 = Livro("10 coisas que aprendi", 20)
print(l1)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)
l1.avancar_paginas(5)