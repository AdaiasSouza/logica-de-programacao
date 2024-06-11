lista_alunos = [[6, 7, 5], [4, 5, 7]]
lista_aprovados, lista_reprovados = [], []
media_turma = 7
media_recuperacao = 5

for notas in lista_alunos:
	media_aluno = sum(notas)/len(notas)
	if media_aluno >= media_turma:
		lista_aprovados.append(media_aluno)
	elif media_recuperacao >= media_aluno < media_turma:
		prova_final = float(input("Informe nota final: "))
		media_final = (prova_final+media_aluno)/2
		if media_final >= media_recuperacao:
			lista_aprovados.append(media_final)
		else:
			lista_reprovados.append(media_final)
	else:
		lista_reprovados.append(media_aluno)
print(f"Aprovados: {lista_aprovados}")
print(f"Reprovados: {lista_reprovados}")


