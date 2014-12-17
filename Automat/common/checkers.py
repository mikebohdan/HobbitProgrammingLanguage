from math import isnan


def isDataType(chackable):
    """
    Function checks is checkable a data type.
    :param chackable: need to be a Token
    :return: True if it's a data type, otherwise - False
    """
    temp = chackable.name.lower()
    if temp == 'int' or \
            temp == 'float' or \
            temp == 'void' or \
            temp == 'string'or \
            temp == 'bool':
        return True
    else:
        return False


def isLowPriorArithmeticOperation(checkable):
    """
    Function check is checkable a plus or minus sign.
    :param checkable: need to be a Token
    :return: True if it equal to '+' or '-', otherwise - Flase
    """
    temp = checkable.name
    if temp == '+' or \
            temp == '-':
        return True
    else:
        return False


def isHighPriorArithmeticOperation(checkable):
    """
    Function checks is checkable a multiply, division or modulo sign.
    :param checkable: need to be a Token
    :return: True if it equal to '*', '/' or '%', otherwise - False
    """
    temp = checkable.name
    if temp == '*' or \
            temp == '/' or \
            temp == '%':
        return True
    else:
        return False


def isID(checkable):
    """

    :param checkable:
    :return:
    """
    if checkable.type.lower() == '':
        return True
    else:
        return False


def isConstant(checkable):
    """

    :param checkable:
    :return:
    """
    if checkable.type.lower() != '':
        return True
    else:
        print(checkable)
        return False


def isString(checkable):
    """

    :param checkable:
    :return:
    """
    if checkable.type.lower() == 'string':
        return True
    else:
        return False


def isBoolOperator(checkable):
    """

    :param checkable:
    :return:
    """
    temp = checkable.name.lower()
    if temp == '<' or \
            temp == '>' or \
            temp == '<=' or \
            temp == '>=' or \
            temp == '!=' or \
            temp == '==':
        return True
    else:
        return False