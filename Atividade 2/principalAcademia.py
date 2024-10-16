from Aluno import Aluno
aluno1 = Aluno("Pedro",19,68,1.78)
aluno2 = Aluno("Késia",23,54,1.60)

print("Dados do aluno 1:")
aluno1.exibir_dados()  
imc1 = aluno1.calcular_imc()
print(f"IMC do aluno 1: {imc1:}")


print("Dados do aluno 2:")
aluno2.exibir_dados()  
imc2 = aluno2.calcular_imc()
print(f"IMC do aluno 2: {imc2:}")