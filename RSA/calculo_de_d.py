from euclidiano_extendido import euclidiano_extendido
def calculo_de_d(e, tot):
    if tot == 0:
        exit()
    else:
       beta = euclidiano_extendido(tot, e)
       if beta < 0:
           d = beta%tot 
       else:
           d = beta
    return d
            