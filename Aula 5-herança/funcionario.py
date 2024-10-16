class Funcionario:
    def __init__(self, nome, salario):
        #estamos mudando a visibilidade dos atributos de privado para protegido, dessa forma, as classes filhas poderão acessar os atributos da classe mãe
        self._nome = nome
        self._salario = salario

    def informacoes(self):
        print(f"Olá {self._nome}, seu salário é {self._salario}")

#CRIANDO CLASSES FILHAS
class Engenheiro(Funcionario): # A classe Engenheiro está herdando se características da classe Funcionario, que será sua classe mâe
    def bonusEngenheiro(self):
        self._salario = self._salario = 1.1 #estamos aumentando o salário em 10%


class Supervisor(Funcionario):
    def relatorio(self):
        print(f"O relatório do funcionário {self._nome} está correto e adequado")