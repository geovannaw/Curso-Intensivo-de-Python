def make_album(Artista,TituloAlbum,QuantFaixas = 0):
    if QuantFaixas != 0:
        album = {'Nome do Artista':Artista,'Titulo do Album':TituloAlbum,'Quantidade de Faixas':QuantFaixas}
    else:
        album = {'Nome do Artista': Artista, 'Titulo do Album': TituloAlbum}
    return album