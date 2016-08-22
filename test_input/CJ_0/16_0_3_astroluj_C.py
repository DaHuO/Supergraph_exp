# get the prime number
def sieveOfEratosthenes (num):
    arr = []
    for i in range(2, num + 1):
        arr.append(i)

    i = j = 0
    while i < len(arr):
        
        j = i + 1
        while j < len(arr):
            if not (arr[j] % arr[i]):
                arr.pop(j)
            else: j += 1
            
        i += 1

    return arr


# isPrime
def isNotPrime (num):
    
    '''if not num % 2: return False
    
    for i in range(3, num + 1, 2):
        if i * i > num: break
        if num % i == 0: return False

    return True'''
    if num % 2 == 0: return 2

    sqn = int(num ** (0.5))
    for i in range(3, sqn + 1, 2):
        if num % i == 0: return i

    return False


# main
inputFile = open ('C-small-attempt1.in', 'r')
outputFile = open('output.txt', 'w')

testCase = int(inputFile.readline())
for i in range(testCase):

    outputFile.write('Case #{0}:\n'.format((i + 1)))
                 
    N, J = inputFile.readline().split(' ')
    N, J = int(N), int(J)
    count = 0

    # make base coin jam
    coinJam = []
    for i in range(N):
        if not i or i == (N - 1):
            coinJam.append('1')
        else: coinJam.append('0')

    # make coin jam
    while count < J:

        answer = []
        for i in range(2, 11):
            
            sum = 0
            for idx, j in enumerate(coinJam):
                # reverse list
                if j == '1' : sum += pow(i, idx)
            else:
                prime = isNotPrime (sum)
                if prime:
                    answer.append(prime)
                else:
                    break

        else:
            count += 1
            coinJam.reverse()
            outputFile.write('{0} {1}\n'.format(''.join(str(s) for s in coinJam), ' '.join(str(s) for s in answer)))

        # coinJam change
        stopCount = 0
        for i in range(1, (N - 1)):
            if coinJam[i] == '0':
                coinJam[i] = '1'
                break
            else:
                stopCount += 1
                coinJam[i] = '0'
        else:
            if stopCount == N - 2: break


inputFile.close()
outputFile.close()

