INPUT_TXT = 'input.txt'
OUTPUT_TXT = 'output.txt'
OUTPUT_TEMPLATE = 'Case #{}:\n'
R = 'r'
W = 'w'


def main():
    with open(INPUT_TXT, R) as in_file, open(OUTPUT_TXT, W) as out_file:
        for i, line in enumerate(in_file):
            if not i:
                continue
            n_and_j = line.replace('\n', '').split(' ')
            N = int(n_and_j[0])
            J = int(n_and_j[1])
            write_text = OUTPUT_TEMPLATE.format(i)
            for jamcoin in get_jamcoins(N, J):
                write_text += jamcoin["name"] + " "
                for j in range(2, 10):
                    write_text += str(jamcoin[j]) + " "
                write_text += str(jamcoin[10]) + "\n"
            out_file.write(write_text)


def get_jamcoins(jamcoin_length, number_of_jamcoins, thouroughness=1000):
    '''
    The higher the value of thouroughness is, the slower the algorithm.
    The lower the ratio of jamcoin_length/the number_of_jamcoins is,
    the higher the thouroughness needs to be in order to find the full
    number_of_jamcoins.
    '''
    jamcoins = []
    i = 0
    for jamcoin_candidate in generate_jamcoin_candidates(jamcoin_length):
        jamcoin = check_if_and_return_jamcoin_divisors(jamcoin_candidate,
                                                       thouroughness)
        if jamcoin:
            jamcoins.append(jamcoin)
            i += 1
        if i == number_of_jamcoins:
            break
    return jamcoins


def generate_jamcoin_candidates(candidate_length=32, search_begin=False):
    i = 0
    if candidate_length >= 32:
        i = 1073741825  # first number with 32 binary digits
    while True:
        check = check_candidate(i, candidate_length)
        if check == "too high":
            break
        elif check == "too low":
            i += 1
        else:
            i += 1
            yield check


def check_candidate(i, candidate_length):
        temp = bin(i)[2:]
        candidate = temp + "1"
        N = len(candidate)
        if N == candidate_length:
            return candidate
        if N > candidate_length:
            return "too high"
        if N < candidate_length:
            return "too low"


def check_if_and_return_jamcoin_divisors(candidate, thouroughness):
    divisors = {}
    for i in range(2, 11):
        number = int(candidate, base=i)
        divisor = find_divisor(number, thouroughness)
        if not divisor:
            return 0
        else:
            divisors[i] = divisor
    divisors["name"] = candidate
    return divisors


def find_divisor(number, thouroughness):
    for i in range(3, thouroughness):
        if not number % i:
            return i
    return 0

if __name__ == "__main__":
    main()
