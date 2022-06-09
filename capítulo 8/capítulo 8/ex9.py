def show_magicians(ListaDeMagicos):
    contador = 1
    for Magico in ListaDeMagicos:
        print(f'Magico {contador} = {Magico}')
        contador += 1
    return 0
Lista = ['Tiago','Estela','Pavan','Geovanna']
show_magicians(Lista)