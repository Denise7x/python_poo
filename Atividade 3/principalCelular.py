from celular import Celular

cliente1 = Celular(numero="123456789", plano="pré-pago")
cliente2 = Celular(numero="987654321", plano="pós-pago")


cliente1.recarregar(50)
cliente2.recarregar(30)  


cliente1.exibir_dados()
cliente2.exibir_dados()


cliente1.fazerChamada(10)  
cliente2.fazerChamada(5)    

cliente1.exibir_dados()
cliente2.exibir_dados()
