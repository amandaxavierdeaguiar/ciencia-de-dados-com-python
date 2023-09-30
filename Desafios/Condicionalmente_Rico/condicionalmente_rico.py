# Entrada de dados
saldo_total = int(input())
valor_saque = int(input())

if (saldo_total >= valor_saque):
    resultado = saldo_total - valor_saque
    print('Saque realizado com sucesso. Novo saldo:', resultado)
elif (valor_saque > saldo_total):
    print ('Saldo insuficiente. Saque nao realizado!')

