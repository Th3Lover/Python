x = int(input('quantos dias o carro foi alugado:'))
z = float(input('Quantos Km rodados com o carro:'))

a = (x * 60) + (z * 0.15)


print('O total a pagar é: {:.2f}'.format(a))