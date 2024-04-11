"""Escreva um programa que controla a utilização das salas de um cinema.Imagine que a lista lugares_vagos=[10,2,1,3,0 contenha o número de  lugares vagos nas 
salas 1,2,3,4 e 5, respectivamente. Esse programa lerá o número da sala e a quantidade de lugares solicitados. Ele deve informar se é possível vender o número 
de lugares solicitados, ou seja, se ainda há lugares livres. Caso seja, possível vender os bilhetes, atualizará o número de lugares livres. A saída ocorre quando
se digita 0 no número da sala."""

lugares_vagos = [20, 3, 9, 5, 8]

while True:
    print("Temos 5 salas disponíveis")
    sala = int(input("Digite o número da sala ou digite 0 para sair: "))
    
    if sala == 0:
        print("Programa encerrado.")
        break
    
    if sala < 1 or sala > len(lugares_vagos):
        print("Sala inválida. Digite um número de sala válido.")
        continue
    
    print("Na sala", sala, "existem", lugares_vagos[sala - 1], "lugares vagos.")
    
    solicitados = int(input("Digite a quantidade de lugares solicitados: "))
    
    if solicitados <= lugares_vagos[sala - 1]:
        lugares_vagos[sala - 1] -= solicitados
        print("Bilhetes vendidos com sucesso! Lugares restantes na sala:", lugares_vagos[sala - 1])
    else:
        print("Não há lugares vagos suficientes na sala.")
