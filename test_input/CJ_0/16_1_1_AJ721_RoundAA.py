def do_case(str):
	out = str[0]
	for ch in str[1:]:
		if ch < out[0]:
			out = out + ch
		else:
			out = ch + out
	return out

f = open("A-large.in")
lines = f.read().split("\n")
i = 0
out = ""
for line in lines[1:]:
	i+=1
	if len(line) > 0:
		out += ("Case #%d: %s\n" % (i, do_case(line)))
	
open("A-large.out","w").write(out)