import datetime

ano = int(input("Digite seu ano de nascimento: "))
ano_atual=datetime.datetime.now().year
idade=ano_atual-ano
if (idade>=16):
    print("Você pode votar esse ano")
else:
    print("Você ainda não pode votar")