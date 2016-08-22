def format_pancakes(p):
    result = p[0]
    for i in range(len(p)):
        if p[i] != result[-1]:
            result = result + p[i]
    return result

def solve(pancakes):
    if '+' not in pancakes:
        return 1
    first_plus = pancakes.index('+')
    
    result = pancakes[first_plus:].count('-') * 2
    if first_plus > 0:
        result = result + 1
    return result 

with open('c:\\python27\\codejam\\outputs.out', 'w') as w, open('c:\\python27\\codejam\\B-large.in') as r:
    cases = int(r.readline())
    for case in range(1, cases+1):
        pancakes = format_pancakes(r.readline())
        if case == 12:
            print pancakes
        w.write('Case #{0}: {1}\n'.format(str(case), solve(pancakes)))

