class IsNotAType(Exception):

    previous = None
    msg = "Token isn't a valid type."

    def __init__(self, line_number, previous=None):
        self._line_number = line_number
        self.previous = previous

    def __str__(self):
        return "At line "+str(self._line_number)+": "+self.msg + \
               '\n' + self.previous.__str__()


class NoMainFunction(Exception):

    previous = None
    msg = "First function in file isn't main."

    def __init__(self, line_number, previous=None):
        self._line_number = line_number
        self.previous = previous

    def __str__(self):
        return "At line "+str(self._line_number)+": "+self.msg + \
               '\n' + self.previous.__str__()


class WrongMainDeclaration(Exception):

    previous = None
    msg = "Wrong main function declaration."

    def __init__(self, line_number, previous=None):
        self._line_number = line_number
        self.previous = previous

    def __str__(self):
        return "At line "+str(self._line_number)+": "+self.msg + \
               '\n' + self.previous.__str__()

class WrongVariablenDeclaration(Exception):

    previous = None
    msg = "Wrong variable declaration."

    def __init__(self, line_number, previous=None):
        self._line_number = line_number
        self.previous = previous

    def __str__(self):
        return "At line "+str(self._line_number)+": "+self.msg + \
               '\n' + self.previous.__str__()


class UnknownConstant(Exception):

    previous = None
    msg = "Unknown constant."

    def __init__(self, line_number, previous=None):
        self._line_number = line_number
        self.previous = previous

    def __str__(self):
        return "At line "+str(self._line_number)+": "+self.msg + \
               '\n' + self.previous.__str__()


class WrongBlockDeclaration(Exception):

    previous = None
    msg = "Wrong block declaration."

    def __init__(self, line_number, previous=None):
        self._line_number = line_number
        self.previous = previous

    def __str__(self):
        return "At line "+str(self._line_number)+": "+self.msg + \
               '\n' + self.previous.__str__()


class WrongSourceCodeString(Exception):

    previous = None
    msg = "Wrong source code string."

    def __init__(self, line_number, previous=None):
        self._line_number = line_number
        self.previous = previous

    def __str__(self):
        return "At line "+str(self._line_number)+": "+self.msg + \
               '\n' + self.previous.__str__()


class WrongInputDeclaration(Exception):

    previous = None
    msg = "Wrong input declaration."

    def __init__(self, line_number, previous=None):
        self._line_number = line_number
        self.previous = previous

    def __str__(self):
        return "At line "+str(self._line_number)+": "+self.msg + \
               '\n' + self.previous.__str__()


class WrongOutputDeclaration(Exception):

    previous = None
    msg = "Wrong output declaration."

    def __init__(self, line_number, previous=None):
        self._line_number = line_number
        self.previous = previous

    def __str__(self):
        return "At line "+str(self._line_number)+": "+self.msg + \
               '\n' + self.previous.__str__()


class WrongIfDeclaration(Exception):

    previous = None
    msg = "Wrong If declaration."

    def __init__(self, line_number, previous=None):
        self._line_number = line_number
        self.previous = previous

    def __str__(self):
        return "At line "+str(self._line_number)+": "+self.msg + \
               '\n' + self.previous.__str__()


class WrongArithmeticExpressionDeclaration(Exception):

    previous = None
    msg = "Wrong arithmetic expression declaration."

    def __init__(self, line_number, previous=None):
        self._line_number = line_number
        self.previous = previous

    def __str__(self):
        return "At line "+str(self._line_number)+": "+self.msg + \
               '\n' + self.previous.__str__()


class WrongForExpressionDeclaration(Exception):

    previous = None
    msg = "Wrong for expression declaration."

    def __init__(self, line_number, previous=None):
        self._line_number = line_number
        self.previous = previous

    def __str__(self):
        return "At line "+str(self._line_number)+": "+self.msg + \
               '\n' + self.previous.__str__()


class WrongBoolExpressionDeclaration(Exception):

    previous = None
    msg = "Wrong bool expression declaration."

    def __init__(self, line_number, previous=None):
        self._line_number = line_number
        self.previous = previous

    def __str__(self):
        return "At line "+str(self._line_number)+": "+self.msg + \
               '\n' + self.previous.__str__()


class IsNotComparable(Exception):

    previous = None
    msg = "Token is not comparable."

    def __init__(self, line_number, previous=None):
        self._line_number = line_number
        self.previous = previous

    def __str__(self):
        return "At line "+str(self._line_number)+": "+self.msg + \
               '\n' + self.previous.__str__()

