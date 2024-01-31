"""

CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

"""

velocidade = input('Digite a velocidade atual do carro: ') # Velocidade atual do carro
local_carro = input('Digite o local em que o carro está em número: ') # Local em que o carro está na estrada


try:
  velocidade_float = float(velocidade)
  local_carro_float = float(local_carro)

  RADAR_1 = 60 # velocidade máxima radar 1
  LOCAL_1 = 100 # Local onde está o radar 1
  RADAR_RANGE = 1 # A distância que o radar pega
  # CONSTANTE = "Variáveis" que não vão mudar

  if local_carro_float > LOCAL_1:
    print('Carro passou do radar !')
  elif local_carro_float >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro_float <= (LOCAL_1 + RADAR_RANGE) and velocidade_float > RADAR_1:
    print(f'Carro está no radar 1 e foi detectado com velocidade {velocidade_float} Km/h')
  else:
    print(f'Carro não passou do radar e está a {velocidade_float} km/h.')
except:
  print('Você forneceu dados incorretos, tente novamente.')

