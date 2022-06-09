rios = {'amazonas' : 'brasil', 
        'mississipi' : 'estados unidos',
        'danúbio' : 'alemanha',}

print()

for rio, pais in rios.items():
    if pais.lower() == 'alemanha':
        print("O " + rio.title() + " corre pela " + pais.title() + ".")
    else:
        print("O " + rio.title() + " corre pelo " + pais.title() + ".")

print()

for rio in rios.keys():
    print("- " + rio.title())

print()

for pais in rios.values():
    print("- " + pais.title())