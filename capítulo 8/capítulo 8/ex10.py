def make_great(ListaDeMagicos):
    contador = 0
    for Magico in ListaDeMagicos:
        ListaDeMagicos[contador] = 'O Grande ' + Magico
        contador += 1
    return 0

def show_magicians(ListaDeMagicos):
    contador = 1
    for Magico in ListaDeMagicos:
        print(f'Magico {contador} = {Magico}')
        contador += 1
    return 0
Lista = ['Tiago','Estela','Pavan','Geovanna']
make_great(Lista)
show_magicians(Lista)