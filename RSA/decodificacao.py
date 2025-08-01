def decodificacao(mensagem_codificada, n, d):
    mensagem_decodifica = []
    for i in range(len(mensagem_codificada)):
        de_cript = (mensagem_codificada[i]**d)%n
        mensagem_decodifica.append(de_cript)
    return mensagem_decodifica
    