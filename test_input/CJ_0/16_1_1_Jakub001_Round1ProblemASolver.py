from DomainModel.TestCase import TestCase
import  math

class Round1ProblemASolver:

    def Solve(self):
        tests = int(input())
        for test in range(tests):
            txt = input().strip()
            a = []
            for c in txt:
                if not a or a[0]>c:
                    a.append(c)
                else:
                    a.insert(0,c)
            ret = ''.join(a)
            print("Case #{}: {}".format(test+1, ret))

    def Tests(self):
        yield TestCase("""7
CAB
JAM
CODE
ABAAB
CABCBBABC
ABCABCABC
ZXCASDQWE
""","""Case #1: CAB
Case #2: MJA
Case #3: OCDE
Case #4: BBAAA
Case #5: CCCABBBAB
Case #6: CCCBAABAB
Case #7: ZXCASDQWE
""")


# to run execute code in Solve with standard input & output
# s = Round1ProblemASolver()
# s.Solve()