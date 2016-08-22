f = open('input.in', 'r')
output = open('output.out', 'w')
lignes=iter(f.read().splitlines())
nbTests=int(next(lignes))

for numeroTest in range(0,nbTests):
    mot = next(lignes)
    lettres = list(mot)

    motFinal = lettres[0]
    lettres.pop(0)

    for element in lettres:
        if element >= motFinal[0]:
            motFinal = element + motFinal
        else:
            motFinal = motFinal + element

    reponse = motFinal

    output.write("Case #"+str(numeroTest+1)+": "+reponse)
    if numeroTest<nbTests-1:
        output.write("\n")
    print("Reponse="+reponse)