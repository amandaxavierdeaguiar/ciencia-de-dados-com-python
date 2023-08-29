texto = input('Informe seu texto:')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end= ' ')
print('') #Adiciona quebra de linha