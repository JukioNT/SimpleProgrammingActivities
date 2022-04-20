numeros = []
end = False
while(end == False):
    numero = int(input("Insira os números (Para terminar digite 0) \n >"))
    if(numero == 0):
        end = True
    else:
        numeros.append(numero)

par = 0
impar = 0
media = 0
for i in range(0, len(numeros), +1):
    media += numeros[i]
    if(numeros[i] % 2 == 0):
        par += 1;
    else:
        impar += 1;

print("Media = ", media/len(numeros) )
print("Pares = ", par, "\nImpares = ", impar)