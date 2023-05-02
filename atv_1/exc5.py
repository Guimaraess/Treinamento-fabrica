salario = float(input("Digite o valor do salário recebido: "))
gastos = float(input("Digite o valor total gasto em despesas: "))

if gastos <= salario:
    print("Gastos dentro do orçamento.")
else:
    print("Gastos ultrapassaram o orçamento.")
