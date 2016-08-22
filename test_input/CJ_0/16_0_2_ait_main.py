import configLoader
import loadFile

def main():
    loader_config = configLoader.configLoader()
    config = loader_config.load_config("config.yml")

    file_reader = loadFile.fileLoader(config['input_file'])
    dataset = file_reader.load("input.txt")
    with open("output.txt", "w") as out_file:
        for i, data in enumerate(dataset):
            answer = sol(data[0])
            answer_string = "case #{0}: {1}\n".format(str(i+1), answer)
            out_file.write(answer_string)



def act(k, i):
    return list(reversed([('-' if x == '+' else '+') for x in k[0:i+1]])) + k[i+1:]


def findseqofpluses(sl):
    return sl.index('-') - 1
        
def firstminusfrombottom(sl):
    n = len(sl)
    slr = list(reversed(sl))
    i = slr.index('-')
    return n-1-i

    

def sol(s):
    sl = list(s)
    steps = 0
    while True:
        try:
            nexti = firstminusfrombottom(sl) if sl[0] == '-' else findseqofpluses(sl)
        except ValueError:
            return steps
        sl = act(sl, nexti)
        steps += 1


if __name__ == "__main__":
    main()
