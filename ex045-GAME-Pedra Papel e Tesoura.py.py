import random
jogo = ["PEDRA", "PAPEL", "TESOURA"]
n1 = str(input("Escolha Pedra, Papel ou Tesoura !\n")).strip().upper()
n2 = random.choice(jogo)

if n1 == n2:
    print(f"Voce Empatou, o computador tambem escolheu: {n2}")

if (n1 == "PEDRA" and n2 == "PAPEL") or (n1 == "PAPEL" and n2 == "TESOURA") or (n1 == "TESOURA" and n2 == "PEDRA"):
    print(f"Voce perdeu, {n1} perde para {n2}")

elif (n2 == "PEDRA" and n1 == "PAPEL") or (n2 == "PAPEL" and n1 == "TESOURA") or (n2 == "TESOURA" and n1 == "PEDRA"):
    print(f"Voce GANHOU, {n1} ganha de {n2}")
