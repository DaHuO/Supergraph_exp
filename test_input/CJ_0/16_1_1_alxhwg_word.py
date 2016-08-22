import sys
import string

def main():
    inF = open(sys.argv[1], 'r')
    name = string.split(sys.argv[1], '.', 1)[0]
    ouF = open("{0}.out".format(name), 'w')
    T = int(inF.readline())
    for i in range(T):
        s = inF.readline()

        k = word(s)

        ouF.write("Case #{0}: {1}".format(i+1, k))
    inF.close()
    ouF.close()

def word(s):
    result = s[0]
    for letter in s[1:]:
        first = result[0]
        if letter >= first:
            result = letter + result
        else:
            result = result + letter
    return result


if __name__ == '__main__':
  main()
