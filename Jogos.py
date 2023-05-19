print("Escolha Sua Opção de Jogo:")
print("[1] Jogo da Advinhação")
print("[2] Jogo da Forca")

jogo = int(input("Digite sua opcao: "))

if jogo == 1:
    print("Voce Escolheu o jogo da Advinhacao")
    import Jogo_Advinhacao
elif jogo == 2:
    print("Voce Escolheu o jogo da Forca")
    import Jogo_forca
else:
    print("Por Favor tente novamente")