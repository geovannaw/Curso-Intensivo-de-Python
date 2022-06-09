def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo que sabemos sobre um usuário."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Tiago', 'Barboza Santos',Cidade='Foz do Iguacu',Idade='20',Curso='Sistemas de Informacao')
print(user_profile)