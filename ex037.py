#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases de conversão:
[1] converter para binário:
[2] converter para octal:
[3] converter para hexadecimal:''')
opcao = int(input('Escolha sua opção:'))
if (opcao == 1):
    print('O numéro {} convertido para binário é {}.'.format(num, bin(num)[2:]))
elif (opcao == 2):
    print('O número {} convertido para octal é {}.'.format(num, oct(num)[2:]))
elif (opcao == 3):
    print('O número {} convertido para hexadecimal é {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente!')

