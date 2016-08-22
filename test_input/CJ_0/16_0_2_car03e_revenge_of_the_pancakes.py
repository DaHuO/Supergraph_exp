import argparse


def parse_args():
    """Parses the command line arguments and returns a dictionary of args and
    their values."""
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="the file with all the input values")
    return parser.parse_args()

BLANK = '-'

def number_of_flips( stack ):
    """ Counts the number of flips necessary to have all the pancakes face
        happy side up. """
    flips = 0
    # counts the number of flips to get all pancakes facing the same side
    for i in range( len(stack) - 1 ):
        if stack[ i ] != stack[ i + 1 ]:
            flips += 1
    # if the last pancake if BLANK, must flip all the pancakes
    if BLANK == stack[ -1 ]:
        flips += 1

    return flips

def main():
    args = parse_args()
    incoming = args.input
    outgoing = incoming.replace( ".in", ".out" )

    with open( incoming, "r" ) as f:
        trials = int( f.readline().strip() )

        for i in range( 1, trials + 1 ):
            stack = list( f.readline().strip() )
            flips = number_of_flips( stack )

            result = "Case #{}: {}".format( i, flips )

            with open( outgoing, "a" ) as o:
                o.write( result )
                if i < trials:
                    o.write( "\n" )


if __name__ == "__main__":
    main()

def test_number_of_flips_one():
    pancakes = list( "-" )
    assert number_of_flips( pancakes ) == 1

def test_number_of_flips_two():
    pancakes = list( "-+" )
    assert number_of_flips( pancakes ) == 1

def test_number_of_flips_three():
    pancakes = list( "+-" )
    assert number_of_flips( pancakes ) == 2

def test_number_of_flips_four():
    pancakes = list( "+++" )
    assert number_of_flips( pancakes ) == 0

def test_number_of_flips_five():
    pancakes = list( "--+-" )
    assert number_of_flips( pancakes ) == 3
