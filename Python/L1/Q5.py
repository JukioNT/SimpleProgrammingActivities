def potenciar(base, expoente):

    for i in range(1, expoente, +1):
        base = base * expoente

    return(base)

base = int(input("Insira a base"))
expoente = int(input("Insira o expoente"))

resultado = potenciar(base, expoente)

print(resultado)