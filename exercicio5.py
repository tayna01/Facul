

conceito = input("Digite o conceito da disciplina: ")

if conceito.isdigit():
    print("Por favor, digite apenas letras.")
else:
    conceito = conceito.upper()
    if conceito in ["A", "B", "C"]:
        print("Aprovado")
    else:
        print("Reprovado")









#Faça um programa que peça ao aluno o conceito dele na disciplina (A, B, C ou D). Se o conceito for A, B ou C apresente “Aprovado”, se não, apresente “Reprovado”.