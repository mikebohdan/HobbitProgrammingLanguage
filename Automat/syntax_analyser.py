import json
from math import isnan
from Automat.common.errors import *
from Automat.common.checkers import *
from Automat.common.common import *
from tokenizer.token import Token


def __creator(state, function):
    return eval("{'state': lambda t:" + state + "," +
                "'function': lambda t:"+function+"}")

stack = [1]
current = 0


def __pop_and_goto(number):
    global stack, current
    stack = stack[:-1]
    current -= 1
    return number


def __pop():
    global stack
    print(stack)
    return True


def __exit():
    global stack
    stack = stack[:-1]
    return True


def __push_and_goto(goto, push):
    global stack, current
    stack.append(push)
    current -= 1
    return goto


def __cycle(goto):
    global current
    current -= 1
    return goto


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
        __creator('True', '__pop_and_goto(11)')
    ],
    11: [
        __creator('t.name=="{"', '12'),
        __creator('True', 'raiser(t=t, exception=WrongBlockDeclaration)')
    ],
    12: [
        __creator('t.name=="}"', '__pop()'),
        __creator('True', '__push_and_goto(21, 13)')
    ],
    13: [
        __creator('t.name=="}"', '__exit()'),
        __creator('True', '__cycle(14)')
    ],
    14: [
        __creator('True', '13')
    ],
    21: [
        __creator('t.name[-1]=="n"', "__pop()"),
        __creator('True', "__push_and_goto(31, 22)")
    ],
    22: [
        __creator('t.name[-1]=="n"', '__pop()'),
        __creator('True', '__pop()')
    ],
    31: [
        __creator('isDataType(t)', '32'),
        __creator('t.name=="in"', '33'),
        __creator('t.name=="out"', '36'),
        __creator('t.name=="if"', '41'),
        __creator('t.name=="for"', '45'),
        __creator('True', '__pop_and_goto(50)')
    ],
    32: [
        __creator('isID(t)', '__pop()'),
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
        __creator('t.name==")"', '__pop()'),
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
        __creator('t.name==")"', '__pop()'),
        __creator('t.name==","', '39'),
        __creator('True', 'raiser(t=t, exception=WrongOutputDeclaration)')
    ],
    39: [
        __creator('isID(t)', '40'),
        __creator('True', 'raiser(t=t, exception=WrongOutputDeclaration)')
    ],
    40: [
        __creator('t.name==")"', '__pop()'),
        __creator('t.name==","', '39'),
        __creator('True', 'raiser(t=t, exception=WrongOutputDeclaration)')
    ],
    41: [
        __creator('t.name=="("', '42'),
        __creator('True', 'raiser(t=t, exception=WrongIfDeclaration)')
    ],
    42: [
        __creator('True', '__push_and_goto(100, 43)')
    ],
    43: [
        __creator('t.name==")"', '__push_and_goto(11, 44)'),
        __creator('True', 'raiser(t=t, exception=WrongIfDeclaration)')
    ],
    44: [
        __creator('t.name=="else"', '__pop_and_goto(11)'),
        __creator('True', '__pop()')
    ],
    45: [
        __creator('True', '__push_and_goto(50, 46)')
    ],
    46: [
        __creator('t.name=="to"', '47'),
        __creator('True', 'raiser(t=t, exception=WrongForDeclaration)')
    ],
    47: [
        __creator('True', '__push_and_goto(60, 48)')
    ],
    48: [
        __creator('t.name=="do"', '49'),
        __creator('True', 'raiser(t=t, exception=WrongForDeclaration)')
    ],
    49: [
        __creator('True', '__pop_and_goto(11)')
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
        __creator('True', '__pop_and_goto(60)')
    ],
    60: [
        __creator('True', '__push_and_goto(70, 61)')
    ],
    61: [
        __creator('isLowPriorArithmeticOperation(t)', '__pop_and_goto(60)'),
        __creator('True', '__pop()')
    ],
    70: [
        __creator('True', '__push_and_goto(80, 71)')
    ],
    71: [
        __creator('isHighPriorArithmeticOperation(t)', '__pop_and_goto(70)'),
        __creator('True', '__pop()')
    ],
    80: [
        __creator('isLowPriorArithmeticOperation(t)', '81'),
        __creator('True', '__pop_and_goto(90)')
    ],
    81: [
        __creator('True', '__pop_and_goto(90)')
    ],
    90: [
        __creator('t.name=="("', '91'),
        __creator('isID(t)', '__pop()'),
        __creator('isConstant(t)', '__pop()'),
        __creator('True', 'raiser(t=t, exception=WrongArithmeticExpressionDeclaration)')
    ],
    91: [
        __creator('True', '__push_and_goto(60, 92)')
    ],
    92: [
        __creator('t.name==")"', '__pop()'),
        __creator('True', 'raiser(t=t, exception=WrongArithmeticExpressionDeclaration)')
    ],
    100: [
        __creator('isID(t)', '101'),
        __creator('isConstant(t)', '101'),
        __creator('t.name=="true"', '__pop()'),
        __creator('t.name=="false"', '__pop()')
    ],
    101: [
        __creator('isBoolOperator', '102'),
        __creator('True', 'raiser(t=t, exception=WrongBoolExpressionDeclaration)')
    ],
    102: [
        __creator('isID(t)', '__pop()'),
        __creator('isConstant(t)', '__pop()'),
        __creator('True', 'raiser(t=t, exception=WrongBoolExpressionDeclaration)')
    ]
})


def move(data):
    global stack, automated_table, current

    length = len(data)

    try:
        while True:
            position = stack[-1]

            while True:
                print(position, current, stack)
                for i in automated_table[position]:
                    if i['state'](Token.fromDict(data[current])):
                        result = i['function'](Token.fromDict(data[current]))
                        break
                current += 1
                print(current)
                if type(result) is bool:
                    break
                else:
                    position = result
            if current >= length-1:
                break
    except Exception as e:
        raise e
    #if len(stack) == 0:
    return 'OK'
    #else:
    #    return "Unknown error, stack not empty."

if __name__ == '__main__':
    data = open('/Users/mike/HobbitTest/o1', 'r')
    data = json.loads(data.read())
    data = data['tokens']
    try:
        print(move(data))
    except Exception as e:
        print(e)

    print(stack)