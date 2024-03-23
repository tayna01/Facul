salario_bruto = float(input("Informe o seu salário bruto: "))
salarioSemImposto = 1903.98
salarioComImposto = 2826.65

if salario_bruto <= salarioSemImposto:
    print("Não precisa pagar imposto de renda!")
elif salario_bruto <= salarioComImposto:
    imposto = salario_bruto * 0.075
    salario_liquido = salario_bruto - imposto
    print(f"O valor do imposto é de R${imposto:.2f}. O valor final é de R${salario_liquido:.2f}.")
else:
    imposto = salario_bruto * 0.15
    salario_liquido = salario_bruto - imposto
    print(f"O valor do imposto é de R${imposto:.2f}. O valor final é de R${salario_liquido:.2f}.")





#Faça um programa que calcule o valor de imposto a ser pago a partir de um salário bruto. Se o salário for um valor até R$1.903,98, a pessoa não precisa pagar imposto de renda. 
#Por outro lado, se o salário for menor que R$2.826,65 é cobrado 7,5% de imposto e se for maior, cobra-se 15%. Faça um programa que receba o salário bruto, 
#calcule e mostre o valor a ser pago.