respostas = {}
chave = True

while chave:
    nome = input("\nQual é o seu nome?  ")
    lugar = input("Se pudesse visitar um lugar do mundo, para onde você iria? ")

    respostas[nome] = lugar

    repetir = input("Você gostaria de deixar outra pessoa responder (sim|não)? ")
    if repetir.lower() == 'não' or repetir.lower() == 'nao':
        chave = False

print("\n--- Resultado da enquete ---\n")
for nome, lugar in respostas.items():
    print(nome.title() + " iria para: " + lugar.title() + ".")