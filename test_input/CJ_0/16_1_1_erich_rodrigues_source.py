n = int(raw_input())
caso = 1


def gera_casos(entrada):
    resposta = []
    tamanho_entrada = len(entrada)

    resposta.append(entrada[0])
    for i in range(1, tamanho_entrada):
        for j in range(len(resposta)):
            resposta.append(resposta[j] + entrada[i])
            resposta[j] = entrada[i] + resposta[j]

    resposta.sort()
    return resposta[-1]


while caso <= n:
    entrada = raw_input()
    resposta = entrada

    lista = gera_casos(entrada)

    print 'Case #' + str(caso) + ': ' + lista
    caso += 1
