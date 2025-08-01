def pre_codificacao(string):
    resultado = ""
    for i in string:
        if i.isalpha():
            valor = ord(i.upper()) - ord('A') + 10
            resultado += str(valor)
        elif i == ' ':
            resultado += '99'
        else:
            resultado += i
    return resultado
