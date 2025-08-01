a = int(input("Digite a:"))
b = int(input("Digite b: "))

x = a 
y = b

d = b 

while x%y != 0:
  d = x%y
  x = y
  y = d
print(f'O mdc({a}, {b}) é igual a: {d}')