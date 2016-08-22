def main():
    cases = int(input())
    for i in range(cases):
        s = input()
        print("Case #"+str(i+1)+": "+find_last_word(s))
def find_last_word(s):
    order = ""
    order += s[0]
    last = ord(s[0])
    for c in s[1:]:
        if(ord(c) < last):
            
            order += c
        else:
            order = c + order
            last = ord(c)
    return ''.join(order)
main()