


def ler(s):
	res = []
	res.append(s[0])
	for i in s[1:]:
		if i >= res[0]:
			res.insert(0,i)
		else:
			res.append(i)
	return res


if __name__ == '__main__':
        T = int(raw_input())
        for i in range(0,T):
		st = 'Case #'+str(i+1)+': '
                linha = raw_input()
		st += ''.join(ler(linha))
		print st
