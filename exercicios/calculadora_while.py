# Calculadora While


# Lógica 

# Pedir primeiro número ao user

# Pedir segundo número ao user

# Solicitar um operador

# Só permitir conta de divisão, multiplicação, adição, subtração

# Assim que ele me mandar o operador eu vou fazer a conta.




while True:

    print('---- Calculadora while ----')

    numero_1 = input("Digite o primeiro número: ")
    numero_2 = input("Digite o segundo número: ")

    numeros_validos = None

    try:
        numero_int_1 = float(numero_1)
        numero_int_2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Caracter digitado inválido tente novamente")
        continue

    print("\nSelecione o operador:")
    print("\n1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão\n")

    operador = input("\nQual operador deseja utilizar ? ")


    if operador == '1':
        print(f"{numero_int_1} + {numero_int_2} = {numero_int_1 + numero_int_2}")
        
    elif operador == '2':
        print(f"{numero_int_1} - {numero_int_2} = {numero_int_1 - numero_int_2}")
        
    elif operador == '3':
        print(f"{numero_int_1} * {numero_int_2} = {numero_int_1 * numero_int_2}")
        
    elif operador == '4':
        print(f"{numero_int_1} // {numero_int_2} = {numero_int_1 // numero_int_2}")

    else:
        print("Caracter inválido digite novamente")
        
    sair = input("\nDeseja Sair ? s/n ").lower().startswith('s')
    if sair is True:
        print("\nVocê saiu")
        break