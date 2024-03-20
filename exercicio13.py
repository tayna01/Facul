import random

valor = random.randint(1, 10)
print(valor)

valor_usuario = int(input("Digite um número: "))

if(valor_usuario == valor):
    print("Você acertou o número sorteado!")
else:
    print("Você errou o número sorteado!") 



#Faça um programa que gera um número aleatório entre 1 e 10. Em seguida, peça para o usuário digitar um número. Se ele acertar, apresente na tela “Acertou”, se não, “Errou”.
