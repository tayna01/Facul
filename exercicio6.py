
salario_minimo = 1212.00
salario_usuario = float(input("Digite o seu salário: "))

if salario_usuario < salario_minimo:
        print("Você recebe menos que um salário mínimo.")
else:
    quantidade_salarios = salario_usuario / salario_minimo
    print(f"Você recebe {quantidade_salarios} salários mínimos.")

