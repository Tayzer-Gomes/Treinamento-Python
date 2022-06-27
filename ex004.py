# Faça um programa que leia algo pelo teclado e mostre o seu tipo primitivo e todas as informações possíveis.

n = input('Digite algo!')
print('O tipo primitivo é',type(n))
print('Só tem espaçoes?', n.isspace())
print('É alpha númerico?', n.isalnum())
print('É alfabético?', n.isalpha())
print('É um número?', n.isnumeric())
print('Está em maiúsculas?', n.isupper())
print('Está em minúsculas?', n.islower())
print('Está capitalizada?', n.istitle())

