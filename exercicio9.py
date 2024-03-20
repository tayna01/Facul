idade = int(input("Digite sua idade: "))

if idade >= 18:
    salario = float(input("Digite seu salário: "))
    salario_com_aumento = ((salario * 0.05) + salario)
    print("Seu salário com aumento de 5% é:", salario_com_aumento)
else:
    print("Cálculo não permitido")