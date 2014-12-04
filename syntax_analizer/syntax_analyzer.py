from syntax_analizer.errors.errors import *

"""
This class provides analysis of source code that written on
Hobbit PL.
For using it you must create new object with give it data
(in dictionary form) that must be analysed.
To analyse tokens table you must run method analyze().
"""

class SyntaxAnalyzer:
    # Index of current token in token table
    current = 0

    def __init__(self, data):
        self.data = data['tokens']          # tokens table
        self.variables = data['variables']  # variables table
        self.constants = data['constants']  # constants table

    """
    This method provide analysis the code.
    """
    def analyze(self):
        try:
            self.main()
        except Exception as e:
            raise e

    """
    This method checking enter point of program.
    It must look like this: void main() ...
    """
    def main(self):
        try:
            self.data_type()
            if self.data[self.current].name != 'main':
                raise NoMainFunction(self.data[self.current].line_number)
            self.current += 1
            if self.data[self.current].name != '(':
                raise WrongMainDeclaration(self.data[self.current].line_number)
            self.current += 1
            if self.data[self.current].name != ')':
                raise WrongMainDeclaration(self.data[self.current].line_number)
            self.current += 1
            self.block()
        except Exception as e:
            raise e

    """
    Method check is current token a data type.
    """
    def data_type(self):
        if not (self.data[self.current].name == 'int' or
                self.data[self.current].name == 'float' or
                self.data[self.current].name == 'string' or
                self.data[self.current].name == 'bool' or
                self.data[self.current].name == 'void'):
            raise IsNotAType(self.data[self.current].line_number)
        self.current += 1

    """
    Method provide checking the way of adding new variable.
    It must look like this:
        int main
    """
    def variable(self):
        try:
            self.data_type()
            if not self.inVaraibles():
                raise WrongVariablenDeclaration(self.data[self.current].line_number)
            self.current += 1
        except Exception as e:
            raise WrongVariablenDeclaration(self.data[self.current].line_number, e)

    """
    Method checks is current token a constant.
    """
    def constant(self):
        if not self.inConstants():
            raise UnknownConstant(self.data[self.current].line_number)
        self.current += 1

    """
    Method check correctness declaration of a block.
    It must look like this:
    {
    ...
    }
    """
    def block(self):
        if self.data[self.current].name != '{':
            raise WrongBlockDeclaration(self.data[self.current].line_number)
        self.current += 1
        try:
            self.block_body()
        except Exception as e:
            if self.data[self.current].name != '}':
                raise WrongBlockDeclaration(self.data[self.current].line_number, e)
        if self.data[self.current].name != '}':
            raise WrongBlockDeclaration(self.data[self.current].line_number)
        self.current += 1

    """
    Method provide checking of block content for correctness.
    """
    def block_body(self):
        try:
            self.source_code_string()
            self.block_body()
        except Exception as e:
            raise WrongBlockDeclaration(self.data[self.current].line_number, e)

    """
    Method checks source code for correctness.
    All source code string must look like this:
        <content>\\n
    """
    def source_code_string(self):
        if self.data[self.current].name != '\\n':
            try:
                self.sc_element()
                if self.data[self.current].name != '\\n':
                    raise WrongSourceCodeString(self.data[self.current].line_number)
            except Exception as e:
                raise WrongSourceCodeString(self.data[self.current].line_number, e)
        self.current += 1

    """
    This method checks what kind of element use in this string and
    then use correct method of this class.
    """
    def sc_element(self):
        flag = False
        try:
            self.data_type()
            self.current -= 1
            flag = True
            self.variable()
        except Exception as e:
            if flag:
                raise WrongSourceCodeString(self.data[self.current].line_number, e)
            else:
                try:
                    if self.data[self.current].name == 'in':
                        self.inp()
                    elif self.data[self.current].name == 'out':
                        self.out()
                    elif self.data[self.current].name == 'for':
                        self.for_cycle()
                    elif self.data[self.current].name == 'if':
                        self.if_expression()
                    elif self.inVaraibles():
                        self.arithmetic_expression()
                    else:
                        raise WrongSourceCodeString(self.data[self.current].line_number)
                except Exception as e:
                    raise WrongSourceCodeString(self.data[self.current].line_number, e)

    """
    Method that provide checking of input operation.
    This operation must look like this:
        in(<variable list>)
    """
    def inp(self):
        if self.data[self.current].name != 'in':
            raise WrongInputDeclaration(self.data[self.current].line_number)
        self.current += 1
        if self.data[self.current].name != '(':
            raise WrongInputDeclaration(self.data[self.current].line_number)
        self.current += 1
        try:
            self.input_param_list()
        except Exception as e:
            raise WrongInputDeclaration(self.data[self.current].line_number, e)
        if self.data[self.current].name != ')':
            raise WrongInputDeclaration(self.data[self.current].line_number)
        self.current += 1

    """
    Method that provide checking of output operation.
    This operation must look like this:
        out(<format string>, <variable list>)
    """
    def out(self):
        if self.data[self.current].name != 'out':
            raise WrongOutputDeclaration(self.data[self.current].line_number)
        self.current += 1
        if self.data[self.current].name != '(':
            raise WrongOutputDeclaration(self.data[self.current].line_number)
        self.current += 1
        if self.data[self.current].type != 'string':
            raise WrongOutputDeclaration(self.data[self.current].line_number)
        self.current += 1
        if self.data[self.current].type != ',':
            self.current += 1
            try:
                self.input_param_list()
            except Exception:
                pass
        if self.data[self.current].name != ')':
            raise WrongOutputDeclaration(self.data[self.current].line_number)
        self.current += 1

    """
    Method checks correctness of if expression.
    It must look like this
    if(a==b)<block>
    """
    def if_expression(self):
        if self.data[self.current].name != 'if':
            raise WrongIfDeclaration(self.data[self.current].line_number)
        self.current += 1
        if self.data[self.current].name != '(':
            raise WrongIfDeclaration(self.data[self.current].line_number)
        self.current += 1
        try:
            self.bool_expression()
        except Exception as e:
            raise WrongIfDeclaration(self.data[self.current].line_number, e)
        if self.data[self.current].name != ')':
            raise WrongIfDeclaration(self.data[self.current].line_number)
        self.current += 1
        try:
            self.block()
        except Exception as e:
            raise WrongIfDeclaration(self.data[self.current].line_number, e)

    """
    Method checks correctness of arithmetic expression.
    It must look like this
    a = 1 + 1
    """
    def arithmetic_expression(self):
        if not self.inVaraibles():
            raise WrongArithmeticExpressionDeclaration(self.data[self.current].line_number)
        self.current += 1
        if self.data[self.current].name != '=':
            raise WrongArithmeticExpressionDeclaration(self.data[self.current].line_number)
        self.current += 1
        try:
            self.arithmetic_expression_body()
        except Exception as e:
            raise WrongArithmeticExpressionDeclaration(self.data[self.current].line_number, e)

    """
    Method checks correctness of declaration of operations
    such as adding and subtracting.
    """
    def arithmetic_expression_body(self):
        try:
            self.term()
        except Exception as e:
            raise WrongArithmeticExpressionDeclaration(self.data[self.current].line_number, e)
        if self.data[self.current].name == '+' or \
                self.data[self.current].name == '-':
            self.current += 1
            try:
                self.arithmetic_expression_body()
            except Exception as e:
                raise WrongArithmeticExpressionDeclaration(self.data[self.current].line_number, e)
        self.current += 1

    """
    This method needed for checking correctness declaration of operations
    such as multiply, division.
    """
    def term(self):
        try:
            self.multiplier()
        except Exception as e:
            WrongArithmeticExpressionDeclaration(self.data[self.current].line_number, e)
        if self.data[self.current].name == '*' or \
                self.data[self.current].name == '/' or \
                self.data[self.current].name == '%':
            self.current += 1
            try:
                self.term()
            except Exception as e:
                raise WrongArithmeticExpressionDeclaration(self.data[self.current].line_number, e)

    """
    This method needed for checking correctness declaration unary operations.
    """
    def multiplier(self):
        if self.data[self.current].name == '+' or \
                self.data[self.current].name == '-':
            self.current += 1
        try:
            self.mp_body()
        except Exception:
            raise WrongArithmeticExpressionDeclaration(self.data[self.current].line_number)

    """
    This method needed for checking correctness declaration of operations
    with brackets.
    """
    def mp_body(self):
        if self.data[self.current].name == '(':
            self.current += 1
            try:
                self.arithmetic_expression_body()
            except Exception:
                raise WrongArithmeticExpressionDeclaration(self.data[self.current].line_number)
            if self.data[self.current].name != ')':
                raise WrongArithmeticExpressionDeclaration(self.data[self.current].line_number)
            self.current += 1
        try:
            self.value()
        except Exception:
            raise WrongArithmeticExpressionDeclaration(self.data[self.current].line_number)

    """
    Methods checks that only numbers can be part of arithmetic operations.
    """
    def value(self):
        if self.data[self.current].name == 'int' or \
                self.data[self.current].name == 'float':
            self.current += 1
            if self.inVaraibles():
                self.current += 1
                return

        raise WrongArithmeticExpressionDeclaration(self.data[self.current].line_number)

    """
    This method checks correctness of for cycle declaration.
    It must look like this:
        for i=1 to 10 do <block>
    """
    def for_cycle(self):
        if self.data[self.current].name == 'for':
            self.current += 1
            try:
                self.arithmetic_expression()
                if self.data[self.current].name != 'to':
                    raise WrongForExpressionDeclaration(self.data[self.current].line_number)
                self.current += 1
                self.arithmetic_expression_body()
                if self.data[self.current].name != 'do':
                    raise WrongForExpressionDeclaration(self.data[self.current].line_number)
                self.current += 1
                self.block()
            except Exception as e:
                raise WrongForExpressionDeclaration(self.data[self.current].line_number, e)

    """
    Method checks for correctness declaration of list of parameters
    which we need to give to callable function.
    """
    def input_param_list(self):
        if self.inVaraibles() or \
                self.inConstants():
            self.current += 1
            if self.data[self.current].name == ',':
                self.current += 1
                try:
                    self.input_param_list()
                except Exception as e:
                    raise e
        else:
            self.current += 1

    """
    Method check for correctness of bool expression.
    It can be like:
        true
        false
        a == b
    """
    def bool_expression(self):
        if self.data[self.current].name == 'true' or \
                self.data[self.current].name == 'false':
            self.current += 1
            return
        try:
            self.comparable()
            if self.data[self.current].name == '<' or \
                    self.data[self.current].name == '>' or \
                    self.data[self.current].name == '<=' or \
                    self.data[self.current].name == '>=' or \
                    self.data[self.current].name == '==' or \
                    self.data[self.current].name == '!=':
                self.current += 1
                self.comparable()
            else:
                raise WrongBoolExpressionDeclaration(self.data[self.current].line_number)
        except Exception as e:
            raise WrongBoolExpressionDeclaration(self.data[self.current].line_number, e)

    """
    Method checks can token be compared to another.
    """
    def comparable(self):
        if self.inVaraibles() or \
                self.inConstants:
            self.current += 1
        else:
            raise IsNotComparable(self.data[self.current].line_number)

    """
    Method checks token existence in table of constants.
    """
    def inConstants(self):
        answer = False
        crnt = self.data[self.current]
        for i in self.constants:
            if crnt.name == i.name:
                answer = True
        return answer

    """
    Method checks token existence in table of variables.
    """
    def inVaraibles(self):
        answer = False
        crnt = self.data[self.current]
        for i in self.variables:
            if crnt.name == i.name:
                answer = True
        return answer