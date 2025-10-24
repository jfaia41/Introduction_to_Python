#Assignment_#2: taqueria.py

# Criar um menu, com itens e preços:
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0.0  #definir total a começar em 0. Depois vai somando o price

# Loop para introdução de itens do menu:
while True:
    try:
        item = input("Item: ").strip()   #.strip() ignora espaços em branco
    except EOFError:          # Move o cursor para a linha seguinte ao terminar com Ctrl-D
        print()
        break

    if not item:
       continue                # ignora linhas vazias

    # Normaliza a entrada para "Title Case", porque o menu está nesse formato
    item_norm = item.title()

    # .get evita KeyError se o item não existir; devolve None por omissão
    price = menu.get(item_norm)

    if price is not None:
        total += price    # equivale a total = total + price
        # Mostra o total acumulado, com $ e duas casas decimais
        print(f"${total:.2f}")
    # Caso contrário, ignora entradas que não estejam no menu
