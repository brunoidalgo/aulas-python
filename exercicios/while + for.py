for i in range(10): # Do 0 ao 9 -- Não chega ao último número
  if i == 2:
    print('i é 2, pulando...')
    continue

  if i == 8:
    print('i é 8, seu else não executará')
    break

  for j in range(1,3): # Do 1 ao 2 -- Não chega ao último número
    print(i,j)

else:
  print('(For) completo com sucesso')