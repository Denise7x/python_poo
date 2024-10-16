from pessoa import Pessoa, Aluno, Professor

pessoa1 = Pessoa("Denise", 17)
aluno1 = Aluno ("Joana", 16, 987)
professor = Professor ("Gilson", 56, "Matemática")

pessoa1.info()
aluno1.info()
aluno1.estudar()
professor.ensinar()