print("Recebendo dados pelo teclado: ", end='\n')
num_1 = int(input("Informe um numero: "))
num_2 = int(input("Informe um numero: "))

soma = num_1+num_2
subtracao = num_1+num_2
multiplicacao = num_1*num_2
divisao = num_1/num_2

print("Operacoes aritmeticas: ", end='\n')
print("\tSoma: ", num_1, "+", num_2, "=", soma, end='\n')
print("\tSubtracao: ", num_1, "-", num_2, "=", subtracao, end='\n')
print("\tMultiplicacao: ", num_1, "*", num_2, "=", multiplicacao, end='\n')
print("\tDivisao: ", num_1, "/", num_2, "=", divisao, end='\n')
print()
print("Operacoes aritmeticas(formando impressao I): ", end='\n')
print(f"\tSoma: {num_1} + {num_2} = {soma}")
print(f"\tSubtracao: {num_1} - {num_2} = {subtracao}")
print(f"\tMultiplicacao: {num_1} * {num_2} = {multiplicacao}")
print(f"\tDivisao: {num_1} / {num_2} = {divisao}")
print()
print("Operacoes aritmeticas(formando impressao II): ", end='\n')
print(f"\tSoma: %.2f + %.2f = %.2f"%(num_1, num_2, soma))
print(f"\tSubtracao: %.2f - %.2f = %.2f"%(num_1, num_2, subtracao))
print(f"\tMultiplicacao: %.2f * %.2f = %.2f"%(num_1, num_2, multiplicacao))
print(f"\tDivisao: %.2f / %.2f = %.2f"%(num_1, num_2, divisao))
