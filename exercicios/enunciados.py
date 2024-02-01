"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# num = input("Digite um número inteiro: ")

# try:
#   if num.isdigit():
#     num_int = int(num)
#   if num_int % 2 == 0: 
#     print(f'{num_int} número é par! ') 
#   else: 
#     print(f'{num_int} é ímpar! ')
# except:
#   print(f"{num} não é um número inteiro, por favor digite um número válido !")



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input("Que horas são ? ")

# try:
#   if hora.isdigit():
#     hora_float = float(hora)
#     if hora_float >= 4 and hora_float <= 11.59: 
#       print(f'São: {hora_float:.2f} da manha, Bom dia ! ') 
#     elif hora_float >= 12 and hora_float <= 17.59: 
#       print(f'São: {hora_float:.2f} da tarde, boa tarde ! ')
#     elif hora_float >= 18 and hora_float <= 23.59:
#       print(f'São: {hora_float:.2f} da noite, boa noite ! ')
#     else:
#       print("Não conheço essa hora !")

# except:
#   print(f"{hora} não é um número, por favor digite um número válido !")



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
"""

name = input("Type your first name: ")

try:
  if name.isDigit():
    if len(name) < 4:
      print("Your name is small")
    elif len(name) >= 5 and len(name) <= 6:
      print("Your name is normal.")
    else:
      print("Your have a big name.")
except:
  print("Dado inválido tente novamente.")