with open('1A.in') as f:
    with open('1A.out','w') as f2:
        T = int(f.readline())
        for t in range(T):
            s = f.readline()[:-1]
            news = s[0]
            for i in range(len(s) - 1):
                if s[i + 1] >= news[0]:
                    news = s[i + 1] + news
                else:
                    news = news + s[i + 1]
            f2.write("Case #"+str(t + 1)+": ")
            f2.write(news+'\n')
        f2.close()
