#Faça um jogo da Forca utilizando listas. Dada uma palavra, dê algumas chances para o usuário acertar.

palavra = "BANANA"

letras_corretas = []

max_tentativas = 6

while max_tentativas > 0:

    tentativa = input("Digite uma letra: ").upper().strip()
    
    if tentativa in palavra and tentativa not in letras_corretas:
        letras_corretas.append(tentativa)
        print("Letra correta!")
    elif tentativa not in palavra:
        max_tentativas -= 1
        print("Letra errada! Você tem", max_tentativas, "tentativas restantes.")
    
    if all(letra in letras_corretas for letra in palavra):
        print("Parabéns! Você adivinhou a palavra:", palavra)
        break

if max_tentativas == 0:
    print("Você perdeu! A palavra era:", palavra)