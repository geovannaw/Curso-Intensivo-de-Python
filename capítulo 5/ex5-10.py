current_users = ['geo', 'yan', 'estela', 'tiago', 'guilherme']
new_users = ['geo', 'leticia', 'pedro', 'jose', 'paulo']

for new_users in new_users:
    if new_users in current_users:
        print('forneca um novo nome')
    else: 
        print('o nome de usuario esta disponivel')