# range + for
# range -> range (start, stop, step)


numeros_positivos = range(0, 11, 1) # Output: 0 a 10 de 1 em 1
# O ultimo número nunca é incluido 

numeros_negativos = range(0, -11, -1) # Output: 0 a 10 de 1 em 1
# O ultimo número nunca é incluido 

# Criando a veriável (numero) para iterar sobre cada numero
for numero in numeros_positivos:
  print(numero)