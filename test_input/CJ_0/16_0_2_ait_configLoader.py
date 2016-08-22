import yaml

class configLoader(object):
    """
    Loads the configuration
    """
    def load_config(self, file_name):
        with open(file_name, 'r') as ymlfile:
            return  yaml.load(ymlfile)

