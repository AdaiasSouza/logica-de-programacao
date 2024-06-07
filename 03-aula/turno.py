turno_informado = str(input("Em que turno voce estuda ? M-matutino ou V-Vespertino ou N- Noturno "))

if turno_informado == 'M' or turno_informado == 'm':
	print("Bom Dia!")
elif turno_informado == 'V' or turno_informado == 'v':
	print("Boa Tarde!")
elif turno_informado == 'N' or turno_informado == 'n':
	print("Boa Noite!")
else:
	print("Valor Inválido!")

