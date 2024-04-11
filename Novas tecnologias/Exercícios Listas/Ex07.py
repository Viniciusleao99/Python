""" Escreva um jogo da velha para dois jogadores. O jogo deve perguntar onde 
você quer jogar e alternar entre os jogadores. A cada jogada, verifique se a 
posição está livre. Verifique também quando um jogador venceu a partida. 
Um jogo da velha pode ser visto como uma lista de 3 elementos, na qual 
cada elemento é outra lista também com três elementos."""

tabuleiro = [[" "]*3 for _ in range(3)]

jogador_atual = "X"

while True:
  
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)
    
    linha = int(input(f"Jogador {jogador_atual}, escolha a linha (1-3): ")) - 1
    coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (1-3): ")) - 1
    
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador_atual
    else:
        print("Essa posição já está ocupada. Escolha outra.")
        continue

    for i in range(3):
        if all(tabuleiro[i][j] == jogador_atual for j in range(3)) or \
           all(tabuleiro[j][i] == jogador_atual for j in range(3)):
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break

    if all(tabuleiro[i][i] == jogador_atual for i in range(3)) or \
       all(tabuleiro[i][2-i] == jogador_atual for i in range(3)):
        print(f"Parabéns! Jogador {jogador_atual} venceu!")
        break
    
    if all(tabuleiro[i][j] != " " for i in range(3) for j in range(3)):
        print("Empate!")
        break
    
    jogador_atual = "O" if jogador_atual == "X" else "X"