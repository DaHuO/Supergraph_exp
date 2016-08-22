"""
Ronda 1
problema 1
"""

def dameRes(casoActual):
    palabra = casoActual
    posta = ""
    posta += palabra[0]
    for c in palabra[1:]:
        if c >= posta[0]:
            posta = c+posta
        else:
            posta += c

    return posta


t = int(raw_input())
for ti in range(1, t+1):
    casoActual = [s for s in raw_input().split(" ")]
    #casoActual[0] = int(casoActual[0])
    print "Case #{}: {}".format(ti, dameRes(casoActual[0]))