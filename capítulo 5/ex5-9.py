user = []

for user in user:
    if user == 'admin':
        print('ola ' + user + ' gostaria de um relatorio do status?')
    elif user:
        print('ola ' + user + ', obrigada por fazer o login')
    else:
        print('precisamos encontrar alguns usuarios')