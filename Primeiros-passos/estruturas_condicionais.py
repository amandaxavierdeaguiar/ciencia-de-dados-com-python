MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Informe a sua idade: '))

if idade >= MAIOR_IDADE:
    print('\nVocê é maior de idade. já pode tirar a carta de condução')
elif idade == IDADE_ESPECIAL:
    print('\nVocê pode fazer apenas as aulas teóricas, não pode fazer as aulas práticas.')
else:
    print ('\nVocê ainda não pode tirar a Carta de Condução')