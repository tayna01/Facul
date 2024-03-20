while True:
    numero = int(input("Digite um número inteiro: "))
    if numero >= 0:
        break
    else:
        print("Número negativo. Por favor, digite novamente.")

resultado = numero * 10
print(f"O resultado é: {resultado}")

