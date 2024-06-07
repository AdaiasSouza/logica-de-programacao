salario_colaborador = 700

if salario_colaborador <= 280:
	novo_salario = salario_colaborador + (salario_colaborador*0.20)
	print(f"Salario antigo: R$ {salario_colaborador} -> Salario novo: R$ {novo_salario}")
elif 280 < salario_colaborador <= 700:
	novo_salario = salario_colaborador + (salario_colaborador*0.15)
	print(f"Salario antigo: R$ {salario_colaborador} -> Salario novo: R$ {novo_salario}")
elif 700 < salario_colaborador <= 1500:
	novo_salario = salario_colaborador + (salario_colaborador*0.10)
	print(f"Salario antigo: R$ {salario_colaborador} -> Salario novo: R$ {novo_salario}")
elif salario_colaborador > 1500:
	novo_salario = salario_colaborador + (salario_colaborador*0.05)
	print(f"Salario antigo: R$ {salario_colaborador} -> Salario novo: R$ {novo_salario}")
