#Faça um algorítmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite seu salário: '))
ns = (s * (15/100)) + s
print('Seu novo salário é: {} reais'.format(ns))
