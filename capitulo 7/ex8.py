sandwich_orders = ['bauru', 'pastrami', 'vada pav', 'bauru', 'roti john',
                   'pastrami', 'bánh mì', 'katsu-sando', 'pastrami']

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("Preparei seu sanduíche de " + sandwich.title())
    finished_sandwiches.append(sandwich)

print("\nSanduíches terminados: ")

for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())
