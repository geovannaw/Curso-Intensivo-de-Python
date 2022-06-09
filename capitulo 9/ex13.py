from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['Estela'] = 'C'
favorite_languages['Geo'] = 'Python'
favorite_languages['Pavan'] = 'Java'
favorite_languages['TIago'] = 'Pascal'

for name, lang in favorite_languages.items():
    print("linguagem favorita de", name, "é", lang)
