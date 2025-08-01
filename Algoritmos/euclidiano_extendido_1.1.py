dividendo = int(input("Digite a: "))
divisor = int(input("Digite b: "))

r0 = dividendo
r1 = divisor

x, x0, x1 = 1, 0, 0
y, y0, y1 = 0, 1, 0


if divisor == 0: 
  print("Divisao invalida")
  exit()
while r1 != 0: 
  q = r0 // r1 
  r = r0 % r1 
  
  x1 = x - q*x0 
  y1 = y - q*y0 

  r0 = r1 
  r1 = r 

  x, y = x0, y0 
  x0 ,y0 = x1, y1 

print(f'Alpha = {x}\nBeta = {y}') 
d = x * dividendo + y * divisor 
print(f'MDC({dividendo}, {divisor}) = {d}')
