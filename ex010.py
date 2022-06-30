#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
#dólares ela pode comprar.
#Considere US$ 1,00 = R$3,27

n = float(input('Quantos reais você tem na carteira? '))
dolar = n/3.27
print('Você poderá comprar {} dólares!'.format(dolar))
