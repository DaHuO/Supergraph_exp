from itertools import combinations

def find_divisor(n):
    for i in range(2, int(n**.5)+1):
        if n % i == 0:
            return i
    return 1

def solve_slow(N, J):
    j = 0
    buf = []
    for i in range(2**(N-2)):
        truncated_binary = bin(i)[2:]
        binary_num = '1' + '0'*(N-2-len(truncated_binary)) + truncated_binary + '1'
        valid_bases = True
        ln = [binary_num]
        for new_base in range(2, 11):
            div = find_divisor(int(binary_num, new_base))
            valid_bases &= (div > 1)
            ln.append(str(div))
        if valid_bases:
            buf.append(' '.join(ln))
            j += 1
        if j == J:
            return '\n'.join(buf)
    assert False, "wtf"
    return '\n'.join(buf)

def composite_monic_polynomials(N, J):
    """generate J composite polynomials of degree N-1 whose coefficients are 0
    or 1.
    """
    j = 0
    l = []
    for n_terms2 in range(2, N, 2):
        n_terms = n_terms2//2
        #print int((N-1)/2. + 1)
        for tp in combinations(range(1, int((N-1)/2. + 1)), n_terms):
            p = [0] * N
            dt = N - 1 - tp[-1]
            raw_factor_coeff_ixs = [0] + list(tp)
            #print tp, dt
            for c in raw_factor_coeff_ixs:
                #print c, c + dt
                p[c] = p[c + dt] = 1
            l.append((p, raw_factor_coeff_ixs))
            #print p
            j += 1
            if j == J:
                break
        if j == J:
            break
    return l

def pretty_format_polynomial(p):
    l = []
    for i, e in enumerate(p):
        if e == 1:
            l.append(str(i))
    return ' '.join(l)

def eval_polynomial(coeff_ixs, x):
    acc = 0
    for coeff_ix in coeff_ixs:
        acc += x**coeff_ix
    return acc

def solve(N, J):
    l = []
    for p, raw_factor_coeff_ixs in composite_monic_polynomials(N, J):
        res = [''.join([str(c) for c in p])]
        #print p
        #print raw_factor_coeff_ixs
        factor_coeff_ixs = [raw_factor_coeff_ixs[-1]-c for c in raw_factor_coeff_ixs]
        #print factor_coeff_ixs
        for base in range(2, 11):
            proof = eval_polynomial(factor_coeff_ixs, base)
            res.append(str(proof))
        l.append(' '.join(res))
    return '\n'.join(l)

if '__main__' == __name__:
    N, J = 32, 500
    print "Case #1:"
    print solve(N, J)
