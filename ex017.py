#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.


import math
co = int(input('Digite o cateto oposto: '))
ca = int(input('Digite o cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa é {}'.format(hi))
