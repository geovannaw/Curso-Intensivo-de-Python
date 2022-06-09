favorite_numbers = {'Geovanna' : [7],
                    'Yan' : [7],
                    'Pavan' : [3, 2, 1, 41],
                    'Estela' : [13],
                    'Thiago' : [2, 5],}

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(name.title() + " numero(s) favorito(s) e " + str(numbers) + ".")

    else:
        print(name.title() + " numero(s) favorito(s) e " + str(numbers) + ".")