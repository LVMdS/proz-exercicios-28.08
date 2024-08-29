import random

def adivinhacao():
    numero_alvo = random.randint(0, 100)
    tentativas = 5
    print("Bem-vindo ao jogo de adivinhação! Você tem 5 tentativas.")
    
    while tentativas > 0:
        try:
            chute = int(input(f"Digite um número inteiro entre 0 e 100 (Tentativas restantes: {tentativas}): "))
            
            if chute < 0 or chute > 100:
                print("Por favor, insira um número válido entre 0 e 100.")
            elif chute == numero_alvo:
                print("Parabéns! Você acertou o número!")
                return True
            else:
                if tentativas > 1:  # Não mostra a dica se for a última tentativa
                    if chute < numero_alvo:
                        print("Tente um número maior.")
                    else:
                        print("Tente um número menor.")
            
            tentativas -= 1
            
            if tentativas == 0:
                print(f"Suas tentativas acabaram! O número sorteado era {numero_alvo}.")
                return False
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def jogo():
    vitorias = 0
    derrotas = 0
    
    while True:
        ganhou = adivinhacao()
        if ganhou:
            vitorias += 1
        else:
            derrotas += 1
        
        print(f"Vitórias: {vitorias} | Derrotas: {derrotas}")
        
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar!")
            break

jogo()
