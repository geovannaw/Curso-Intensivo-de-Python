def describe_city(cidade,pais='Pais nao definido'):
    result = f'{cidade} esta localizada em {pais}'
    return result
print(describe_city('Foz do Iguacu','Brasil'))
print(describe_city('los angeles','EUA'))
print(describe_city('italia'))