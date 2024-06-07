nota_p1 = 5
nota_p2 = 5
nota_p3 = 5

soma_notas = nota_p1+nota_p2+nota_p3
media_aluno = soma_notas/3
media_turma = 7
media_recuperacao = 5

print("Calculando media das notas:")
if media_aluno >= media_turma:
	print(f"\tAluno aprovado. Nota: {media_aluno}")
elif media_aluno >= media_recuperacao and media_aluno < media_turma:
	print(f"\tAluno de prova final. Nota: {media_aluno}")
	nota_prova_final = 5
	media_final = (nota_prova_final + media_aluno)/2
	if media_final >= media_recuperacao:
		print(f"\tAluno aprovado. Nota: {media_final}")
	else:
		print(f"\tAluno reprovado. Nota: {media_final}")
else:
	print(f"\tAluno reprovado. Nota: {media_aluno}")
print()
