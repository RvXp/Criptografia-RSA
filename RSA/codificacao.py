def codificacao(blocos, n, e):
    mensagem_codificda = []
    for i in range(len(blocos)):
        cript = (blocos[i]**e)%n
        mensagem_codificda.append(cript)
    return mensagem_codificda
