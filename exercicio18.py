numero = int(input("Digite um número inteiro: "))

if (numero > 0):
    if (numero % 2 == 0):
        print("O número é positivo e par.")
    else:
        print("O número é positivo e ímpar.")
elif (numero < 0):
    numero += 100
    print(f"O número é negativo. Adicionando 100, o resultado é: {numero}")
else:
    print("O número é zero.")




#Faça um programa para pedir um número inteiro. Se esse número for positivo, verifique e informe se ele é par ou ímpar. 
#Se ele for negativo, some 100 e apresente na tela.