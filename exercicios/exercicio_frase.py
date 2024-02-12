frase = 'O Python é uma linguagem de pogramação multiparadigma. Python foi criado por Guido Van Rossum'

# Qual letra apareceu mais vezes na frase ?


i = 0
apareceu_mais_vezes = 0
letra_repetida_mais_vezes = ''

while i < len(frase):
  letra_atual = frase[i]

  if letra_atual == " ":
    i += 1
    continue

  letra_repetida = frase.count(letra_atual)


  if apareceu_mais_vezes < letra_repetida:
    apareceu_mais_vezes = letra_repetida
    letra_repetida_mais_vezes = letra_atual

  i += 1

print(f"A letra que apareceu mais vezes foi:'{letra_repetida_mais_vezes}' que apareceu {apareceu_mais_vezes}x")


# Iteração sobre cada indice