"""Comece com o programa que você escreveu no Exercício 4. Crie dois novos dicionários que representem pessoas diferentes e armazene os três dicionários em uma
lista chamada people. Percorra sua lista de pessoas com um laço. À medida que percorrer a lista, apresente tudo que você sabe sobre cada pessoa"""

pessoa1 = {
    "first_name": "Vini",
    "last_name": "Leão",
    "age": 24,
    "city": "Goiânia"
}

pessoa2 = {
    "first_name": "Ana",
    "last_name": "Luiza",
    "age": 25,
    "city": "São Paulo"
}

pessoa3 = {
    "first_name": "Arthur",
    "last_name": "White",
    "age": 4,
    "city": "Brasília"
}

people = [pessoa1, pessoa2, pessoa3]

for pessoa in people:
    print("\nInformações pessoais:")
    print("Primeiro Nome:", pessoa["first_name"])
    print("Sobrenome:", pessoa["last_name"])
    print("Idade:", pessoa["age"])
    print("Cidade:", pessoa["city"])