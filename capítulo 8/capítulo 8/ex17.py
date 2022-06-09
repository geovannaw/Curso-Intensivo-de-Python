def describe_city(cidade,pais='Pais n definido'):
    result = f'{cidade} esta localizada em {pais}'
    return result


def make_album(Artista,TituloAlbum,QuantFaixas = 0):
    if QuantFaixas != 0:
        album = {'Nome do Artista':Artista,'Titulo do Album':TituloAlbum,'Quantidade de Faixas':QuantFaixas}
    else:
        album = {'Nome do Artista': Artista, 'Titulo do Album': TituloAlbum}
    return album


def Carro(modelo,outback,color,tow_packages):
    InfCarro = {'Modelo':modelo,'Outback':outback,'Color':color,'Tow Packages':tow_packages}
    return InfCarro