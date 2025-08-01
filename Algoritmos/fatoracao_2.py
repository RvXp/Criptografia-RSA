def fatoracao(n, f, eh_primo):
    if n == 1:
        return
    else:
        while n/f != n//f: 
            if f > n**(1/2):
                if eh_primo == True:
                    print(f'{n} é primo')
                    exit()
            f += 1 
        else:
            print(f'{f}')
            eh_primo = False
            fatoracao(n/f, 2, eh_primo)
        
n = int(input("Digite n: "))
if n == 1 or n == - 1: 
  print(f'{n} não pode ser fatorado!')
else:
  fatoracao(n, 2, True)