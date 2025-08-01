def fermat(x, y, n):
  if(y == int(y) and x != (n + 1)/2):
      print(f"{x + y}, {x - y} são fatores de n")
      return 
  elif(x == (n + 1)/2 and y != int(y)):
      print(f"{n} é primo")
      return 
  else:
    if(n == x*x):
      print(f"{n} é um quadrado perfeito tendo {x} como seu fator") 
      return
    else: 
      x += 1 
      y  =  ((x*x) - n)**(1/2) 
      fermat(x,y,n) 

n = int(input("Digite um numero "))
if(n%2 == 0):
  print(f'2 é fator de {n}')
else: 
  raiz = n**(1/2)
  fermat (n//raiz, 0.5, n)

