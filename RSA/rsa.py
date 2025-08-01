from pre_codificacao import pre_codificacao
from gerador_de_blocos import gerador_de_blocos
from gerador_de_chaves import gerador_de_chaves
from codificacao import codificacao
from decodificacao import decodificacao
                    
mensagem = 'RSA é pika'
pre_cod = pre_codificacao(mensagem)
print(f"Pré-codificação: {pre_cod}")

chaves = gerador_de_chaves()
n = chaves[0]
e = chaves[1]
d = chaves[2]

print(f"Chave publica: ({e},{n})")
print(f"Chave privada: ({d},{n})")

blocos = gerador_de_blocos(pre_cod, n)
print(blocos)

mensagem_codificada = codificacao(blocos, n, e)
print(f"Mensagem codificada: {mensagem_codificada}")

mensagem_decodifica = decodificacao(mensagem_codificada, n , d)
print(f'Mensagem decodificada: {mensagem_decodifica}')
