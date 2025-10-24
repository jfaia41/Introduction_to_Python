# assignment_#2: bitcoin.py

# Precisamos de "sys.argv" para ler argumentos da linha de comandos e "sys.exit" para terminar o programa com mensagem de erro quando necessário.
# Usamos a biblioteca "requests" para fazer a ligação HTTP à API da CoinCap e obter o preço da Bitcoin.

import sys # importar módulo padrão do Python, que dá acesso a funcionalidades e variáveis do próprio sistema (da execução do Python). O nome “sys” vem de system.
import requests  # biblioteca externa (não vem com o Python por defeito) que serve para enviar pedidos HTTP — ou seja, comunicar com APIs e sites na Internet.

API_URL = "https://rest.coincap.io/v3/assets/bitcoin"
API_KEY = "4cc28730e2749f8b1433aef4a51c03e902f4263e15e5fb986fe639c9f30cced2"

# Definir a função principal:

def main():
    # 1) Ler e validar o argumento da linha de comandos (número de Bitcoins)
    if len(sys.argv) != 2:  # Comprimento da lista = 2 (Lista é composta por dois elementos: 1. Nome do ficheiro 2. O valor dado ao programa)
        sys.exit("Missing command-line argument")  # Esperamos exatamente um argumento além do nome do ficheiro: a quantidade N de Bitcoins. Se não vier, mostramos instruções de uso e terminamos: N = quantidade de Bitcoins

## Tentamos converter sys.argv[1] para float. Se o utilizador escrever algo não numérico (ex.: "abc"), float(...) lança ValueError.

    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # 2) Pedir o preço da Bitcoin à API da CoinCap
    try:

        response = requests.get(
            API_URL,
            headers={"Authorization": f"Bearer {API_KEY}"},  # Bearer token = “chave que o portador apresenta para provar que tem autorização”.
            timeout=10 # evitar que o programa fique preso indefinidamente.
        )
        response.raise_for_status()  # levanta exceção se o status HTTP não for 2xx. Ou seja, for diferente do sucesso

    except requests.RequestException as e: # "RequesteException" é a classe base de erros. Ou seja, engloba todo o tipo de eros
        sys.exit(f"Erro ao contactar a API: {e}")

    # 3) Extrair o preço (priceUsd) do JSON
    try:
        data = response.json() # converte o corpo da resposta para um dict Python
        price_usd = float(data["data"]["priceUsd"])   # priceUsd vem como string (ex.: "97845.0243..."), convertemos para float

    except (ValueError, KeyError, TypeError):
        sys.exit("Erro: resposta da API inesperada (não foi possível obter priceUsd).")

    # 4) Calcular o custo total e imprimir formatado
    total = n * price_usd

    # Formato: USD com vírgula como separador de milhar e 4 casas decimais
    print(f"${total:,.4f}")

if __name__ == "__main__":  # “Se este ficheiro está a ser executado diretamente (e não importado), então chama a função main().”
    main()
