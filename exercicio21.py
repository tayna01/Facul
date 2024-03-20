
valor_compra = float(input("Informe o valor da sua compra: "))

if(valor_compra > 500):

    forma_pagamento = (int(input("Informe a forma de pagamento: (1)PIX , (2)CARTÃO E (3)DINHEIRO")))

    if(forma_pagamento == 1):
        valor_desconto = (valor_compra * 0.10)
        valor_final = (valor_compra -  valor_desconto)
        print(f"O valor do desconto foi de R${valor_desconto:.2f}, com isso o valor final da sua compra é de R${valor_final:.2f}") 

    else:
        valor_desconto = (valor_compra * 0.05)
        valor_final = (valor_compra -  valor_desconto)
        print(f"O valor do desconto foi de R${valor_desconto:.2f}, com isso o valor final da sua compra é de R${valor_final:.2f}") 

else:
    print("Não há desconto para compras abaixo de R$500.")



#Uma loja está com uma promoção em compras acima de R$500. Acima desse valor, a loja oferece 10% de desconto se o cliente pagar por PIX ou 5% de desconto para outras 
#formas de pagamento. Por outro lado, para compras abaixo de R$500, a loja oferece apenas 5% de desconto se o pagamento for por PIX. 
#Faça um programa que receba um valor e a forma de pagamento, calcule e imprima o valor do desconto e o valor final da compra.