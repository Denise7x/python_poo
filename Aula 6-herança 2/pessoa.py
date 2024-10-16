class Pessoa: #superclasse ou class mae
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def info(self):
        print (f"Nome: {self._nome} Idade: {self._idade}")

#Classe filha 1 - Aluno
# pass para informar que nao vai progamar nada por enquanto, ignora possiveis erros
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade) #utilizando o construtor a classe mãe
        self._matricula  = matricula #estamos utilizando um atributo exclusivo da classe filha

    def estudar(self):
        print(f"{self._nome}, está matriculado com o código {self._matricula} e continua estudando normalmente.")

#Classe filha 2 - Professor
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self._disciplina = disciplina

    def ensinar(self):
        print(f"{self._nome}, professor(a) da disciplina {self._disciplina}, está ensinando.")