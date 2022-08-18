#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros

preco = float(input('Digite o valor:'))
opcao = input('''Escolha uma opção:
[1] - Dinheiro ou cartão: 10% de desconto.
[2] - à vista no cartão: 5% de desconto.
[3] - 2 vezes no cartão: preço formal.
[4] - 3 vezes ou mais no cartão: 20% de juros.\n''')

if opcao == '1':
    pagamento = preco - (10/100) * preco
elif opcao == '2':
    pagamento = preco - (5/100) * preco
elif opcao == '3':
    pagamento = preco
else:
    pagamento = preco + (20/100) * preco
print('O preço a pagar é R$ {:.2f}!'.format(pagamento))
