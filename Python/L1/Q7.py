nomes = []
for i in range(0, 5, +1):
    print("Insira um nome(", i, "de 5 )")
    nomes.append(input(">"))
for i in range(0, 5, +1):
    print(nomes[i])
print("Reverso:")
nomes.reverse()
for i in range(0, 5, +1):
    print(nomes[i])