"""t = [0 for i in range(16)]
t[0] = 1
t[1] =1 
t[14] = 1
t[15] = 1
print( "".join(str(x) for x in t), "3 4 5 6 7 8 9 10 11") 
for b in range(2, 11):
    a = 0
    bp = 1
    for i in range(len(t)):
        a += t[i]*bp
        bp *= b
    print(a)"""
c = ""
print("Case #1:")
for i in range(10):
    c+="0"
for i in range(500):
    a = "{0:09b}".format(i)
    b = ""
    for char in a:
        b += char+char
    
    print("11"+c+b+"11 3 4 5 6 7 8 9 10 11")
