#Usando for
try:
    alvo = 12
    tentativas = 5

    for i in range(tentativas):
        chute = int(input(f"Tentativa {i+1}/{tentativas}: Digite um número de 0 a 100: "))

        if chute == alvo:
            print("Parabéns, você acertou!")
            break
        else:
            if chute < alvo:
                print(f"Que pena, você errou! O número alvo é maior que {chute}.")
            else:
                print(f"Que pena, você errou! O número alvo é menor que {chute}.")
            if i < tentativas - 1:
                print("Tente novamente.")
            else:
                print(f"Você esgotou todas as suas tentativas, o numero alvo era {alvo}")
except ValueError:
    print("O número digitado deve ser um valor inteiro.")


#Usando While 
"""
try:
    alvo = 12
    tentativas = 5
    chutes_dados = 0

    while chutes_dados < tentativas:
        chute = int(input(f"Tentativa {chutes_dados+1}/{tentativas}: Digite um número de 0 a 100: "))

        if chute == alvo:
            print("Parabéns, você acertou!")
            break
        else:
            if chute < alvo:
                print(f"Que pena, você errou! O número alvo é maior que {chute}.")
            else:
                print(f"Que pena, você errou! O número alvo é menor que {chute}.")
            
            chutes_dados += 1

            if chutes_dados < tentativas:
                print("Tente novamente.")
            else:
                print("Você esgotou todas as suas tentativas.")
except ValueError:
    print("O número digitado deve ser um valor inteiro.")
    
"""