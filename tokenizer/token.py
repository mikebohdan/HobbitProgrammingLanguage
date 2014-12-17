class Token:
    type = ""
    name = ""
    line_number = 0
    language_id = 0
    variable_id = float('NaN')

    def __init__(self, name, type, line_number):
        self.name = name
        self.type = type
        self.line_number = line_number

    @staticmethod
    def fromDict(dictionary):
        new = Token(dictionary['name'],
                    dictionary['type'],
                    dictionary['line_number'])
        new.language_id = dictionary['alphabet_id']
        new.variable_id = dictionary['variable_id']

        return new

    """
    method represent Token in readable form
    :returns representing string
    """
    def __str__(self):
        return format('line: %5d \u007c token: %20s \u007c type: %6s \u007c alphabet_id: %5d \u007c variable_id: %5.0f'
                      % (self.line_number, self.name, self.type, self.language_id, self.variable_id))

    """
    method represent Token in dictionary form
    :returns dictionary that can be used in creation of json object
    """
    def toDict(self):
        return {
            "line_number": self.line_number,
            "name": self.name,
            "type": self.type,
            "alphabet_id": self.language_id,
            "variable_id": self.variable_id
        }
