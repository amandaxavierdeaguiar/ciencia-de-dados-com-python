valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())


valor_final = valor_inicial * (1+taxa_juros)** periodo

print(f"Valor final do investimento: R$ {valor_final:.2f}")