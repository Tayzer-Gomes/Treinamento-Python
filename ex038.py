#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

num = int(input('Digite o primeiro número:'))
num1 = int(input('Digite o segundo número:'))
if (num > num1):
    print('O primeiro valor é maior.')
elif(num < num1):
    print('O segundo número é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
