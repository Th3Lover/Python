x = int( input ("Digite um numero: "))

u = x // 1 % 10
d = x //10 % 10
c = x //100 % 10
m = x //1000 % 10

print ("Analisando o Número {}".format(x)) 
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
