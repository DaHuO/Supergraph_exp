
t = int(raw_input())

for i in xrange(1, t+1):
    pancakes = raw_input()

    flips = 0
    happy = True

    while pancakes:
        if happy:
            pancakes = pancakes.rstrip("+")
        else:
            pancakes = pancakes.rstrip("-")

        happy = not happy
        flips += 1

    print "Case #{}: {}".format(i, flips - 1)
