from conta import Conta

minhaConta = Conta(321, "Epamenondas Soares", 2000)

minhaConta.relatorio()

minhaConta.setLimite(8000)
minhaConta.relatorio() 

print(f"Seu limite atual é {minhaConta.getLimite()}")

minhaConta.depositar(200)
minhaConta.relator()
minhaConta.sacar(150)
minhaConta.relator()