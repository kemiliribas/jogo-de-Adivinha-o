print("************")
print("Bem vindo ao Jogo de adivinhação!")
print("************")

numero secreto=69

chute_str=input("dgite o seu numero:")
print("voce digitou:",chute_str)
chute=int(chute_str)

if(numero_secreto==chute):
    print("voce acertou!")
    else:
        print("voce errou!")
print("fim do jogo")