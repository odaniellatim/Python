import os

lista = []
separador = '                     '

while True:
  print(separador)
  print('Selecione uma opção')
  opcao = input('[i]nserir [a]pagar [l]istar: ')

# adiciona um item na lista
  if opcao == 'i':
    os.system('clear')
    valor = input('Valor: ')
    lista.append(valor)

#apaga um item da lista
  elif opcao == 'a':
    #os.system('clear')
    print(separador)
    indice_str = input('Informe o índice para apagar: ')

    try:
      indice = int(indice_str)
      del lista[indice]
    except:
      print('Não foi possivel apagar o índice informado!')

# mostra os itens da lista
  elif opcao == 'l':
    os.system('clear')
    
    if len(lista) == 0:
      print('Sua lista está vazia.')
    
    for i, valor in enumerate(lista):
      print(i, valor)


  else:
    os.system('clear')
    print('Selecione uma opção valida!')