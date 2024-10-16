class Aluno: 
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = float(peso)
        self.altura = float(altura)

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}kg")
        print(f"Altura: {self.altura}m") 

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc 