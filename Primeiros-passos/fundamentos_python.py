nome = input("Qual nome do seu cão? ")
idade_animal = input(f"Qual a idade do {nome} ? ") 
peso_animal = float(input(f"Informe o peso do {nome}: "))

VACINA_INELEGIVEL = float(10)

if peso_animal >= VACINA_INELEGIVEL:
    print ('Seu cão não pode receber a medicação sugerida. Procure um dos nossos veterinários.')
else:
    preco_vacina = 10
    preco_vacina = float(preco_vacina)

    desconto_vacina = 0.50
    valor_total = preco_vacina - desconto_vacina * preco_vacina

    print(f'Valor da Vacina {preco_vacina}€, com desconto: {valor_total}€')
