def movimentos(d, origem, auxiliar, destino):
    if d == 1:
        print(f'movendo {d} de {origem} para {destino}')
    else:
        movimentos(d-1, origem, destino, auxiliar)
        print(f'movendo {d} de {origem} para {destino}')
        movimentos(d-1, auxiliar, origem, destino)
    
d = int(input("Digite o número de discos: "))
movimentos(d, 'A', 'B', 'C')