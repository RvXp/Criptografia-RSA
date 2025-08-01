a = int(input("Digite a: "))
b = int(input("Digite b: "))

x0 = a
y0 = b

x1, x2, x3 = 1, 0, 0
y1, y2, y3 = 0, 1, 0

if b == 0:
  print('Divisão invalida pois o divisor igual a zero')
  exit()
  
while b != 0:
  q = a//b
  r = a%b

  x3 = x1 - q * x2
  y3 = y1 - q * y2

  a = b
  b = r
  
  x1, y1 = x2, y2
  x2, y2 = x3, y3

print(f'alpha = {x1} e beta = {y1}')
d = x0 * x1 + y0 * y1
print(f'mdc({x0}, {y0}) = {d}')
