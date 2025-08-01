def crivo(vet, p): 
  if p*p > n: 
    for j in range(1, (n-1)//2):
      if vet[j] == 1:
        print(2*j + 1)
    return True
  else:  
    if vet[(p-1)//2] == 0:
     p += 2
    else:
      t = p*p
      while t < n:
        vet[(t-1)//2] = 0
        t += 2*p
      p += 2
    crivo(vet, p)

n = int(input("Digite n: ")) 
vet = []
p = 3

for i in range(0, (n-1)//2):
  vet.append(1)

if(crivo(vet,p) is True):
  exit()

