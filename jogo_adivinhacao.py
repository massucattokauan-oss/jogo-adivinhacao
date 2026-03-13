import random

def jogar():
    print("\nBem-vindo ao Jogo da Adivinhação!")
    print("Eu pensei em um número entre 1 e 100. Tente adivinhar!")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False
    
    while not acertou:
        try:
            palpite = int(input("\nQual é o seu palpite? "))
            tentativas += 1
            
            if palpite < 1 or palpite > 100:
                print("Ei, o número tem que ser entre 1 e 100! Tenta de novo.")
                continue
                
            if palpite < numero_secreto:
                print("Muito baixo! Tenta um número maior.")
            elif palpite > numero_secreto:
                print("Muito alto! Tenta um número menor.")
            else:
                acertou = True
                print(f"\nParabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
                
                if tentativas <= 5:
                    print("Nossa, você é muito bom nisso! 🔥")
                elif tentativas <= 10:
                    print("Boa! Mandou bem.")
                else:
                    print("Demorou um pouquinho, mas conseguiu! 😄")
                    
        except ValueError:
            print("Ops! Digite apenas números inteiros. Tenta de novo.")

# Loop principal do jogo inteiro
while True:
    jogar()  # Executa uma rodada completa
    
    while True:
        resposta = input("\nQuer jogar de novo? (s/n): ").strip().lower()
        if resposta in ['s', 'sim', 'y']:
            break  # Sai do loop interno e volta pro jogar()
        elif resposta in ['n', 'nao', 'não', 'no']:
            print("Valeu por jogar! Até a próxima! 👋")
            exit()  # Ou use return se estiver em função maior
        else:
            print("Digite 's' para sim ou 'n' para não.")