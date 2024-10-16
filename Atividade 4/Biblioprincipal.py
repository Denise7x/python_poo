from biblioteca import Livro, Revista

def criar_biblioteca(): 

    l1 = Livro("O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 1954, 576)
    l2 = Livro("Orgulho e Preconceito", "Jane Austen", 1813, 580)
    
   
    r3 = Revista("Quatro Rodas", "Desconhecido", 2004, 100)
    
    
    print("\nInformações do Livro 1:")
    l1.informacoes()

    print("\nInformações do Livro 2:")
    l2.informacoes()

    print("\nInformações da Revista:")
    r3.informacoes()

# Executando a função para criar a biblioteca
if __name__ == "__main__":
    criar_biblioteca()

