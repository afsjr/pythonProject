# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone:
    def __init__(self):
        self.tamanho
        self.interface

    def ligar(self):
        print('ligando do telefone')

class Mp3Player(Smartphone):
    def __init__(self):
        Smartphone.__init__(self)
        print('Criado o objeto Smartphone')

    def tamanho(self):
        print(32)

    def interface(self):
        print('IOS')

    def tocar(self):
        print('tocando sua música favorita')

mp = Mp3Player()

mp.tamanho()
mp.interface()
mp.tocar()
mp.ligar()
