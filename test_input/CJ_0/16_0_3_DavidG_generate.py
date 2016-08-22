def to_base(val, base):
	retval = 0
	num = val
	mul = 1
	while num:
		if num & 1:
			retval += mul
		num = num >> 1
		mul = mul * base

	return retval

def solve(N, J):
	b2_val = 2**(N - 1) + 1 - 2

	while J > 0 and b2_val < 2**N:
		b2_val += 2
		
		tdivs = {}

		for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
			if (b2_val % p) == 0:
				tdivs[2] = p
				break
		else:
			continue

		b3_val = to_base(b2_val, 3)

		for p in [2, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
			if (b3_val % p) == 0:
				tdivs[3] = p
				break
		else:
			continue

		b4_val = to_base(b2_val, 4)

		for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
			if (b4_val % p) == 0:
				tdivs[4] = p
				break
		else:
			continue

		b5_val = to_base(b2_val, 5)

		for p in [2, 3, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
			if (b5_val % p) == 0:
				tdivs[5] = p
				break
		else:
			continue

		b6_val = to_base(b2_val, 6)

		for p in [5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
			if (b6_val % p) == 0:
				tdivs[6] = p
				break
		else:
			continue

		b7_val = to_base(b2_val, 7)

		for p in [2, 3, 5, 11, 13, 17, 19, 23, 29, 31, 37]:
			if (b7_val % p) == 0:
				tdivs[7] = p
				break
		else:
			continue

		b8_val = to_base(b2_val, 8)

		for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
			if (b8_val % p) == 0:
				tdivs[8] = p
				break
		else:
			continue

		b9_val = to_base(b2_val, 9)

		for p in [2, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
			if (b9_val % p) == 0:
				tdivs[9] = p
				break
		else:
			continue

		b10_val = to_base(b2_val, 10)

		for p in [3, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
			if (b10_val % p) == 0:
				tdivs[10] = p
				break
		else:
			continue

		print b10_val, tdivs[2], tdivs[3], tdivs[4], tdivs[5], tdivs[6], tdivs[7], tdivs[8], tdivs[9], tdivs[10]
		J -= 1

print "Case #1:"
solve(32, 500)
