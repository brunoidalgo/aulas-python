# Operadores logícos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que você já viu)
# 0 0.0 '' False
# Tambem existe o tipo none que é
# usado para representar um não valor.


# entrada = input("[E]ntrar [S]air: ")

# senha_digitada = input('Senha: ')

# senha_permitida = '12345'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#   print('Entrar')
# else:
#   print('Sair')

# Avaliação de curto circuito
# print(True and False and True)

senha = input('Senha: ') or 'Sem senha'
print(senha)