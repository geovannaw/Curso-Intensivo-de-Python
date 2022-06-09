favorite_languages = {
    'geovanna': 'python',
    'yan': 'c',
    'tiago': 'pascal',
    'estela': 'html',
    }

for name, language in favorite_languages.items():
    print(f"linguagem favorita do(a) {name.title()} e: {language.title()}.")

print("\n")

coders = ['pavan', 'tiago', 'luciano', 'yan']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"obrigada por responder a enquete, {coder.title()}!")
    else:
        print(f"{coder.title()}, qual sua linguagem de programacao preferida?")