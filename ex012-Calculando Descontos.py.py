preco = eval(input('Digite o preço do produto: '))
desconto = preco * 0.05
final = preco - desconto
print(f'O desconto é de R${desconto:.2f} e o total da compra fica em R${final:.2f}')