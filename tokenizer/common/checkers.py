"""
checks if checkable is digit or not and returns True if it's a digit,
otherwise - False
"""
def isDigit(checkable):
    digits = [format('%d' % i)
              for i in range(10)]
    if checkable in digits:
        return True
    else:
        return False
"""
checks if checkable is letter
:returns True if it's a digit, otherwise - False
"""
def isLetter(checkable):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g',
               'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z',
               '_']
    if checkable in letters:
        return True
    else:
        return False

"""
checks for Hooks
:returns True if it's a hook, otherwise returns False
"""
def isDoubleHook(checkable):
    if checkable == '"':
        return True
    else:
        return False

"""
checks for '!'
:returns True if it's a '!', otherwise - False
"""
def isExMark(checkable):
    if checkable == '!':
        return True
    else:
        return False

"""
checks for start of comment
:returns True if checkable == '#', otherwise - False
"""
def isACommentStart(checkable):
    if checkable == '#':
        return True
    else:
        return False

"""
checks for 'e' in float numbers
:returns True if checkable == 'e', otherwise - False
"""
def isE(checkable):
    if checkable == 'e':
        return True
    else:
        return False

"""
checks for '.' in floating numbers
:returns True if checkable == '.', otherwise - False
"""
def isSplitterDot(checkable):
    if checkable == '.':
        return True
    else:
        return False

"""
checks for '|' in splitters
:returns True if checkable == '|', otherwise - False
"""
def isVerticalLine(checkable):
    if checkable == '|':
        return True
    else:
        return False

"""
checks for '&' in splitters
:returns True if checkable == '&', otherwise - False
"""
def isSingleAnd(checkable):
    if checkable == '&':
        return True
    else:
        return False

"""
checks for '=' in splitters
:returns True if checkable == '=', otherwise - False
"""
def isSingleEqu(checkable):
    if checkable == '=':
        return True
    else:
        return False

"""
checks is it single splitter
:returns True if checkable is single splitter, otherwise - False
"""
def isSingleSplitter(checkable):
    single_splitters = ['*', '/', '%', '(', ')', '{', '}', '\n']
    if checkable in single_splitters:
        return True
    else:
        return False

"""
checks for first part of double splitters
:returns True if checkable is first part of double splitter, otherwise - False
"""
def isFirtsPartOfDoubleSplitter(checkable):
    fpds = ['<', '>']
    if checkable in fpds:
        return True
    else:
        return False

"""
checks for '+' and '-'
:returns True if checkable == '+' or '-', otherwise - False
"""
def isPlusOrMinus(checkable):
    pom = ['+', '-']
    if checkable in pom:
        return True
    else:
        return False

"""
checks for white splitter like tab and space
:returns True if checkable is white splitter, otherwise - False
"""
def isWhiteSplitter(checkable):
    ws = ['\t', ' ']
    if checkable in ws:
        return True
    else:
        return False
