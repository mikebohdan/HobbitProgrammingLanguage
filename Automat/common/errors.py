class AbstractException(Exception):
    message = ''
    string_number = 0

    def __init__(self, token):
        """

        :param token:
        :return:
        """
        self.string_number = token.line_number
        self.message = "'" + token.name + "'" + self.message

    def __str__(self):
        return self.message + ' at: ' + str(self.string_number)


class DataTypeException(AbstractException):
    message = ' is not a data type.'


class WrongNameOfMainFunction(AbstractException):
    message = ' is a wrong name of a main function.'


class WrongFunctionDeclaration(AbstractException):
    message = ' is not correct of function declaration.'


class WrongBlockDeclaration(AbstractException):
    message = ' is not a part of block declaration.'


class WrongEndOfLine(AbstractException):
    message = ' can\'t be as EOL.'


class WrongVariableDeclaration(AbstractException):
    message = ' is not variable ID.'


class WrongInputDeclaration(AbstractException):
    message = ' is a wrong token in input declaration!'


class WrongOutputDeclaration(AbstractException):
    message = ' is a wrong token in output declaration!'


class WrongIfDeclaration(AbstractException):
    message = ' is a wrong token in if declaration!'


class WrongForDeclaration(AbstractException):
    message = ' is a wrong token in for declaration!'


class WrongArithmeticExpressionDeclaration(AbstractException):
    message = ' can\'t be in arithmetic expression.'


class WrongBoolExpressionDeclaration(AbstractException):
    message = ' can\'t be in boolean expression.'