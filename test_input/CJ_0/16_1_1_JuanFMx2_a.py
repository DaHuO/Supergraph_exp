'''
Created on Apr 8, 2016

@author: JuanFMx2
'''
import sys
import os.path
import traceback

def last_word(case_num,line_input):
  answer = "INSOMNIA"
  try:
    str_w = line_input.strip()
    list_str = [str_w[0]]
    for index in xrange(1,len(str_w)):
      if str_w[index] >= list_str[0]:
        list_str.insert(0,str_w[index],)
      else:
        list_str.append(str_w[index])
    #answer = "".join(reversed(sorted(list_str)))
    answer = "".join(list_str)
  except:
    traceback.print_exc()
    print "Error parsing line '%s'"%line_input
    sys.exit()
  print "Case #%s: %s"%(case_num,answer)

def parse_input(input_path, process_line_func):
  with open(input_path) as f:
    cur_line = f.readline()
    try:
      num_lines_to_process = int(cur_line)
    except:
      print "'%s' is not a number!" % cur_line
      sys.exit(0)
    
    for i in range(num_lines_to_process):
      cur_line = f.readline()
      if not cur_line:
        print "line %s is empty!" % cur_line
        sys.exit(0)
      process_line_func((i+1),cur_line)
    content = f.readlines()
    

def main(input_path):
  if os.path.isfile(input_path):
    parse_input(input_path, last_word)
  else:
    print "Unknown file: '%s'" % input_path
    sys.exit(0)
    
if __name__ == "__main__":
  if len(sys.argv) >= 2:
    main(sys.argv[1])
  else:
    print "Insufficient Parameters"
    sys.exit(0)