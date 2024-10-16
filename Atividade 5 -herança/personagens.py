class Personagem:
    def __init__(self, nome, vida=100, rank="Novato"):
        self._nome = nome
        self._vida = vida
        self._rank = rank
        
    def receberDano(self, dano):
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0

    def verificarVida(self):
        if self._vida > 0:
            print(f"{self._nome} está vivo")
        else:
            print(f"{self._nome} está morto")
    
    def detalhes(self):
        print(f"Nome: {self._nome}, Vida: {self._vida}, Rank: {self._rank}")


class Heroi(Personagem):
    def __init__(self, nome, vida=100, rank="Novato", identidade="", energia=50, poder=""):
        super().__init__(nome, vida, rank)
        self._identidadeSecreta = identidade
        self._energia = energia 
        self._poder = poder
    def executarHabilidade(self, tipoHabilidade):
        energia_consumo = 10  # Pode ser ajustado
        if self._energia >= energia_consumo:
            self._energia -= energia_consumo
            print(f"{self._nome} utilizou a habilidade {tipoHabilidade} Consumiu {energia_consumo} de energia")
        else:
            print(f"{self._nome} não tem energia suficiente para utilizar {tipoHabilidade}")

    def recarregarEnergia(self):
        energia_aumentar = 10  # Pode ser ajustado
        self._energia += energia_aumentar
        print(f"{self._nome} recarregou {energia_aumentar} de energia. Energia atual: {self._energia}.")

    def detalhes(self):
        super().detalhes()
        print(f"Identidade Secreta: {self._identidadeSecreta}, Energia: {self._energia}, Poder: {self._poder}")


class Vilao(Personagem):
    def __init__(self, nome, vida=100, rank="Novato", malicia=70):
        super().__init__(nome, vida, rank)
        self._malicia = malicia

    def desferirGolpe(self, tipoGolpe):
        malicia_consumo = 10  # Pode ser ajustado
        if self._malicia >= malicia_consumo:
            self._malicia -= malicia_consumo
            print(f"{self._nome} desferiu o golpe: {tipoGolpe} potencializado pela malícia e consumiu {malicia_consumo} de malícia.")
        else:
            print(f"{self._nome} não tem malícia suficiente para desferir {tipoGolpe}!")

    def detalhes(self):
        super().detalhes()
        print(f"Malícia: {self._malicia}")
