# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 
# B r u n o
#-4 -3 -2 -1

# nome = "Bruno"
# print(nome[0])
# print(nome[1])
# print(nome[2])
# print(nome[3])
# print(nome[4])

# print('B' in nome)
# print('b' not in nome)


name = input('Type your name: ')

find = input('Type that you want find ? ')

if find in name:
  print(f"{find} it's at {name}")
else:
  print('Word not founded.')