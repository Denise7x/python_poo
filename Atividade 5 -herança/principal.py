from personagens import Personagem, Heroi, Vilao

heroi1 = Heroi ("Vortex", 170, "Lendário", "Valentina", 50, "Cura Acelerada")
vilao1 = Vilao  ("Risadão", 100, "Novato", 60)
personsagem_comum1 = Personagem ("Cyborg", 80, "Intermediário")

print("Detalhes do Herói:")
heroi1.detalhes()
heroi1.executarHabilidade("de regenerar rapidamente ferimentos, restaurar energia e imunizar contra doenças, permitindo curar a si mesmo e a aliados.")
heroi1.recarregarEnergia()
heroi1.verificarVida()
    
    
print("Detalhes do Vilão:")
vilao1.detalhes()
vilao1.desferirGolpe("Riso Tóxico")
vilao1.verificarVida()

    
print("Detalhes do Personagem Comum:")
personsagem_comum1.detalhes()
personsagem_comum1.receberDano(30)
personsagem_comum1.verificarVida()