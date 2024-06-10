print("\tCalculando medias de notas: ", end='\n')
qtd_medias = int(input("Informe a quantidade de medias: "))
for repeticao in range(qtd_medias):
	print(f"Calculando aluno ->{repeticao}")
	nota_p1 = float(input("Informe nota 1: "))
	nota_p2 = float(input("Informe nota 2: "))
	nota_p3 = float(input("Informe nota 3: "))

	media_aluno = (nota_p1+nota_p2+nota_p3)/3
	media_turma = 7
	media_recuperacao = 5

	if media_aluno >= media_turma:
		print(f"\tAluno aprovado nota:{media_aluno}")
	elif media_recuperacao <= media_aluno < media_turma:
		print(f"\tAluno de recuperacao nota:{media_aluno}")
		prova_final = float(input("Informe nota final: "))
		media_final = (prova_final+media_aluno)/2
		if media_final >= media_recuperacao:
			print(f"\tAluno aprovado nota:{media_final}")
		else:
			print(f"\tAluno reprovado nota:{media_final}")
	else:
		print(f"\tAluno reprovado nota:{media_aluno}")
	print()
print("Fim da execucao...")