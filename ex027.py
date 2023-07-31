x = str ( input ("Digite seu nome completo:")).strip() # Pegando o nome e tirando os espaços 

z = x.split() # Repartindo o nome 

print (z[0]) # Pegando só a primeira parte do nome 

print (z[len(z)-1]) # Pegando a ultima parte do nome 