#Crie um programa que faça o computador jogar Jokenpô com você.
import  random
pc = random.randint(1, 3)
jogo = input('''Escolha sua opção:
[1] - Pedra
[2] - Papel
[3] - Tesoura\n''')
if jogo != '1' != '2'!= '3:':
    print('Jogada inálida!')
elif pc == 1 and jogo == '2':
    print('Você ganhou!')
elif pc == 1 and jogo == '3':
    print('Você perdeu!')
elif pc == 2 and jogo == '1':
    print('Você perdeu!')
elif pc == 2 and jogo == '3':
    print('Você ganhou!')
elif pc == 3 and jogo == '1':
    print('Você ganhou!')
elif pc == 3 and jogo == '2':
    print('Você perdeu!')
else:
    print('Empatou!')
print('A minha opção foi {} e a sua foi {}.'.format(pc, jogo))