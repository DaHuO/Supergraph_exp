line=0
archivo = open("A-large.in", "Ur")
num_lines = archivo.readline().rstrip('\n')
f = open("resultado.txt", "w")
for dato in range(0,int(num_lines)):
	line+=1
	data = archivo.readline().rstrip('\n')
	res="";
	resultado=data[0]
	i=0
	while(i<len(data)-1):
		res=resultado[0]
		i+=1
		if res>data[i]:
			resultado=resultado+data[i]
		else:
			resultado=data[i]+resultado
	f.write("Case #%d: %s" % (line,resultado+"\n"))
f.close()