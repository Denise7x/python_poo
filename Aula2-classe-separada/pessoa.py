class Pessoa: 
    #Método Construtor
    def __init__(self, nome, hobby, endereco):
        self.nome = nome
        self.hobby = hobby
        self.endereco = endereco

    #Criando Métodos
    def exibirMooby(self):
        print(f"Olá, meu hobby atual é {self.hobby}")

    def mudarMooby(self, novohobby):
        self.hobby = novohobby
        print(f"Meu hobby foi mudado para {novohobby}")
        