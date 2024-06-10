print("\t Calculadora: ")
num = int(input("Informe numero: "))
OPCAO_SOMA = 1 
OPCAO_SUBTRACAO = 2
OPCAO_MULTIPLICACAO = 3
OPCAO_DIVISAO = 4
OPCAO_MENU = int(input("Informe opcao: "))
print("1->soma 2->subtracao 3->multiplicacao 4->divisao")
if OPCAO_MENU == OPCAO_SOMA:
	for i in range(0,num,1):
		for j in range(1,10,1):
			k = i+1
			print(f"{k} + {j} = {k+j}")
		print()
elif OPCAO_MENU == OPCAO_SUBTRACAO:
	for i in range(0,num,1):
		for j in range(1,10,1):
			k = i+1
			print(f"{k} - {j} = {k-j}")
		print()
elif OPCAO_MENU == OPCAO_MULTIPLICACAO:
	for i in range(0,num,1):
		for j in range(1,10,1):
			k = i+1
			print(f"{k} x{j} = {k*j}")
		print()
elif OPCAO_MENU == OPCAO_DIVISAO:
	for i in range(0,num,1):
		for j in range(1,10,1):
			k = i+1
			print(f"{k} x{j} = {k/j}")
		print()
else:
	print("Opção inválida")
print()