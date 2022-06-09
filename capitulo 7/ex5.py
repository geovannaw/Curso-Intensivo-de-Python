idade = input("digite sua idade ou 'quit' para sair: ")

while idade != 'quit' :
    idade = int(idade)
    if idade < 3 :
            print('ingresso gratuito')
            break
    elif (idade >= 3) and (idade<= 12) :
            print('pague 10 dolares')
            break
    else:
            print('pague 15 dolares')
            break
   