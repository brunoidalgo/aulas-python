print('----- Calculadora de Imc ----- v1.0')
nome = str(input('Digite seu nome: '))
altura = float(input('Sua altura em metros: '))
peso = int(input('Agora seu peso: '))
imc = peso // (altura * altura)

if(imc < 18):
  print(f'{nome} tem {altura} de altura, pesa {peso} Kg e seu IMC é {imc} Categoria: Baixo Peso')
elif(imc > 18.5 and imc <= 24.9 ):
  print(f'{nome} tem {altura} de altura, pesa {peso} Kg e seu IMC é {imc} Categoria: Peso Adequado')
elif(imc >= 25 and imc <= 29.9):
  print(f'{nome} tem {altura} de altura, pesa {peso} Kg e seu IMC é {imc} Categoria: Sobrepeso')
elif(imc > 30 and imc <= 34.9):
  print(f'{nome} tem {altura:.2f} de altura, pesa {peso} Kg e seu IMC é {imc} Categoria: Obesidade Grau 1')