"""
Google Code Jam
2016 Qualification Round
Problem C. Coin Jam
Copyright EJM Software 2016
"""
class Jammer(object):
    """Code Jam Helper Class"""
    def __init__(self, input_handle, output_handle):
        self.input_handle = input_handle
        self.output_handle = output_handle
        self.case_num = 1
    def read_string(self):
        """Reads one line as a string"""
        return self.input_handle.readline().rstrip("\n")
    def read_array(self):
        """Reads one line as an array"""
        return self.read_string().split()
    def write_case(self, solution):
        """Write one case to the output handle"""
        self.output_handle.write("Case #%i: %s\n"%(self.case_num, solution))
        self.case_num += 1

def num_from_base(string, base):
    num = 0
    i = 0
    for digit in string[::-1]:
        if digit=="1":
            num += base ** i
        i += 1
    return num

# Only find factors smaller than cutoff. There are extra jamcoins,
# so it is not worth finding the ones with enormous factors!
def first_factor(number, cutoff=10000):
    # Go ahead and eliminate the even numbers
    if number%2==0:
        return 2
    # Check all the odd numbers
    i = 3
    while i * i <= min(number, cutoff):
        if number%i==0:
            return i
        else:
            i+=2
    return None

def solve(jam):
    casecount = int(jam.read_string())
    n, j = map(int, jam.read_array())
    solution = ""
    solution_count = 0
    coin = "1" * n
    end = "1" + "0" * (n-2) + "1"
    while coin != end:
        #print coin
        factors = []
        for base in range(2, 11):
            #print num_from_base(coin, base)
            f = first_factor(num_from_base(coin, base))
            #print base, f
            factors.append(f)
            if f == None:
                break
        if factors.count(None)==0:
            solution += "\n" + coin + " " + " ".join(map(str, factors))
            solution_count += 1
            print str(solution_count) + "/" + str(j)
            if solution_count==j:
                break
        # Calculate the next jam coin
        switch = coin.rindex("1", 1, n-1)
        coin = coin[:switch] + "0" + "1" * (n - switch - 1)
    jam.write_case(solution)

if __name__=="__main__":
    import sys
    if len(sys.argv)==3:
        inputh = open(sys.argv[1], "r") if sys.argv[1]!="null" else sys.stdin
        outputh = open(sys.argv[2], "w") if sys.argv[2]!="null" else sys.stdout
        solve(Jammer(inputh, outputh))
    else:
        print "usage: python a.py INPUT_FILE OUTPUT_FILE"
        print "parameters:"
        print "\tINPUT_FILE is the filename of the input. If \"null\", the program will read from stdin."
        print "\tOUTPUT_FILE is the filename of the output. If \"null\", the program will write to stdout."
