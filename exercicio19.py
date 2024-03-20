valor_compra = float(input("Digite o valor da sua compra: "))

if(valor_compra > 100):
    desconto_compra = (valor_compra * 0.10)
    valor_final = (valor_compra - desconto_compra)
    print(f"O valor do desconto é de R${desconto_compra}, o valor final da sua compra é de R${valor_final}")
else:
    print(f"O valor final da sua compra é de R${valor_compra}")


#Uma loja está com uma promoção de 10% desconto em compras acima de R$100. 
#Faça um programa que receba um valor, calcule e imprima o valor do desconto, se existir, e o valor final da compra.