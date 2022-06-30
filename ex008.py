# Escreva um programa que leia um número em metros e o exiba convertido em centímetros e milímetros:

n = int(input('Digite um valor em metros: '))
c = (n * 100)
m = (n * 1000)
print('O valor digitado é: {} \ncentímetros é {} \nmilímetros é {}'.format(n, c, m))
