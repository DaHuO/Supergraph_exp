import sys

def main():

    T = int(sys.stdin.readline().strip())

    for i in range(0,T):
        S = list(sys.stdin.readline().strip())
        flip_count = get_flip_count(S)
        print ("Case #%d: %d" % (i+1, flip_count))


def plain_faces(S):
    return sum(map(lambda x: 1 if x=='-' else 0, S))




def get_flip_count(S):
    
    flip_count=0
    while True:
        if plain_faces(S)==0:
            return flip_count

        #flip the leading '+' 
        if S[0]=='+':
            flip_count+=1
            for i in range(0,len(S)):
                if(S[i]=='-'):
                    break
                else:
                    S[i]='-' # + flipped to -        
    
        last_plain_face_index = get_last_plain_face_index(S)
        flip_on_index(S, last_plain_face_index)
        flip_count+=1


def get_last_plain_face_index(S):    
    index=len(S)-1
    while S[index]!='-':
        index-=1
    return index



def flip(sym):
    if sym=='-':
        return '+'
    else:
        return '-'



def flip_on_index(S, index):

    for i in range(0,index+1):
        if i > index-i:
            break
        tmp1 = S[i]
        tmp2 = S[index-i]
   
        S[i] = flip(tmp2)
        S[index-i] = flip(tmp1)

        



#calling main function
main()

    



