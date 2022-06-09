favorite_places = {
    'yan' : ['casa'],
    'geovanna' : ['eua'],
    'isa' : ['shopping'],}

for name, places in favorite_places.items():
    if len(places) > 1:
        print("\n" + name.title() + " lugar favorito e: ")

        for place in places:
            print("\t- " + place.title())

    else:
        print("\n" + name.title() + " lugar favorito e " +
              places[0].title()  + ".")