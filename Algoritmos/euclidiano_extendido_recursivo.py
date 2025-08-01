def algoritmo(x0, y0, x1, x2, y1, y2):
  if y0 == 0:
    print(f'alpha = {x1} e beta = {y1}')
    d = x0 * x1 + y0 * y1
    print(f'mdc({x0}, {y0}) = {d}')
    exit()
    
  else:
    
    q = x0//y0
  
    r = x0%y0

    x3 = x1 - q * x2
    y3 = y1 - q * y2

    x0 = y0
    y0 = r

    x1, y1 = x2, y2
    x2, y2 = x3, y3
    algoritmo(x0, y0, x1, x2, y1, y2)

a = int(input("Digite a: "))
b = int(input("Digite b: "))
if b == 0:
  print('Divisão invalida pois o divisor igual a zero')
  exit()
else:
  algoritmo(a, b, 1, 0, 0, 1)
  