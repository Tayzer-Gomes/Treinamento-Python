# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
n1 = input('Digite o nome 1:')
n2 = input('Digite nome 2: ')
n3 = input('Digite nome 3: ')
n4 = input('Digite nome 4: ')
resultado = random.choice([n1, n2, n3, n4],)
print('O aluno(a) sorteado é: {}'.format (resultado))


