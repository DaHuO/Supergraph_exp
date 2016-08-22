import argparse


def parse_args():
    """Parses the command line arguments and returns a dictionary of args and
    their values."""
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="the file with all the input values")
    return parser.parse_args()

def last_word( string ):
    """ Returns the last word alphabetically. """
    result = string[0]

    for char in string[ 1: ]:
        if char >= result[0]:
            result = char + result
        else:
            result += char

    return result


def main():
    args = parse_args()
    incoming = args.input
    outgoing = incoming.replace( ".in", ".out" )

    with open( incoming, "r" ) as f:
        trials = int( f.readline().strip() )

        for i in range( 1, trials + 1 ):
            string = f.readline().strip()

            word = last_word( string )

            result = "Case #{}: {}".format( i, word )

            with open( outgoing, "a" ) as o:
                o.write( result )
                o.write( "\n" )

if __name__ == "__main__":
    main()

def test_one():
    assert last_word("CAB") == "CAB"

def test_two():
    assert last_word("JAM") == "MJA"

def test_three():
    assert last_word("CODE") == "OCDE"

def test_four():
    assert last_word("ABAAB") == "BBAAA"

def test_five():
    assert last_word("CABCBBABC") == "CCCABBBAB"

def test_six():
    assert last_word("ABCABCABC") == "CCCBAABAB"

def test_seven():
    assert last_word("ZXCASDQWE") == "ZXCASDQWE"
