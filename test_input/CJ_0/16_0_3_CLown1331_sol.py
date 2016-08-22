def dec_bin( nbr ):
	ret = 0
	dig = 1
	while nbr > 0:
		rem = nbr % 2
		rem *= dig
		ret += rem
		nbr /= 2
		dig *= 10
	return ret 

def base_convert( nbr, base ):
	ret = 0
	dig = 0
	while nbr > 0:
		rem = nbr % 10
		rem *=  pow( base, dig )
		ret += rem
		nbr /= 10
		dig += 1
	return ret

def prime( nbr ):
	if nbr == 2 or nbr == 1:
		return -1
	i = 2
	while i * i <= nbr:
		if nbr % i == 0:
			return i
		i += 1
	return -1

t = int( raw_input() )
cs = 0
li = [0] * 12
while t > 0:
	t -= 1
	cs += 1
	n, j = map( int, raw_input().split() )
	start = pow( 2, n - 1 ) + 1
	end = pow( 2, n )
	print "Case #{}:".format( cs )
	fl = True
	cnt = 0
	for nbrs in xrange( start, end, 2 ):
		binary = dec_bin( nbrs )
		fl = True
		for base in xrange( 2, 11 ):
			dec = base_convert( binary, base )
			li[ base ] = prime( dec )
			if li[ base ] == -1:
				fl = False
				break
		if fl == True:
			print binary, li[ 2 ], li[ 3 ], li[ 4 ], li[ 5 ], li[ 6 ], li[ 7 ], li[ 8 ], li[ 9 ], li[ 10 ]
			cnt += 1
		if cnt == j:
			break