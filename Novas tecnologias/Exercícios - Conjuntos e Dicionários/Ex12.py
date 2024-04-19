"""Crie vários dicionários, em que o nome de cada dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua o tipo do animal e o 
nome do dono. Armazene esses dicionários em uma lista chamada pets. Em seguida, percorra sua lista com um laço e, à medida que fizer isso, 
apresente tudo que você sabe sobre cada animal de estimação."""

bella = {"tipo": "Cachorro", "nome dono": "Arthur"}
garfild = {"tipo": "Gato", "nome dono": "Vnicius"}
piu = {"tipo": "Passarinho", "nome dono": "Ana"}

pets = [bella, garfild, piu]

for pet in pets:
    print("\nInformações sobre o pet:")
    print("Tipo:", pet["tipo"])
    print("nome_dono:", pet["nome dono"])