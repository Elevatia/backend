class Lib:
    def __init__(self):
        pass

    def required(self, data, requirements):
        if (data != None):
            for requirement in requirements:
                if (requirement not in data):
                    return (False)
            return (True)
        return (False)
