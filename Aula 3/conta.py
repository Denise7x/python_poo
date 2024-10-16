class Conta:
    def __init__(self,numero,titular,saldo,limite=200):

    #Estamos passando um valor padrão para o limite, tornando-o opcional, dessa forma o objetoao ser criado pode ter um limite ou não
    #Quando colocamos 2 underline antes do atributo, indicamos que esse atributo está com a visibilidade "privado", o ocntrário significa que está público
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def relatorio(self):
        print(f"Olá {self.__titular} seu saldo é {self.__saldo} e o seu limite atual é de {self.__limite}")

    def getLimite(self):
        return self.__limite

    def setLimite(self, valor):
        if valor < 0:
            print("Informe um valor válido")
        else:
            self.__limite = valor

    def depositar(self, valor):
        if valor <= 0:
            print("Informe um valor positivo")

        else:
            self.__saldo = self.__saldo + valor

    def sacar(self, valor):
        if valor <= 0 or valor > self.__saldo:
            print("Saldo insuficente ou valor negativo solicitado")