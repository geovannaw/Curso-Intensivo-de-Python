def make_great(ListaDeMagicos):
    contador = 0
    for Magico in ListaDeMagicos:
        ListaDeMagicos[contador] = 'O Grande ' + Magico
        contador += 1

def show_magicians(ListaDeMagicos):
    contador = 1
    for Magico in ListaDeMagicos:
        print(f'Magico {contador} = {Magico}')
        contador += 1
    return 0

Lista = ['Tiago','Estela','Pavan','Geovanna']
Lista2 = Lista[::]
make_great(Lista2)
print('Lista 1')
print(f'{show_magicians(Lista)}')
print('Lista 2')
print(f'{show_magicians(Lista2)}')