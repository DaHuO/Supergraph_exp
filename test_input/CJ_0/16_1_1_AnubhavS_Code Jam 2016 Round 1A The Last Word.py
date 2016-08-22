
with open("C:/Users/Anubhav/Desktop/A-large.in", "r") as filein:
    with open("C:/Users/Anubhav/Desktop/A-large.out", "w") as fileout:

        number = int(filein.readline())

        for i in range(number):
            s = filein.readline()
            t = s[0]
            s = s[1:]

            for ch in s:
                if ch < t[0]:
                    t += ch
                else:
                    t = ch + t
            s = s[1:]

            fileout.write("Case #{}: {}".format(i+1, t))
