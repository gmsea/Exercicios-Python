print("Bem vindo a Loja !")
preco = float(input("Digite o preço do produto em R$ "))
pg = int(input("Como o voce deseja pagar?\n"
               "(1) - Á vista, dinheiro ou cheque: 10% off\n"
               "(2) - Á vista cartão: 5% OFF\n"
               "(3) - Parcelar em 2x: Preço normal\n"
               "(4) - Parcelar em 3x ou mais: 20% Juros\n"
               "Escolha uma das opções acima: "))
if pg == 1:
    pg1 = preco * 0.9
    print(f"Voce ganhou um desconto de 10% e o preço ficou em R${pg1:.2f}")
elif pg == 2:
    pg2 = preco * 0.95
    print(f"Voce ganhou um desconto de 5% e o preço ficou em R${pg2:.2f}")
elif pg == 3:
    pg3 = preco
    print(f"Voce ira parcelar 2x no crédito o valor de R${pg3:.2f}")
elif pg == 4:
    pg4 = preco * 1.2
    print(f"Voce optou por parcelar 3x ou mais e sera cobrado um acrescimo de 20% dando o valor total de R${pg4:.2f}")