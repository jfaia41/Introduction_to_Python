# Custo da coca-cola = 50
cost = 50

# Conta = custo
acount = cost

# Calcular o troco
while acount > 0:
    print (f"Amount Due: {acount}")
    money = int(input("Insert Coin:"))
    

# Só aceita moedas de 25, 10, ou 5

    if money in [25, 10, 5]:
        acount-=money

    else:
        print("Invalid coin. Please insert 25, 10, or 5.")

# Indicar o valor do troco
## Variável troco

change = 0
if acount < money:
    change = abs(acount)
    print(f"Change Owed: {change}")