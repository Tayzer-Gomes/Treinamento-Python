# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.


Km = float(input('Informe a quilometragem percorrida: '))
dias = int(input('Informe quantos dias de aluguel: '))
V_dia = dias * 60
rodado = Km * 0.15
preco = V_dia + rodado
print('O preço total a pagar é {}'.format(preco))
