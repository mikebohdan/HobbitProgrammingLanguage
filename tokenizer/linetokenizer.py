from tokenizer.common.checkers import *
from tokenizer.common.error import *
from tokenizer.token import Token
from tokenizer.common.error import EmptyLineReadingException


class LineTokenizer:
    __current_token = ""
    __current_line = ""
    __line_number = 0

    def __init__(self, line, line_number):
        self.__current_line = line + '\n'
        self.__line_number = line_number

    """
    checks for ability to get next token
    :returns true if you have an ability to get a next token otherwise - false
    """
    def hasNext(self):
        if len(self.__current_line) == 0:
            return False
        else:
            return True

    """
    tries to get next token otherwise raise an error
    :returns a tuple of tokens
    """
    def next(self):
        if len(self.__current_line) != 0:
            try:
                return self._state_1()
            except Exception as e:
                raise e
        else:
            raise EmptyLineReadingException(lnumber=self.__line_number)

    def _state_1(self):
        current_symbol = self.__current_line[0]
        self.__current_line = self.__current_line[1:]
        self.__current_token = current_symbol

        if isDigit(current_symbol):                         # checking for start of number token
            return self._state_2()
        elif isDoubleHook(current_symbol):                  # checking for start of string token
            return self._state_8()
        elif isACommentStart(current_symbol):               # checking for start of comment
            self.__current_token = '\n'
        elif isLetter(current_symbol):                      # checking for start of symbolic token
            return self._state_10()
        elif isSingleSplitter(current_symbol) or \
                isSingleEqu(current_symbol):              # checking for single splitter token
            return self._getSplitter()
        elif isFirtsPartOfDoubleSplitter(current_symbol):   # checking for start of double splitter token
            return self._state_11()
        elif isExMark(current_symbol):                      # checking for first part of '!='
            return self._state_12()
        elif isSingleAnd(current_symbol):                   # checking for first part of '&&'
            return self._state_13()
        elif isVerticalLine(current_symbol):                # checking for first part of '||'
            return self._state_14()
        elif isWhiteSplitter(current_symbol):
            return self._state_1()
        else:
            raise SymbolNotFoundExceprint(lnumber=self.__line_number)         # rising an error if symbol no found

    def _state_2(self):
        current_symbol = self.__current_line[0]
        if isDigit(current_symbol):                         # checking for digit
            self.__current_token += current_symbol
            self.__current_line = self.__current_line[1:]
            return self._state_2()
        elif isE(current_symbol):                           # checking for start of float token
            self._push(current_symbol)
            return self._state_5()
        elif isSplitterDot(current_symbol):                 # checking for start of float token
            self._push(current_symbol)
            return self._state_3()
        else:                                               # getting a int token
            return self._getInteger()

    def _state_3(self):
        current_symbol = self.__current_line[0]
        self.__current_token += current_symbol
        self.__current_line = self.__current_line[1:]
        if isDigit(current_symbol):                         # checking for digit after .
            return self._state_4()                          # example 1.+ is not posible
        else:                                               # but 1.1 is correct
            raise InvalidRecordOfFloatNumberException(lnumber=self.__line_number)

    def _state_4(self):
        current_symbol = self.__current_line[0]
        if isDigit(current_symbol):                         # checking for digit for float
            self._push(current_symbol)
            return self._state_4()
        elif isE(current_symbol):                           # checking for e for double precision float number
            self._push(current_symbol)
            return self._state_5()
        else:                                               # getting a float number
            return self._getFloat()

    def _state_5(self):
        current_symbol = self.__current_line[0]
        self.__current_line = self.__current_line[1:]
        self.__current_token += current_symbol
        if isDigit(current_symbol):                         # checking for digit, as example: 2.7e15
            return self._state_6()
        elif isPlusOrMinus(current_symbol):                 # checking for + or -, as example 2.7e-3
            return self._state_7()
        else:                                               # raise an Error in other cases
            raise UnexpectedSymbolException(lnumber=self.__line_number)

    def _state_6(self):
        current_symbol = self.__current_line[0]
        if isDigit(current_symbol):                         # checking for digit in double precision float number
            self.__current_token += current_symbol
            self.__current_line = self.__current_line[1:]
            return self._state_6()
        else:                                               # getting a float number
            return self._getFloat()

    def _state_7(self):
        current_symbol = self.__current_line[0]
        self.__current_line = self.__current_line[1:]
        self.__current_token += current_symbol
        if isDigit(current_symbol):                         # checking for correct digit after + or -
            return self._state_6()                          # example: 3.14e-a is incorrect notice
        else:
            raise UnexpectedSymbolException(lnumber=self.__line_number)

    def _state_8(self):
        if len(self.__current_line) == 0:                   # checking for string ending until line end
            raise WrongStringVariableEndException(lnumber=self.__line_number)
        current_symbol = self.__current_line[0]
        self.__current_line = self.__current_line[1:]
        self.__current_token += current_symbol
        if isDoubleHook(current_symbol):                    # checking for string end
            return self._getString()
        else:
            return self._state_8()

    def _state_9(self):
        return self._getToken()                             # comment skipping

    def _state_10(self):
        current_symbol = self.__current_line[0]
        if isDigit(current_symbol) or \
                isLetter(current_symbol):                   # name of token can consist only letters and numbers
            self._push(current_symbol)
            return self._state_10()
        else:                                               
            return self._getToken()

    def _state_11(self):
        current_symbol = self.__current_line[0]
        if isSingleEqu(current_symbol):                     # checking for '=' in double splitters like >= and <=
            self.__current_token += current_symbol
            self.__current_line = self.__current_line[1:]
        return self._getSplitter()                          # in any case  it returns one of this splitters <, >, >=, <=

    def _state_12(self):
        current_symbol = self.__current_line[0]
        if isSingleEqu(current_symbol):                     # checking for != splitter otherwise rise an error
            self._push(current_symbol)
            return self._getSplitter()
        else:
            raise UnexpectedSymbolException(lnumber=self.__line_number)

    def _state_13(self):
        current_symbol = self.__current_line[0]
        if isSingleAnd(current_symbol):                     # checking for && splitter otherwise rise an error
            self._push(current_symbol)
            return self._getSplitter()
        else:
            pass
        raise UnexpectedSymbolException(lnumber=self.__line_number)

    def _state_14(self):
        current_symbol = self.__current_line[0]
        if isVerticalLine(current_symbol):                     # checking for || splitter otherwise rise an error
            self._push(current_symbol)
            return self._getSplitter()
        else:
            raise UnexpectedSymbolException(lnumber=self.__line_number)

    """
    :returns a tuple with an integer number token
    """
    def _getInteger(self):
        return {Token(name=self.__current_token,
                     type='Int',
                     line_number=self.__line_number)}

    """
    :returns a tuple with a float number token
    """
    def _getFloat(self):
        return {Token(name=self.__current_token,
                     type='float',
                     line_number=self.__line_number)}

    """
    :returns a tuple of splitters tokens
    """
    def _getSplitter(self):
        if self.__current_token == '\n':
            self.__current_token = '\\n'
        return {Token(name=self.__current_token,
                     type='',
                     line_number=self.__line_number)}

    """
    represent string in paradigm of tokens
    :returns a tuple of start splitter token, string and finish splitter token
    """
    def _getString(self):
        return {Token(name=self.__current_token[:1],
                      type='',
                      line_number=self.__line_number),
                Token(name=self.__current_token[1:-1],
                     type='string',
                     line_number=self.__line_number),
                Token(name=self.__current_token[:1],
                      type='',
                      line_number=self.__line_number)}

    """
    :returns tuple of non-typed Tokens like int, double, lol, etc.
    """
    def _getToken(self):
        return {Token(name=self.__current_token,
                     type='',
                     line_number=self.__line_number)}

    """
    pushing line to next value
    """
    def _push(self, current_symbol):
        self.__current_line = self.__current_line[1:]
        self.__current_token += current_symbol
