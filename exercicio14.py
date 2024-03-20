import random

valorX = int(input("Digite um valor para X: "))
valorY = int(input("Digite um valor para Y: "))
valorXeY = int(input(f"Digite um valor entre {valorX} e {valorY}: "))

numero_aleatorio = random.randint(valorX, valorY)

if(numero_aleatorio == valorXeY):
    print("Acertou!!")
else:
    print(f"Errou o número sorteado foi {numero_aleatorio}")





#Faça um programa que gera um número aleatório entre X e Y. Para isso, peça para o usuário um valor para X, Y e um número entre X e Y. 
#Gere um valor aleatório entre X e Y e verifique se ele é igual ao número digitado pelo usuário. Se ele acertar, apresente na tela “Acertou”, se não, “Errou”.