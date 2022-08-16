# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.


reta1 = int(input('Digite o primeiro valor:'))
reta2 = int(input('Digite a segundo valor:'))
reta3 = int(input('Digite o terceiro valor'))
if reta1 == reta2 and reta2 == reta3:
    print('Suas retas formam um triângulo equiláteros!')
if reta1 != reta2 and reta2 != reta3:
    print('Suas retas formam um triângulo escaleno!')
if reta1 == reta2 and reta1!= reta3:
    print('Suas retam formam um triângulo isóceles!')
