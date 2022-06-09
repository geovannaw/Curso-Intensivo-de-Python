def Sanduiche(ListaDeItens):
    print('Os itens do sanduiche sao: ')
    return [d for d in ListaDeItens]
Lista = ["Pure","Batata","Carne"]
print(f'Sanduiche 1 = {Sanduiche(Lista)}')
Lista = ["Molho","Presunto","Mussarela"]
print(f'Sanduiche 2 = {Sanduiche(Lista)}')
Lista = ["Maionese","Mortadela"]
print(f'Sanduiche 3 = {Sanduiche(Lista)}')
