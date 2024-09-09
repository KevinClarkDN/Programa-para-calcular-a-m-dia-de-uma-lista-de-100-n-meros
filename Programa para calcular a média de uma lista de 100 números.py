# Programa para Calcular a Média de uma Lista de 100 Números

def calcular_media(numeros):
    """Calcula a média de uma lista de números."""
    return sum(numeros) / len(numeros)

def main():
    print("Bem-vindo ao programa de cálculo da média de 100 números!")
    numeros = []
    
    while len(numeros) < 100:
        try:
            entrada = input(f"Digite o número {len(numeros) + 1} de 100: ")
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
    
    media = calcular_media(numeros)
    print(f"\nA média dos 100 números inseridos é: {media:.2f}")

if __name__ == "__main__":
    main()