import random

def miller_rabin(n, b):
    
    return True


# Entradas        
n = int(input("Digite o número a ser testado: "))
b = int(input("Digite a base inicial: "))


# saida
if(n%2 != 0 and (1 < b < n-1)):
    saida = miller_rabin(n, b)
    
if(saida == True):
    print(f"{n} é composto")
else:
    print("Teste inconclusivo")