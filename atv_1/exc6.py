ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = 2023

idade = ano_atual - ano_nascimento

if idade >= 18:
    print("Você tem", idade, "anos e é maior de idade.")
else:
    print("Você tem", idade, "anos e é menor de idade.")
