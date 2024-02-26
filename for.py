# Iterável -> str, range, etc (__iter__)
# Iterador -> Quem sabe entregar um valor por vez
# Next -> Me entregue o próximo valor
# Iter -> Me entregue seu iterador


# texto = iter('Bruno') # __iter__()
# print(next(texto)) # .__next__()
# print(texto.__next__())


# For letra in texto
text = "Bruno" # Iterável
iterador = iter(text) # Iteretor

while True:
  try:
    letra = (next(iterador))
    print(letra)

  except StopIteration:
    break



for letra in text:
  print(letra)

  """
  
  O laço (for) faz essa sequência de cálculos
  Primeiro ele cria um iterador dentro da sua variável
  Depois ele itera sobre cada indice da sua variável.
  
  """