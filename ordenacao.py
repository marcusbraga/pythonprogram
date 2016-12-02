def ordena():
  vet = [int(x) for x in input("Digite a seq numerica com espaco.Ex: 4 5 2 = ").split()]
  a = vet
  print ('  ')
  print ('  ')
  aux = 0
  frase = 'Sequencia desordenada: '
  tam = len (a)
  print (frase,a)
  j = 0
  while j < tam :
    h = j + 1
    while h < tam :
      if a[j] > a[h] :
        aux = a[j]
        a[j] = a[h]
        a[h] = aux
      h += 1
    j += 1
  frase = 'Sequencia ordenado: '
  print ('  ')
  print ('  ')
  print (frase,a)