class Livro: 
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def exibirInformacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de publicação: {self.ano_publicacao}")

    def verificarIdadeLivro(self):
        idade_livro = 2024 - self.ano_publicacao
        if idade_livro > 50:
            print("Este livro é um clássico")
        else:
            print("Ainda não é considerado um clássico")
