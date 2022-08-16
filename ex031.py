#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.


distancia = float(input('Qual a distância da sua viagem em Km?'))
if distancia <=200:
    preco = distancia * 0.50
    print('O valor cobrado da sua viagem será {:.2f} R$!'.format(preco))
else:
    preco1 = distancia * 0.45
    print('O valor cobrado da sua viagem será {} R$!'.format(preco1))