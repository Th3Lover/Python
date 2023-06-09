import math

x = float ( input ('Digite o valor do 1° cateto:'))
z = float ( input ('Digite o valor do 2° cateto:'))

h = math.hypot(x,z)
 
print('O valo da hipotenusa é: {:.2f}'.format(h))