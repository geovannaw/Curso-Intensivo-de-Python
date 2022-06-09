orders = ['bauru', 'pastrami', 'vada pav', 'bauru', 'roti john',
                   'pastrami', 'bánh mì', 'katsu-sando', 'pastrami']
finished = []

print(orders)

while 'pastrami' in orders:
    orders.remove('pastrami')
    print(orders)

print("\n- Hoje estamos sem Pastrami. Obrigado pela compreensão.\n")

while orders:
    sandwiches = orders.pop()
    print("Estamos preparando o seu sanduíche de " + sandwiches.title())
    finished.append(sandwiches)

print("\nSanduíches prontos: ")
for finish in finished:
    print(finish)