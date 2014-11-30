import json
from tokenizer.common.alphabet import Alphabet
from tokenizer.common.error import OverriddenException
from tokenizer.linetokenizer import LineTokenizer


class Tokenizer:
    source_to_analyze = None
    variables = []
    constants = []

    def __init__(self, source_to_analyze):
        self.source_to_analyze = source_to_analyze

    """
    method is analyzing given file for lexical problems
    :returns dictionary of sets tokens, variables and constants
    """
    def analyze(self):
        line_number = 0
        answer = []                                                         # set of all tokens
        variable_id = 0                                                     # variable used for numbering of tokens
        constant_id = 0                                                     # variable used for numbering of constants
        new_variable_create_flag = False                                    # indicate process of creating new variable
        for line in self.source_to_analyze:
            linetokenizer = LineTokenizer(line=line,
                                          line_number=line_number)
            line_number += 1
            while linetokenizer.hasNext():
                try:
                    tokens = linetokenizer.next()                           # getting next token if it exist
                    for token in tokens:
                        answer.append(token)                                # adding token to tokens list
                        token.language_id = Alphabet.getCode(token)         # getting alphabet code of toekn
                        if token.type != '':                                # checking is token is a constant
                            if not self._isConstant(token):
                                token.variable_id = constant_id             # and adding to constant list
                                constant_id += 1
                                self.constants.append(token)
                            continue
                        elif Alphabet.isDataType(token):                    # checking for start of process of creating
                            new_variable_create_flag = True                 # new variable
                            continue
                        elif new_variable_create_flag:                      # if we in process of creating new variable
                            if not Alphabet.isReserved(token):              # and token isn't reserved
                                token.variable_id = variable_id
                                variable_id += 1
                                self.variables.append(token)                # adding token to variable list
                                new_variable_create_flag = False            # end exit process of creating new variable
                                continue
                            else:
                                raise OverriddenException(lnumber=line_number)
                        elif not Alphabet.isReserved(token) and \
                                not self._isVariable(token):                    # if token reserved
                            raise UnknownVariableException(lnumber=line_number) # we raise an Exception

                except Exception as e:                                      # catching and printing any exception
                    raise e
        return {
            'tokens':       answer,
            'variables':    self.variables,
            'constants':    self.constants
        }

    """
    inner method to check is checkable is already a variable
    :returns True if it's a variable, otherwise - False
    """
    def _isVariable(self, checkable):
        for i in self.variables:
            if i.name == checkable.name:
                return True
        return False

    """
    inner method to check is checkable is already a constant
    :returns True if it's a constant, otherwise - False
    """
    def _isConstant(self, checkable):
        for i in self.constants:
            if i.name == checkable.name:
                return True
        return False

if __name__ == '__main__':
    input_file = open("/Users/mike/input.hobbit")
    output_file = open("/Users/mike/output.json", 'w')
    tz = Tokenizer(source_to_analyze=input_file)
    try:
        tz = tz.analyze()
    except OverriddenException as oe:
        print(oe)
    except UnknownVariableException as uve:
        print(uve)
    output_json = json.dumps({
        'tokens':       [i.toDict() for i in tz['tokens']],
        'variables':    [i.toDict() for i in tz['variables']],
        'constants':    [i.toDict() for i in tz['constants']],
    }, separators=(',', ':'), indent=4)
    output_file.write(output_json)
    output_file.close()
    output_token_file = open("/Users/mike/tokens.txt", 'w')
    output_variables_file = open("/Users/mike/variables.txt", 'w')
    output_constants_file = open("/Users/mike/constants.txt", 'w')
    for token in tz['tokens']:
        output_token_file.write(token.__str__()+'\n')
    for variable in tz['variables']:
        output_variables_file.write(variable.__str__()+'\n')
    for constant in tz['constants']:
        output_constants_file.write(constant.__str__()+'\n')