#Problem Revenge of the Pancakes
def solve(p_states):
    """p will be short for pancakes"""
    flips = 0
    p_states = p_states[::-1] #reverse it
    bottom_smiles = True
    prev = "+"
    for s in p_states:
        if bottom_smiles == True and s == prev:
            continue #the bottom pancakes can be ignored if they're smileys
        bottom_smiles = False

        if (s != prev):
            flips +=1
            prev = s


    return flips


if __name__ == "__main__":
    testcases = eval(input())
    for case_num in range(1, testcases+1):
        data = str(input())
        print("Case #%i: %s" % (case_num, solve(data)))
