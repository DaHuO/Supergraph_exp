
# coding: utf-8

# In[ ]:

# t = int(raw_input())
# for case in range(1,t+1):
#     s = raw_input()
#     last_word = [s[0]]
#     for letter in s[1:]:
#         if ord(letter) >= ord(last_word[0]):
#                     last_word.insert(0,letter)
#         else:
#             last_word.append(letter)
#     print "Case #{}: {}".format(case,''.join(last_word))


# In[ ]:

t = int(raw_input())
for case in range(1,t+1):
    s = raw_input()
    last_word = {0:s[0]}
    first,last = 0,0
    for letter in s[1:]:
        if ord(letter) >= ord(last_word[first]):
            last_word[first-1] = letter
            first = first-1
        else:
            last_word[last+1] = letter
            last = last+1
    last_word = [last_word[key] for key in sorted(last_word.keys())]
    print "Case #{}: {}".format(case,''.join(last_word))


# In[ ]:



