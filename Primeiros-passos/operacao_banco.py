conta_normal = True
conta_universitaria = False

saldo = 2200
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com o uso do cheque especial')
    else:
        print('Não foi possível realizar o saque, saldo insufiente.')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com o uso do cheque especial')
    else:
        print('Não foi possível realizar o saque, saldo insufiente.')
else:
    print("Sistema não reconheceu seu tipo de conta, fale com seu gerente!")