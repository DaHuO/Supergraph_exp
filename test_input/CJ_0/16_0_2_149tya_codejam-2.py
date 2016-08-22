import unit4utils
import string

def fn(input):
    output=[]
    for s in input[1:]:
        count=0
        length=len(s)
        while "-" in s:
            i=0
            temp=s[i]
            while i<length and temp==s[i]:
                i+=1
            if s[i-1] == "+":
                temp="-"*i
            else:
                temp="+"*i
            temp+=s[i:]
            s=temp
            count+=1
        output.append(count)
    return output

def read_words(filepointer):
    result=[]
    with open(filepointer,'r') as fd:
        for num in fd:
            result.append(num)
    return result

def write_words(filepointer,numbers):
    i=1
    with open(filepointer,'w') as fd:
        for num in numbers:
            num=str(num)
            if i==len(numbers):
                temp="Case #"+str(i)+": "+num
            else:
                temp="Case #"+str(i)+": "+num+"\n"
            fd.write(temp)
            i+=1

def main(source, destination):
    input=read_words(source)
    output=fn(input)
    write_words(destination,output)

def test_anagram_sort():
    source = unit4utils.get_input_file("B-large.in")
    destination = unit4utils.get_temp_file("largeoutput-2.txt")
    main(source, destination)
