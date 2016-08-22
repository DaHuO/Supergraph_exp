import math

def is_coin_jam(numb):
    bases = []
    for i in range(2,11):
        if not is_prime(int(numb,i)):
            return False
        bases.append(int(numb,i))
    for j in range(len(bases)):
        bases[j] = is_prime(bases[j])
    return bases



def is_prime(n):
    if n == 2:
        return False
    for i in range(2,int(math.ceil(math.sqrt(n)+1))):
        if n%i == 0:
            return i
    return False

def main():
    fil = open('C-small-attempt0.in','r')
    output = open('output.txt','w')
    cases = fil.readline()
    info = fil.readline().split()
    goal = info[1]
    length = info[0]
    generated_length = int(length)-2
    combos = [bin(x)[2:].rjust(generated_length, '0') for x in range(2**generated_length)]
    teller = 0
    print("Case #1:")
    output.write("Case #1:\n")
    for comb in combos:
        if teller == int(goal):
            break
        if(is_coin_jam("1"+comb+"1")):
            teller += 1
            string = "1"+comb+"1"
            for d in is_coin_jam("1"+comb+"1"):
                string += " "+str(d)
            print(string)
            output.write(string+"\n")
    output.close()
    fil.close()

main()
