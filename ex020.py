import random

n1 = input('Nome do primeiro aluno:')
n2 = input('Nome do segundo aluno:')
n3 = input('Nome do terceiro aluno:')
n4 = input('Nome do quarto aluno:')

x = [n1, n2, n3, n4]

y = random.shuffle(x)

print('A ordem de apresentação do trabalho sera: {}'.format(x))
