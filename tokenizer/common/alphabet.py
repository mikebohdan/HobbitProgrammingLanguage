class AlphabetClass:
    data_types = {
        'string':   1,
        'bool':     2,
        'int':      3,
        'float':    4,
        'void':     5
    }
    splitters = {
        '<':        10,
        '>':        11,
        '<=':       12,
        '>=':       13,
        '!=':       14,
        '==':       15,
        '&&':       16,
        '||':       17,
        '=':        21,
        '+':        22,
        '-':        23,
        '*':        24,
        '/':        25,
        '%':        26,
        '(':        45,
        ')':        46,
        '{':        47,
        '}':        48,
        ',':        52,
        '"':        54,
        ';':        55,
        '#':        102,
        '\\n':      103,
    }
    key_words = {
        'if':       60,
        'for':      61,
        'to':       62,
        'else':     74,
        'return':   79,
        'output':   84,
        'input':    85,
    }

    """
    checks is the checkable is a data type
    :returns True if checkable is Data Type, otherwise - False
    """
    def isDataType(self, checkable):
        try:
            self.data_types[checkable.name]          # tries to get a code for checkable in data_type dictionary
            return True                         # if it can't to get it checkable isn't a data type
        except KeyError:                        # otherwise - is Data Type
            return False

    """
    checks is the checkable is a reserved word
    :returns True if it's a reserved word, otherwise - False
    """
    def isReserved(self, checkable):
        try:                                    # tries to get a code of data type for checkable
            self.data_types[checkable.name]
            return True
        except KeyError:
            try:
                self.splitters[checkable.name]       # tries to get a code of splitter for checkable
                return True
            except KeyError:
                try:
                    self.key_words[checkable.name]   # tries to get a code of key word for checkable
                    return True
                except KeyError:                # if it can get one of the codes it returns true
                    return False                # otherwise it returns false

    """
    try to get a code of variable
    :returns if it's an alphabet key it returns code, otherwise - 0
    """
    def getCode(self, var):
        try:
            return self.splitters[var.name]             # tries to return a code of splitter for var
        except KeyError:
            try:
                return self.data_types[var.name]        # tries to return a code of data type for var
            except KeyError:
                try:
                    return self.key_words[var.name]     # trie to return a code of key word for var
                except KeyError:                        # if all tries are unsuccessful return 0
                    return 0

Alphabet = AlphabetClass()
