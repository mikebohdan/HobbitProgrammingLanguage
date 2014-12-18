import json
from math import isnan
from Automat.common.errors import *
from Automat.common.checkers import *
from Automat.common.common import *
from tokenizer.token import Token


def __creator(state, function):
    """
    This function provide functionality of creating dictionary
    on the go.
    :param state: jump condition
    :param function: jump function
    :return: generated code of dictionary
    """
    return eval("{'state': lambda t:" + state + "," +
                "'function': lambda t:"+function+"}")

stack = [1]
current = 0


def __push_and_go(pushed, go):
    """
    This function created for adding to stack.
    Also this function saves current parameter.
    :param pushed: state that function adding to stack
    :param go: next state
    :return: next state
    """
    global current, stack
    stack.append(pushed)
    current -= 1
    return go


def __push_and_go_non_save(pushed, go):
    """
    This function created for adding to stack.
    ATTENTION! This function isn't saves current parameter.
    :param pushed: state that function adding to stack
    :param go: next state
    :return: next state
    """
    stack.append(pushed)
    return go


def __pop_and_exit():
    """
    Simple EXIT function.
    ATTENTION! It isn't saves current value.
    :return: True
    """
    return True


def __go_and_save(go):
    """
    Simple transition function that saves current value.
    :param go: next state
    :return: next state
    """
    global current
    current -= 1
    return go


def __pop_and_save():
    """
    Simple EXIT function.
    Also it is saves current value.
    :return: True
    """
    global current
    current -= 1
    return True

automated_table = dict({
    1: [
        __creator('isDataType(t)', '2'),
        __creator('True', 'raiser(t=t, exception=DataTypeException)')
    ],
    2: [
        __creator('t.name=="main"', '3'),
        __creator('True', 'raiser(t=t, exception=WrongNameOfMainFunction)')
    ],
    3: [
        __creator('t.name=="("', '4'),
        __creator('True', 'raiser(t=t, exception=WrongFunctionDeclaration)')
    ],
    4: [
        __creator('t.name==")"', '5'),
        __creator('True', 'raiser(t=t, exception=WrongFunctionDeclaration)')
    ],
    5: [
        __creator('True', '__go_and_save(11)')
    ],
    11: [
        __creator('t.name=="{"', '12'),
        __creator('True', 'raiser(t=t, exception=WrongBlockDeclaration)')
    ],
    12: [
        __creator('t.name=="}"', '__pop_and_exit()'),
        __creator('True', '__push_and_go(13, 21)')
    ],
    13: [
        __creator('t.name=="}"', '__pop_and_exit()'),
        __creator('True', '__push_and_go(13, 21)')
    ],
    21: [
        __creator('t.name=="\\\\n"', "__pop_and_exit()"),
        __creator('True', "__push_and_go(22, 31)")
    ],
    22: [
        __creator('t.name=="\\\\n"', '__pop_and_exit()'),
        __creator('True', 'raiser(t=t, exception=WrongEndOfLine)')
    ],
    31: [
        __creator('isDataType(t)', '32'),
        __creator('t.name=="in"', '33'),
        __creator('t.name=="out"', '36'),
        __creator('t.name=="if"', '41'),
        __creator('t.name=="for"', '45'),
        __creator('True', '__go_and_save(50)')
    ],
    32: [
        __creator('isID(t)', '__pop_and_exit()'),
        __creator('True', 'raiser(t=t, exception=WrongVariableDeclaration)')
    ],
    33: [
        __creator('t.name=="("', '34'),
        __creator('True', 'raiser(t=t, exception=WrongInputDeclaration)')
    ],
    34: [
        __creator('isID(t)', '35'),
        __creator('True', 'raiser(t=t, exception=WrongInputDeclaration)')
    ],
    35: [
        __creator('t.name==","', '34'),
        __creator('t.name==")"', '__pop_and_exit()'),
        __creator('True', 'raiser(t=t, exception=WrongInputDeclaration)')
    ],
    36: [
        __creator('t.name=="("', '37'),
        __creator('True', 'raiser(t=t, exception=WrongOutputDeclaration)')
    ],
    37: [
        __creator('isString(t)', '38'),
        __creator('True', 'raiser(t=t, exception=WrongOutputDeclaration)')
    ],
    38: [
        __creator('t.name==")"', '__pop_and_exit()'),
        __creator('t.name==","', '39'),
        __creator('True', 'raiser(t=t, exception=WrongOutputDeclaration)')
    ],
    39: [
        __creator('isID(t)', '40'),
        __creator('True', 'raiser(t=t, exception=WrongOutputDeclaration)')
    ],
    40: [
        __creator('t.name==")"', '__pop_and_exit()'),
        __creator('t.name==","', '39'),
        __creator('True', 'raiser(t=t, exception=WrongOutputDeclaration)')
    ],
    41: [
        __creator('t.name=="("', '42'),
        __creator('True', 'raiser(t=t, exception=WrongIfDeclaration)')
    ],
    42: [
        __creator('True', '__push_and_go(43, 100)')
    ],
    43: [
        __creator('t.name==")"', '__push_and_go_non_save(44, 11)'),
        __creator('True', 'raiser(t=t, exception=WrongIfDeclaration)')
    ],
    44: [
        __creator('t.name=="else"', '11'),
        __creator('True', '__pop_and_save()')
    ],
    45: [
        __creator('True', '__push_and_go(46, 50)')
    ],
    46: [
        __creator('t.name=="to"', '47'),
        __creator('True', 'raiser(t=t, exception=WrongForDeclaration)')
    ],
    47: [
        __creator('True', '__push_and_go(48, 60)')
    ],
    48: [
        __creator('t.name=="do"', '49'),
        __creator('True', 'raiser(t=t, exception=WrongForDeclaration)')
    ],
    49: [
        __creator('True', '__go_and_save(11)')
    ],
    50: [
        __creator('isID(t)', '51'),
        __creator('True', 'raiser(t=t, exception=WrongArithmeticExpressionDeclaration)')
    ],
    51: [
        __creator('t.name=="="', '52'),
        __creator('True', 'raiser(t=t, exception=WrongArithmeticExpressionDeclaration)')
    ],
    52: [
        __creator('True', '__go_and_save(60)')
    ],
    60: [
        __creator('True', '__push_and_go(61, 70)')
    ],
    61: [
        __creator('isLowPriorArithmeticOperation(t)', '60'),
        __creator('True', '__pop_and_save()')
    ],
    70: [
        __creator('True', '__push_and_go(71, 80)')
    ],
    71: [
        __creator('isHighPriorArithmeticOperation(t)', '70'),
        __creator('True', '__pop_and_save()')
    ],
    80: [
        __creator('isLowPriorArithmeticOperation(t)', '81'),
        __creator('True', '__go_and_save(90)')
    ],
    81: [
        __creator('True', '90')
    ],
    90: [
        __creator('t.name=="("', '91'),
        __creator('isID(t)', '__pop_and_exit()'),
        __creator('isConstant(t)', '__pop_and_exit()'),
        __creator('True', 'raiser(t=t, exception=WrongArithmeticExpressionDeclaration)')
    ],
    91: [
        __creator('True', '__push_and_go(92, 60)')
    ],
    92: [
        __creator('t.name==")"', '__pop_and_exit()'),
        __creator('True', 'raiser(t=t, exception=WrongArithmeticExpressionDeclaration)')
    ],
    100: [
        __creator('isID(t)', '101'),
        __creator('isConstant(t)', '101'),
        __creator('t.name=="true"', '__pop_and_exit()'),
        __creator('t.name=="false"', '__pop_and_exit()')
    ],
    101: [
        __creator('isBoolOperator', '102'),
        __creator('True', 'raiser(t=t, exception=WrongBoolExpressionDeclaration)')
    ],
    102: [
        __creator('isID(t)', '__pop_and_exit()'),
        __creator('isConstant(t)', '__pop_and_exit()'),
        __creator('True', 'raiser(t=t, exception=WrongBoolExpressionDeclaration)')
    ]
})


def move(data):
    """
    This function checks grammar according to rules that we describe in
    automated_table
    :param data: list of Token objects.
    :return: list of moves and errors if they're exist
    """
    global stack, automated_table, current

    stack = [1]
    current = 0

    length = len(data)
    output = []

    try:
        while True:
            if len(stack) == 0:
                break
            position = stack[-1]
            stack = stack[:-1]

            while True:
                output.append(str([position, data[current]['name'], stack]))
                for i in automated_table[position]:
                    if i['state'](Token.fromDict(data[current])):
                        result = i['function'](Token.fromDict(data[current]))
                        break
                current += 1
                if type(result) is bool:
                    break
                else:
                    position = result
            if current >= length-1:
                break
    except Exception as e:
        output.append(e)
        return output

    if len(stack) == 0:
        output.append('OK')
    else:
        output.append("Unknown error, stack not empty.")

    return output

if __name__ == '__main__':
    data = open('/Users/mike/HobbitTest/o1', 'r')
    data = json.loads(data.read())
    data = data['tokens']
    try:
        print(move(data))
    except Exception as e:
        print(e)

    print(stack)