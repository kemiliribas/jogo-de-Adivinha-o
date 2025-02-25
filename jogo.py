print("************")
print("Bem vindo ao Jogo de adivinhação!")
print("************")
numero secreto=69
total_de_tentativas=3
rodada=1
chute_str=input("dgite o seu numero:")
while (rodada<= total_de_tentativas):
    print("tentativas{} de {}".format(rodada,total_de_tentativas))  

print("voce digitou:",chute_str)
chute=int(chute_str)


acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Parabéns!Você acertou!")
    else:
        if(maior):
            print("O seu chute foi maior do que o numero secreto!")
        elif(menor):
            print("O seu chute foi menor do que o numero secreto!")

            rodada = rodada + 1

print("Fim do jogo")