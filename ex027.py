#Faça um programa que leia o nome completo de uma pessoa, 
#mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Qual seu nome?')).strip()
dividido = nome.split()
print('Seu primeiro nome é {}'.format(dividido[0]))
print('Seu sobrenome é {}'.format(dividido[len(dividido)-1]))








