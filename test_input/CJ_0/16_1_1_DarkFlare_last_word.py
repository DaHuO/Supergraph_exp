import sys
sys.setrecursionlimit(10000)

def construct_last_word(original):
    if original=="":return ""
    str_list=[]
    str_list.extend(original)
    str_list.reverse()
    max_ch=str_list[0]
    for ch in str_list:
        if ch>max_ch:
            max_ch=ch
    index=str_list.index(max_ch)
    str_list.reverse()
    index=len(str_list)-index-1
    right=str_list[0:index]
    if index==len(str_list)-1:left=""
    else:   left=str_list[index+1:]
    if len(right)==0:return str(max_ch)+''.join(left)
    elif len(left)==0:return str(max_ch)+construct_last_word(right)

    return str(max_ch)+construct_last_word(right)+''.join(left)

input=open("input.txt","r")
output=open("output.txt","w")
T = int(input.readline())
for cases in range(1,T+1):
    word=str(input.readline())
    word=word.strip()
    output.write("Case #" + str(cases) + ": " + construct_last_word(word) + "\n")

input.close()
output.flush()
output.close()