def check(num):
    proofs = []
    for base in range(2, 11):
        to_check = int(num, base)
        div = 3
        while div*div <= to_check:
            if to_check % div == 0:
                proofs.append(div)
                break
            div += 2
        else:
            return False, []
    return True, proofs

def solve(n, j):
    coins = []
    proofs = []
    extra = 1 + 2**(n-1)
    for num in [extra + 2*i for i in range(2**(n-2))]:
        cand_coin = "{:b}".format(num)
        res, proof = check(cand_coin)
        if res:
            coins.append(cand_coin)
            proofs.append(proof)
            if len(coins) >= j:
                break
    return '\n'.join([coins[i] + " " + " ".join(map(str, proofs[i])) for i in range(j)])
    

filename = input("Enter input filename: ")
file = open(filename, 'r')

if 'in' in filename:
    outfile = open(filename.replace('in','out'), 'w')
else:
    outfile = open('.'.join(filename.split('.')[:-1]) + "out." + filename.split('.')[-1], 'w')

t = int(file.readline().strip())
for i in range(t):
    n,j = file.readline().split()
    outfile.write("Case #{}:\n{}\n".format(i+1, solve(int(n), int(j))))
    
file.close()
outfile.close()