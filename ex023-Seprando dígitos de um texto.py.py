n = input("Número: ")
variavel = 4-len(n)
novo = n.replace(n, "0"*variavel+n)
print("Unidade: ", novo[3])
print("Dezena: ", novo[2])
print("Centena: ", novo[1])
print("Milhar: ", novo[0])

