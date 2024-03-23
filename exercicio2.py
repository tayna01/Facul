try:
    valorUm = int(input("Digite o primeiro valor inteiro: "))
    valorDois = int(input("Digite o segundo valor inteiro: "))

    if valorUm > valorDois:
        print(f"O maior numero é: {valorUm}")
    elif valorUm == valorDois:
        print(f"O primeiro valor é igual ao segundo valor")
    else:
        print(f"O maior numero é: {valorDois}")

except ValueError:
    print("Por favor, digite apenas números inteiros.")
