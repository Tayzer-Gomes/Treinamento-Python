#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

#Só funciona em radiano por isso é necessário usar o comando rad = math.radians(angulo) para converter.

import math
angulo = float(input('Digite o ângulo em graus: '))
rad = math.radians(angulo)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print('O angulo digitado foi: {}\nSeu seno é: {:.2f}\nSeu cosseno é: {:.2f}\nSua tangente é: {:.2f}'.format(angulo, seno, cosseno, tangente))