#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Digite o preço do produto: '))
np = p - (5/100)
print('O novo valor com desconto é: {} reais!'.format(np))
