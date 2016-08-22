class fileLoader(object):
    """
        load input files
    """
    def __init__(self, config):
        super(fileLoader, self).__init__()
        self.config = config

    def load(self, file_name):
        file_lines = []
        with open(file_name) as r_file:
            file_lines = r_file.readlines()        
        file_lines.reverse()
        intervals = self.get_intervals_num(file_lines)
        return self.read_file_content(file_lines, intervals)

    def get_intervals_num(self, file_lines):
        return int(file_lines.pop()) # also seek

    def read_file_content(self, file_lines, intrervals):
        for x in xrange(intrervals):
            yield self.read_interval_content(file_lines, len(self.config['interval_content']))

            
    def read_interval_content(self, file_lines, interval_size):
        index_to_function = self.config['interval_content']
        this_interval_result = ()
        for x in xrange(interval_size):
            current_line = file_lines.pop()
            if index_to_function[x] == 'int':
                this_interval_result = this_interval_result + (self.int_parse(current_line), )
            if index_to_function[x] == 'string':
                this_interval_result = this_interval_result + (self.string_parse(current_line), )
            if index_to_function[x] == 'int_list':
                this_interval_result = this_interval_result + (self.int_list_parse(current_line, " "), )
            if index_to_function[x] == 'string_list':
                this_interval_result = this_interval_result + (self.string_list_parse(current_line, " "), )
                
        return this_interval_result

    def int_parse(self, line):
        return int(line)

    def string_parse(self, line):
        return line.strip()

    def int_list_parse(self, line, seperator):
        return map(int, line.strip().split(seperator))

    def string_list_parse(self, line, seperator):
        return line.strip().split(seperator)
        
    


    

    
        
        
