try:
    alvo = 12
    chute = int(input("Digite um numero de 0 a 100? "))

    if(chute == alvo):
        print ("Parabens voce acertou!")
    else:
        print ("Que pena! voce errou! melhor sorte na proxima")
except:
    print("O nimero digitado deve ser um valor inteiro")