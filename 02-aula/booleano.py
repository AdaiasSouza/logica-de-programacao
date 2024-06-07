email_usuario = True
senha_usuario = True
acesso_liberado_and = email_usuario and senha_usuario
acesso_liberado_or = email_usuario or senha_usuario

saldo_conta = False
valor_pedido = True
compra_concluida_and = saldo_conta and	valor_pedido
compra_concluida_or = saldo_conta or valor_pedido

print("\tResultados booleanos: ")
print(f"Email: {email_usuario} and Senha: {senha_usuario} = {acesso_liberado_and}")
print(f"Email: {email_usuario} or Senha: {senha_usuario} = {acesso_liberado_or}")
print(f"Saldo: {saldo_conta} and Valor.Pedido: {valor_pedido} = {compra_concluida_and}")
print(f"Saldo: {saldo_conta} or Valor.Pedido: {valor_pedido} = {compra_concluida_or}")
print()
