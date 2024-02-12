# While else


string = 'valorqualquer'


i = 0

while i < len(string):
  letra = string[i]
  print(letra)
  i +=1

  if letra == ' ':
    print("Achei o espaço")
    break

else:
  print('Não encontrei espaço na string')