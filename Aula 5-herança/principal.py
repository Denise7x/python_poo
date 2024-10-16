from funcionario import Funcionario, Engenheiro, Supervisor

f1 = Funcionario("Joana", 3000)
engenheiro1 = Engenheiro("Koala", 3000)

f1.informacoes() 
engenheiro1.bonusEngenheiro()
engenheiro1.informacoes()

supervisor = Supervisor ("Vanessa", 300)
supervisor.relatorio()