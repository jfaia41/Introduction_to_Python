# assignment_#2: lines.py

import sys

def main():
    # 1) Validar nº de argumentos
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    # 2) Verificar extensão .py
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # 3) Abrir ficheiro (ou sair se não existir)
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    # 4) Contar linhas de código (exclui linhas em branco e comentários que começam com #)
    count = 0
    for line in lines:
        stripped = line.lstrip()  # remove espaços à esquerda (mantém docstrings como código)
        if stripped == "" or stripped == "\n":     # linha vazia
            continue
        if stripped.startswith("#"):               # comentário
            continue
        count += 1

    # 5) Imprimir total
    print(count)

if __name__ == "__main__":
    main()
