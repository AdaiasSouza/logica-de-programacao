print("\tMENU")
print("\t1->soma\n2->subtracao\n3->multiplicacao\n4->divisao")

inicia_menu = True

opcao_soma = 1
opcao_subtracao = 2
opcao_multiplicacao = 3
opcao_divisao = 4

while inicia_menu:	
	opcao_menu = int(input("Informe opcao: "))
	if opcao_menu == opcao_soma:
		print("\tSOMA:", end='\n')
		num_1 = float(input("Informe numero: "))
		num_2 = float(input("Informe numero: "))
		soma = num_1+num_2
		print(f"\t{num_1} + {num_2} = {soma}")
	elif opcao_menu == opcao_subtracao:
		print("\tSUBTRACAO:", end='\n')
		num_1 = float(input("Informe numero: "))
		num_2 = float(input("Informe numero: "))
		subtracao = num_1-num_2
		print(f"\t{num_1} - {num_2} = {subtracao}")
	elif opcao_menu == opcao_multiplicacao:
		print("\tMULTIPLICACAO:", end='\n')
		num_1 = float(input("Informe numero: "))
		num_2 = float(input("Informe numero: "))
		multiplicao = num_1*num_2
		print(f"\t{num_1} x {num_2} = {multiplicao}")
	elif opcao_menu == opcao_divisao:
		print("\tDIVISAO:", end='\n')
		num_1 = float(input("Informe numero: "))
		num_2 = float(input("Informe numero: "))
		divisao = num_1/num_2
		print(f"\t{num_1} / {num_2} = {divisao}")
	else:
		print("Opção inválida!")
	inicia_menu = str(input(("Continua ? S -> Sim, N -> Nao: ")))
	if inicia_menu == 'N' or inicia_menu == 'n':
		inicia_menu = False	
	
print("Fim da execucao...")
print()

	
	

