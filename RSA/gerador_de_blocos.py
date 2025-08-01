def gerador_de_blocos(pre_cod, n):
    blocos = []
    bloco_atual = pre_cod[0]
    for i in range(1, len(pre_cod)):
        bloco_aux = bloco_atual + pre_cod[i]
        if int(bloco_aux) > n:
            if pre_cod[i] != '0':
                blocos.append(int(bloco_atual))
                bloco_atual = pre_cod[i]
            else:
                blocos.append(int(bloco_atual[:-1]))
                bloco_atual = bloco_atual[-1] + pre_cod[i]
        else:
            bloco_atual = bloco_aux
    if bloco_atual:
        blocos.append(int(bloco_atual))
    return blocos
             