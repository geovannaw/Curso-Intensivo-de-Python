pizzas = ['calabresa', 'frango', 'queijo']
friend_pizza = pizzas[:]
pizzas.append('portuguesa')
friend_pizza.append('romanesca')
for pizzas in pizzas:
    print('minhas pizzas favoritas sao: ', pizzas)
for friend_pizza in friend_pizza:
    print('as pizzas favoritas dos meus amigos sao: ', friend_pizza)
