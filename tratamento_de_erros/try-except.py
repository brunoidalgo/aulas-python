"""

Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

"""

numero_str = input(
  'Vou dobrar o número digitado: '
)



try:
  numero_float = float(numero_str)
  print(f'float: {numero_float}')
  print(f'O dobro de {numero_float} é {numero_float * 2:.2f}')
except:
  print(f'{numero_str} não é um número.')








# if numero_str.isdigit():
#   numero_float = float(numero_str)
#   print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#   print(f'{numero_str} não é um número.')