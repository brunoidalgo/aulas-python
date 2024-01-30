# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair" ? ')


if entrada == 'entrar':
  print('Você entrou no sistema')
elif entrada == 'sair':
  print('Você saiu do sistema')
else:
  print('Você não digitou nem entrar e nem sair')

  # Caso a condição for atendida apenas o bloco de código da mesma será executado.
  # Podem ter quantos elif precisar no código.