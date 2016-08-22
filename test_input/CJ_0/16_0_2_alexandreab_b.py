#!/usr/bin/env python
# encoding utf-8

q = input('')
#print("DEBUG: quantidade lida: {}".format(q))
for case in range(1,q+1):
    count = 0
    v = str(raw_input(''))
    l = map((lambda x: x=='+' and 1 or -1),v)
    #print("DEBUG: lista lida: \n\t{}".format(str(l)))
    ok = False
    lok = []

    while not ok:
        # tira o subgrupo final que jah estah organizado
        finalorg=0
        copy = reversed(l)
        for i in copy:
            if i==1:
                finalorg += 1
                l.pop()
            else:
                break
        #print("DEBUG: elementos ok no final: {}".format(str(finalorg)))
        #print("DEBUG: lista remanescente: {}".format(str(l)))
        if not l:
            break

        iniciocerto = 0
        if l[0]==-1:
            #print("DEBUG: o primeiro elemento eh errado, entao trocar.")
            l = map((lambda x:x*(-1)), l)
            l = list(reversed(l))
            count += 1
            #print("DEBUG: ###TROCA. Total: {}".format(count))
            #print("DEBUG: lista com final certo:\n\t{}".format(str(l)))
            continue
        else:
            #print("DEBUG: lista com inicio certo:\n\t{}".format(str(l)))
            for j in l:
                ##print("DEBUG: elemento: {}".format(j))
                if j==1:
                    iniciocerto += 1
                else:
                    break

        #print("DEBUG: elementos certos no inicio: {}".format(iniciocerto))
        pa = l[0:iniciocerto]
        #print("DEBUG: parte A:\n\t{}".format(str(pa)))
        pb = l[iniciocerto:]
        #print("DEBUG: parte B:\n\t{}".format(str(pb)))
        if iniciocerto==len(l):
            #print("DEBUG: tudo ok. \o/")
            break
        else:
            pa = map((lambda x:x*(-1)),pa)
            pa = list(reversed(pa))
            l =  pa+pb
            count += 1
            #print("DEBUG: ###TROCA. Total: {}".format(count))
            #print("DEBUG: lista com o inicio errado:\n\t{}".format(str(l)))

    print("Case #{}: {}".format(case, count))
