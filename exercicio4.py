nota_trabalho = float(input("Digite a nota do trabalho: "))
nota_prova = float(input("Digite a nota da prova: "))


if (0 <= nota_trabalho <= 100 and 0 <= nota_prova <= 100):
    
    media = (nota_trabalho + nota_prova) / 2

    if media >= 60:
        print("Aprovado")
    else:
        print("Reprovado")
else:
    print("As notas devem estar entre 0 e 100")






#Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100). Se a média aritmética das notas for maior ou igual a 60, escreva “Aprovado”, senão, “Reprovado”.