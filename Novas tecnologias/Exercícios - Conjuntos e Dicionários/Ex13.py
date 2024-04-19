"""Crie uma lista chamada sandwich_orders e a preencha com os nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada 
finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e mostre uma mensagem para cada pedido, por exemplo, Preparei seu 
sanduíche de atum. À medida que cada sanduíche for preparado, transfira o para a lista de sanduíches prontos. Depois que todos os sanduíches 
estiverem prontos, mostre uma mensagem que liste cada sanduíche preparado"""

sandwich_orders = ["Atum", "Frango", "Presunto e Queijo", "Vegetariano"]

finished_sandwiches = []

while sandwich_orders:
    pedido = sandwich_orders.pop(0)  
    print("Preparei seu sanduíche de " + pedido + "...")
    finished_sandwiches.append(pedido) 

print("\nSanduíches prontos:")
for sanduiche in finished_sandwiches:
    print(sanduiche)
