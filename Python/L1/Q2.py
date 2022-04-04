from os import system


preco = float(input("Digite o valor \n"))
validN = False
while validN == False:
    system("cls")
    print("Selecione um método de pagamento")
    print(f"À vista em dinheiro ou cheque(15% de DESCONTO) | 1")
    print(f"À vista no cartão de crédito(10% de DESCONTO)  | 2")
    print(f"Em duas vezes(Sem desconto)                    | 3")
    print(f"Em três vezes(10% de JUROS)                    | 4")
    metodo = int(input(">"))
    if metodo >= 1 and metodo <= 4:
        validN = True
if metodo == 1:
    print(f"O valor a ser pago é R${preco*0.85:,.2f}")
elif metodo == 2:
    print(f"O valor a ser pago é R${preco*0.90:,.2f}")
elif metodo == 3:
    print("O valor a ser pago é ", preco)
else:
    print(f"O valor a ser pago é R${preco*1.10:,.2f}")