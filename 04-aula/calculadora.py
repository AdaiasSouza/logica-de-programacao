"""
	Documentacao..
"""
print("\tMENU")
print("\t1->soma\n2->subtracao\n3->multiplicacao\n4->divisao")
INICIA_MENU = True
OPCAO_SOMA = 1
OPCAO_SUBTRACAO = 2
OPCAO_MULTIPLICACAO = 3
OPCAO_DIVISAO = 4
while INICIA_MENU:
    OPCAO_MENU = int(input("Informe opcao: "))
    if OPCAO_MENU == OPCAO_SOMA:
        print("\tSOMA:", end='\n')
		num_1 = float(input("Informe numero: "))
		num_2 = float(input("Informe numero: "))
		soma = num_1+num_2
		print(f"\t{num_1} + {num_2} = {soma}")
	elif OPCAO_MENU == OPCAO_SUBTRACAO:
		print("\tSUBTRACAO:", end='\n')
		num_1 = float(input("Informe numero: "))
		num_2 = float(input("Informe numero: "))
		subtracao = num_1-num_2
		print(f"\t{num_1} - {num_2} = {subtracao}")
	elif OPCAO_MENU == OPCAO_MULTIPLICACAO:
		print("\tMULTIPLICACAO:", end='\n')
		num_1 = float(input("Informe numero: "))
		num_2 = float(input("Informe numero: "))
		multiplicao = num_1*num_2
		print(f"\t{num_1} x {num_2} = {multiplicao}")
	elif OPCAO_MENU == OPCAO_DIVISAO:
		print("\tDIVISAO:", end='\n')
		num_1 = float(input("Informe numero: "))
		num_2 = float(input("Informe numero: "))
		divisao = num_1/num_2
		print(f"\t{num_1} / {num_2} = {divisao}")
	else:
		print("Opção inválida!")
	INICIA_MENU = str(input(("Continua ? S -> Sim, N -> Nao: ")))
	if INICIA_MENU == 'N' or INICIA_MENU == 'n':
		INICIA_MENU = False
print("Fim da execucao...")
print()
