def solve(quiz):
    quiz += "+"
    cnt = 0

    for idx in range(len(quiz) -1):
        if quiz[idx] != quiz[idx + 1]:
            cnt += 1

    return cnt
