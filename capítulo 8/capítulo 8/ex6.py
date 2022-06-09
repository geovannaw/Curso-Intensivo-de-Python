def city_country(cidade,pais):
    result = cidade.title() + ', ' + pais.title()
    return result

print(city_country('Foz do Iguacu','Brasil'))
print(city_country('los angeles','EUA'))
print(city_country('cancun','mexico'))