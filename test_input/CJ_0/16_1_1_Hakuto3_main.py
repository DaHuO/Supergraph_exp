from sys import stdin

def main():
    a = int(stdin.readline().strip())
    for i in range(a):
        cad = ""; temp = stdin.readline().strip()
        let = temp[0] ; cad+=let
        for j in range(1,len(temp)):
            if let <= temp[j]: cad = temp[j]+cad
            else: cad = cad+temp[j]
            let = cad[0]
        print("Case #{0}: {1}".format(i+1, cad))
main()
