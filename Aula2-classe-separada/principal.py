#Estamos acessando o arquivo 'pessoa' e dentro desse arquivo estamos importando a classe `Pessoa`
from pessoa import Pessoa

#Criando Objetos
p1 = Pessoa("Joana","Correr", "Rua dos Alfinetes 2121")
p1.exibirhobby()
p1.mudarhobby("Natação")

#Solicitando dados do usuário
nomePessoa = input("Informe o nome da pessoa")
hobbyPessoa = input("Informe o hobby a pessoa: ")
endPessoa = input("Qual o endereço? ")

p2 = Pessoa(nomePessoa, hobbyPessoa, endPessoa)
p2.exibirHooby()