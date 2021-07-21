nome = input("Digite o nome do cliente: ")
dia = int(input("Digite o dia de vencimento: "))
mes = input("Digite o mês do vencimento: ")
valor = input("Digite o valor da fatura: ")

print("Olá, {}".format(nome))
print("A sua fatura com vencimento em {} de {} no valor de R$ {} está fechada.".format(dia, mes, valor))
