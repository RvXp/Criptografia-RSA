n = int(input("Digite n: "))
if n == 1 or n == - 1: 
  print(f'{n} não pode ser fatorado!')
else:
  f = 2
  while n/f != n//f: 
    if f > n**(1/2): 
      print(f'{n} é primo')
      exit()
    f += 1
  else:
    print(f'{f} é o menor fator de {n}!') 