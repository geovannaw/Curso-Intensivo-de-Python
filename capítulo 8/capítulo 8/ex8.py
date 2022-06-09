def make_album(Artista,TituloAlbum,QuantFaixas = 0):
    if QuantFaixas != 0:
        album = {'Nome do Artista':Artista,'Titulo do Album':TituloAlbum,'Quantidade de Faixas':QuantFaixas}
    else:
        album = {'Nome do Artista': Artista, 'Titulo do Album': TituloAlbum}
    return album

while True:
    NomeArt = input('Entre com o nome do artista: ')
    TitAlb  = input('Entre com o titulo do album: ')
    print(make_album(NomeArt,TitAlb))
    continuar = input('Deseja continuar(S/N)? ').upper()
    if continuar == 'N':
        print('Saindo')
        break
