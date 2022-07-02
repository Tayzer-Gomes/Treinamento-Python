#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pinta-lo, sabendo que cada litro de tinta,
# pinta uma área de 2 metros.

l = float(input('Qual a largura da parede em metros? '))
a = float(input('Qual a altura da parede em metros? '))
area = (l * a)
tinta = area/2
print('Sua área total é: {} e a quantidade de tinta necessária é: {} litros!'.format(area, tinta))

