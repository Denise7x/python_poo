from datetime import datetime

class Biblioteca:
    def __init__(self, titulo, autor, anoPublicacao, numeroPagina):
        self._titulo = titulo
        self._autor = autor
        self._anoPublicacao = anoPublicacao
        self._numeroPagina = numeroPagina

    def detalhes(self):
        print(f'Título: {self._titulo}, Autor: {self._autor}, Ano de Publicação: {self._anoPublicacao}')

    def calcularIdadeItem(self):
        ano_atual = datetime.now().year
        idade = ano_atual - self._anoPublicacao

        if idade > 70:
            return "muito antigo"
        elif 30 <= idade <= 70:
            return "recente"
        else:
            return "contemporâneo"


class Livro(Biblioteca):
    def verificarTamanho(self):
        if self._numeroPagina > 300:
            return "longo"
        else:
            return "curto"
            
    def informacoes(self):
        idade_classificacao = self.calcularIdadeItem()  # Corrigido para usar o método correto
        tamanho = self.verificarTamanho()
        print(f"O item '{self._titulo}', publicado em {self._anoPublicacao}, é considerado '{idade_classificacao}' e é um livro {tamanho} com {self._numeroPagina} páginas.")


class Revista(Biblioteca):
    def verificarEdicao(self):
        if self._anoPublicacao < 1998:
            return "é uma edição especial"
        else:
            return "não é uma edição especial"

    def informacoes(self):
        idade_classificacao = self.calcularIdadeItem()
        edicao = self.verificarEdicao()
        print(f"A revista '{self._titulo}', publicada em {self._anoPublicacao}, é '{idade_classificacao}' e {edicao}.")

