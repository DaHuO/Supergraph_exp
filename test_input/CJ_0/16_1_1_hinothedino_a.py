#!/usr/bin/env python

num_trials = int(input())

for k in range(num_trials):
    
    word = input()

    output = word[0]

    for i in range(1, len(word)):
        if( word[i] < output[0]):
            output += word[i]
        else:
            output = word[i] + output

    print("Case #{}: {}".format(k+1, output))
            
