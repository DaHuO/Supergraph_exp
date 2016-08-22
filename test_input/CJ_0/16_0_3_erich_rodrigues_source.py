import math
from functools32 import lru_cache


@lru_cache(maxsize=None)
def is_prime(valor):
    if valor % 2 == 0:
        return 2

    for x in xrange(long(3), 100):
        if valor % x == 0:
            return x
    return False

n = 32
j = 500
corretos = 0

inicio = (2**(n-1))+1
fim = (2 ** n) - 1

print 'Case #1:'
while inicio <= fim and corretos < j:
    binario = bin(inicio)
    binario_str = binario[2:]

    if not(binario_str[0] == '1' and binario_str[-1] == '1'):
        continue
    else:
        ok = True
        lista = []
        for x in xrange(2, 11):
            numero_atual = int(binario_str, x)
            is_ = is_prime(numero_atual)
            if not is_:
                ok = False
                break
            else:
                lista.append(str(is_))
        if ok:
            print binario_str, ' '.join(lista)
            corretos += 1

    inicio += 2
