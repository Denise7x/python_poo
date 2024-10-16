from Livro import Livro

p1 = Livro("O Cortiço", "Aluísio de Azevedo", 1890)
p2 = Livro("Como Eu Era Antes De Você", "JoJo Moyes", 2012)

print("Informações do livro 1:")
p1.exibirInformacoes()  
p1.verificarIdadeLivro()

print("Informações do livro 2:")
p2.exibirInformacoes()  
p2.verificarIdadeLivro()