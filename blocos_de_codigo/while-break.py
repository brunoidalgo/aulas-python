"""

RepetiçÕes
while (enquanto)
Eexecuta uma ação enquanto uma condição for verdadeira.

"""

contador = 0

while contador <= 30:
  contador += 1

  if contador == 6:
    print("Não vou mostrar o 6")
    continue
  

  if contador >= 10 and contador <= 26:
    print(f"Não vou mostrar o {contador}")
    continue
  
  print(contador)

  if contador == 28:
    break
  
  

print("Acabou")
  



# condicao_str = True

# while condicao_str:
#   nome = input("Digite seu nome: ")
  
#   if len(nome) >= 3:
#     print(f"Seu nome é: {nome}")
#     condicao_str = False
#   else:
#     print("Digite um nome válido")
