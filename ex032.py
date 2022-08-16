#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date # pega data atual do pc
ano = int(input('Digite o ano:'))
'''if ano == 0:
    ano = date.today().year'''#Pega somente o ano
if ano%4 == 0 and ano%100 !=0 or ano%400 == 0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
