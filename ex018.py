import math

x = float( input('Digite um angulo: '))

y = math.cos(math.radians(x))
z = math.sin(math.radians(x))
a = math.tan(math.radians(x))

print('Os valor dos angulos são: cosseno: {:.2f}, seno: {:.2f} e tangente: {:.2f}'.format(y,z,a))