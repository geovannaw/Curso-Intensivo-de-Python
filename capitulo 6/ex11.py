cities = {
    'Foz do Iguacu' : {'Pais' : 'Brasil', 'Populacao' : '165.500',
        'fato' : 'tem a itaipu',},
    'Santa Terezinha' : {'Pais' : 'Brasil', 'Populacao' : '10.000',
        'fato' : 'Tem a FESPOP',},}

for name, info in cities.items():
    print("\nCidade: " + name.title())
    print("- País: " + info['Pais'].title())
    print("- População: " + info['Populacao'])
    print("- Definição: " + info['fato'].title())