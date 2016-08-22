#!/usr/bin/env python3

import sys

DEBUG = False

def main():
  if len(sys.argv) != 2:
    print("Usage: %s <input file>" % sys.argv[0])
    sys.exit(0)
  
  with open(sys.argv[1], 'rt') as f:
    num_cases = int(f.readline())

    for case_num in range(num_cases):
      word = f.readline().strip()
      last_word = word[0]
      seed_char = ord(last_word)
      if DEBUG: print("seed_char: %s - %d" % (last_word, seed_char))
      
      for letter in word[1:]:
        if DEBUG: print("Letter: %s - %d" % (letter, ord(letter)))
        if ord(letter) < seed_char:
          last_word += letter
          if DEBUG: print("Less, after")
        else:
          last_word = letter + last_word
          if DEBUG: print("More, before")
        seed_char = ord(last_word[0])
        if DEBUG: print("New seed char: %s - %d" % (letter, ord(letter)))
      
      print("Case #%d: %s" % (case_num + 1, last_word))

if __name__ == "__main__":
  main()
