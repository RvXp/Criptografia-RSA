from calculo_de_e import calculo_de_e
from calculo_de_d import calculo_de_d
def gerador_de_chaves():
    chaves = []
    p = 11
    q = 13
    
    n = p*q
    chaves.append(n)
    tot = (p-1)*(q-1)
    
    e = calculo_de_e(tot)
    chaves.append(e)
    d = calculo_de_d(e, tot)
    chaves.append(d)
    
    return chaves
