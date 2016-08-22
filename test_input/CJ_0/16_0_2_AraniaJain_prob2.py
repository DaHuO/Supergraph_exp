test_cases = []

num_cases = int(input("Enter number of test cases: "))
i=0
while(i<num_cases):
    test_cases.append(raw_input())
    i+=1

i=0
while(i<len(test_cases)):
    case = test_cases[i]
    count = 0

    while(case.count("-")>0):
      limit = len(case)
      to_test = case[-limit:]
      while(to_test.count("-")>0):
        limit-=1
        to_test = case[-limit:]

      to_change = case[0:len(case)-limit]
      to_keep = case[-limit:]

      to_change = to_change.replace("-", "a")
      to_change = to_change.replace("+", "-")
      to_change = to_change.replace("a", "+")

      case = to_change + to_keep

      count+=1
    print "Case #{}: {}".format(i+1, count)
    i+=1
