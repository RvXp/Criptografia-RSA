a = int (input("digite a: "))
b = int (input("digite b: "))

q = 0 
r = a 
while(r >= b): 
  r = r - b
  q = q + 1
print(f'quociente: {q}') 
print(f'resto: {r}') 
  