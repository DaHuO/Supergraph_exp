t = int(raw_input())  # read a line with a single integer

# def ans(s):
#     arr = [""]
#
#     for i in s:
#         new_arr = []
#         for a in arr:
#             b = i + a
#             c = a + i
#             new_arr.append(b)
#             new_arr.append(c)
#         arr = new_arr
#
#     new_arr.sort(reverse=True)
#     return arr[0]

def ans(s):
    last = s[0]

    for i in s[1:]:
        if i >= last[0]:
            last = i + last
        else:
            last = last + i

    return last

for i in xrange(1, t + 1):
    s = raw_input()
    res = ans(s)
    print "Case #{}: {}".format(i, res)
