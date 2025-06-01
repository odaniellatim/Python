while True:
  numero_1 = input('Digite um número: ')
  numero_2 = input('Digite outro número: ')
  operador = input('Digite o operador (+ - / *): ')

  numeros_validos = None
  num_1_float = 0
  num_2_float = 0

  separador = '                                 '
  
  try:
    num_1_float = float(numero_1)
    num_2_float = float(numero_2)
    numeros_validos = True
  except:
    numeros_validos = None

  if numeros_validos is None:
    print(separador, separador)
    print('Um ou ambos os números digitados são inválidos.')
    print(separador, separador)
    continue

  operadores_permtiidos = '+-/*'

  if operador not in operadores_permtiidos:
    print(separador, separador)
    print('Operador inválido.')
    print(separador, separador)
    continue

  if len(operador) > 1:
    print(separador, separador)
    print('Digite apenas um operador.')
    print(separador, separador)
    continue

  print('Realizando sua conta. Confira o resultado abaixo:')
  print(separador, separador)
  if operador == '+':
    print(separador, separador)
    print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)
  elif operador == '-':
    print(separador, separador)
    print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)
  elif operador == '/':
    print(separador, separador)
    print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float)
  elif operador == '*':
    print(separador, separador)
    print(f'{num_1_float} x {num_2_float} = ', num_1_float * num_2_float)
  else:
    print(separador, separador)
    print('Nunca deveria chegar aqui.')

  # sair do programa
  print(separador, separador)
  sair = input('Quer sair? [s]im: ').lower().startswith('s')
  print(separador, separador)

  if sair is True:
    break