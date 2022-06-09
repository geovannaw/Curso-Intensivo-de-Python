def make_album(Artista,TituloAlbum,QuantFaixas = 0):
    if QuantFaixas != 0:
        album = {'Nome do Artista':Artista,'Titulo do Album':TituloAlbum,'Quantidade de Faixas':QuantFaixas}
    else:
        album = {'Nome do Artista': Artista, 'Titulo do Album': TituloAlbum}
    return album

print(f'Album 2: {make_album("geovanna","aaa")}')
print(f'Album 3: {make_album("Pavan","bbb")}')
print(f'Album 1: {make_album("estela","ccc",5)}')
print(f'Album 3: {make_album("yan","ddd",50)}')

