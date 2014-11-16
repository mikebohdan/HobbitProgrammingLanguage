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

    """
    method represent Token in readable form
    :returns representing string
    """
    def __str__(self):
        return format('line: %5d \u007c token: %30s \u007c type: %9s \u007c alphabet_id: %5d \u007c variable_id: %5.0f' %
                      (self.line_number, self.name, self.type, self.language_id, self.variable_id))

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
