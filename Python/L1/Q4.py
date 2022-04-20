base = int(input("Insira a base"))
expoente = int(input("Insira o expoente"))

for i in range(1, expoente, +1):
    base = base * expoente

print(base)