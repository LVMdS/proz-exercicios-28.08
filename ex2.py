try:
    alvo = 12
    chute = int(input("Digite um número de 0 a 100: "))

    if chute == alvo:
        print("Parabéns, você acertou!")
    else:
        if chute < alvo:
            print(f"Que pena, você errou! O número alvo é maior que {chute}. Melhor sorte na próxima!")
        else:
            print(f"Que pena, você errou! O número alvo é menor que {chute}. Melhor sorte na próxima!")
except ValueError:
    print("O número digitado deve ser um valor inteiro.")
