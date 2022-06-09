pizza = 'peperonni'
print(pizza == 'peperonni')  #true
print(pizza == 'calabresa') #false

carro = 'Hrv'
print(carro == 'hrv') #false
print(carro.lower() == 'hrv') #true

idade = 20
print(idade>21) #false
print(idade<=20) #true

idade1 = 20
idade2 = 18
print(idade1>=20 and idade2<19) #true
print(idade1>21 or idade2<=18) #true

buffet = ['arroz', 'feijao']
print('arroz' in buffet) #true
print('macarrao' in buffet) #false
