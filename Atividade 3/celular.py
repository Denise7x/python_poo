class Celular: 
    def __init__(self, numero, saldo=0, plano="pré-pago"):
        self.__numero = numero
        self.__saldo = saldo
        self.__plano = plano
        self.__valorMinuto = 1.50

    @property
    def plano(self):
        return self.__plano

    @plano.setter
    def plano(self, novo_plano): 
        self.__plano = novo_plano

    def recarregar(self, valor):
        if self.__plano == "pré-pago":
            self.__saldo += valor

    def fazerChamada(self, duracao_minutos):
        custo = duracao_minutos * self.__valorMinuto
        if self.__plano == "pré-pago":
            if self.__saldo >= custo:
                self.__saldo -= custo
            else:
                print("Saldo insuficiente para a chamada.")
        else:
            print(f"Chamada de {duracao_minutos} minutos. O valor será cobrado no final do mês: R$ {custo:.2f}")

    def exibir_dados(self):
        print(f"O número de celular é: {self.__numero}, seu plano é {self.__plano} e seu saldo é de: R$ {self.__saldo:.2f}")           
