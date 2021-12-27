# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.
class Pessoa():
    def __init__(self, nome='', cidade='', telefone=0, email=''):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return "%s mora em %s, possui o tel :%s e email %s" % (self.nome, self.cidade, self.telefone, self.email)

perso1 = Pessoa()

perso1.cidade = 'Limoeiro'
perso1.nome ='Adelino'
perso1.telefone = 81997551165
perso1.email = 'teste@teste.com'

print(perso1)