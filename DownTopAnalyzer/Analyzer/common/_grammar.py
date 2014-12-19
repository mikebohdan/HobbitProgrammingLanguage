from collections import OrderedDict
from Analyzer.common._element import Element


def init():
    alphabet = OrderedDict([
        # Non terminals
        ('<main>', Element('<main>')),
        ('<data_type>', Element('<data_type>')),
        ('<param_list>', Element('<param_list>')),
        ('<param_list1>', Element('<param_list1>')),
        ('<variable>', Element('<variable>')),
        ('<block>', Element('<block>')),
        ('<block_body>', Element('<block_body>')),
        ('<block_body1>', Element('<block_body1>')),
        ('<source_code_string>', Element('<source_code_string>')),
        ('<sc_element>', Element('<sc_element>')),
        ('<inp>', Element('<inp>')),
        ('<out>', Element('<out>')),
        ('<if_expression>', Element('<if_expression>')),
        ('<arithmetic_expression>', Element('<arithmetic_expression>')),
        ('<arithmetic_expression_body>', Element('<arithmetic_expression_body>')),
        ('<arithmetic_expression_body1>', Element('<arithmetic_expression_body1>')),
        ('<term>', Element('<term>')),
        ('<multiplier>', Element('<multiplier>')),
        ('<mp_body>', Element('<mp_body>')),
        ('<value>', Element('<value>')),
        ('<operator_1lvl>', Element('<operator_1lvl>')),
        ('<operator_2lvl>', Element('<operator_2lvl>')),
        ('<for_cycle>', Element('<for_cycle>')),
        ('<input_param_list>', Element('<input_param_list>')),
        ('<bool_expression>', Element('<bool_expression>')),
        ('<comparable>', Element('<comparable>')),
        ('<bool_operator>', Element('<bool_operator>')),
        ('<splitter>', Element('<splitter>')),
        ('<+>', Element('<+>')),
        ('<->', Element('<->')),
        ('<ID>', Element('<ID>')),
        ('<constant>', Element('<constant>')),
        # =================

        # Terminals
        ('int', Element('int')),
        ('float', Element('float')),
        ('string', Element('string')),
        ('bool', Element('bool')),
        ('void', Element('void')),
        ('true', Element('true')),
        ('false', Element('false')),
        ('{', Element('{')),
        ('}', Element('}')),
        ('\\n', Element('\\n')),
        ('in', Element('in')),
        ('out', Element('out')),
        ('if', Element('if')),
        ('(', Element('(')),
        (')', Element(')')),
        ('else', Element('else')),
        ('+', Element('+')),
        ('-', Element('-')),
        ('*', Element('*')),
        ('/', Element('/')),
        ('%', Element('%')),
        ('for', Element('for')),
        ('to', Element('to')),
        ('do', Element('do')),
        (',', Element(',')),
        ('<', Element('<')),
        ('>', Element('>')),
        ('<=', Element('<=')),
        ('>=', Element('>=')),
        ('!=', Element('!=')),
        ('==', Element('==')),
        ('!', Element('!')),
        ('?', Element('?')),
        ('&', Element('&')),
        ('"', Element('"')),
        (';', Element(';')),
        (':', Element(':')),
        ('[', Element('[')),
        (']', Element(']')),
        ('ID', Element('ID')),
        ('constant', Element('constant')),
        ('=', Element('='))
        # ==================
    ])

    # Equal relations
    alphabet['<data_type>'].Equals = [alphabet['ID']]
    alphabet['<param_list1>'].Equals = [alphabet[')']]
    alphabet['<variable>'].Equals = [alphabet[',']]
    alphabet['<constant>'].Equals = [alphabet[','], alphabet[')'], alphabet['<block>']]
    alphabet['<block>'].Equals = [alphabet['else']]
    alphabet['<block_body1>'].Equals = [alphabet['}']]
    alphabet['<source_code_string>'].Equals = [alphabet['<block_body>']]
    alphabet['<sc_element>'].Equals = [alphabet['\\n']]
    alphabet['<arithmetic_expression>'].Equals = [alphabet['to']]
    alphabet['<arithmetic_expression_body1>'].Equals = [alphabet[')'], alphabet['do']]
    alphabet['<term>'].Equals = [alphabet['<operator_1lvl>']]
    alphabet['<multiplier>'].Equals = [alphabet['<operator_2lvl>']]
    alphabet['<operator_1lvl>'].Equals = [alphabet['<arithmetic_expression_body>']]
    alphabet['<operator_2lvl>'].Equals = [alphabet['<term>']]
    alphabet['<input_param_list>'].Equals = [alphabet[')']]
    alphabet['<bool_expression>'].Equals = [alphabet[')']]
    alphabet['<comparable>'].Equals = [alphabet['<bool_operator>']]
    alphabet['<bool_operator>'].Equals = [alphabet['<comparable>']]
    alphabet['string'].Equals = [alphabet[',']]
    alphabet['{'].Equals = [alphabet['<block_body>']]
    alphabet['in'].Equals = [alphabet['(']]
    alphabet['out'].Equals = [alphabet['(']]
    alphabet['if'].Equals = [alphabet['(']]
    alphabet['('].Equals = [alphabet['<param_list>'], alphabet['<input_param_list>'], alphabet['constant'],
                           alphabet['<bool_expression>'], alphabet['<arithmetic_expression_body>']]
    alphabet[')'].Equals = [alphabet['<block>']]
    alphabet['else'].Equals = [alphabet['<block>']]
    alphabet['<+>'].Equals = [alphabet['<mp_body>']]
    alphabet['<->'].Equals = [alphabet['<mp_body>']]
    alphabet['for'].Equals = [alphabet['<arithmetic_expression>']]
    alphabet['to'].Equals = [alphabet['<arithmetic_expression_body>']]
    alphabet['do'].Equals = [alphabet['<block>']]
    alphabet[','].Equals = [alphabet['<param_list>'], alphabet['<input_param_list>']]
    alphabet['<ID>'].Equals = [alphabet['('], alphabet['='], alphabet[',']]
    alphabet['='].Equals = [alphabet['<arithmetic_expression_body>']]

    # First relations
    alphabet['<main>'].First = [alphabet['<data_type>']]
    alphabet['<data_type>'].First = [alphabet['int'], alphabet['float'], alphabet['string'],
                                     alphabet['bool'], alphabet['void']]
    alphabet['<param_list>'].First = [alphabet['<variable>']]
    alphabet['<variable>'].First = [alphabet['<data_type>']]
    alphabet['<block>'].First = [alphabet['{']]
    alphabet['<block_body>'].First = [alphabet['<source_code_string>']]
    alphabet['<source_code_string>'].First = [alphabet['<sc_element>']]
    alphabet['<sc_element>'].First = [alphabet['<variable>'], alphabet['<inp>'], alphabet['<out>'],
                                      alphabet['<if_expression>'], alphabet['<arithmetic_expression>'],
                                      alphabet['<for_cycle>']]
    alphabet['<inp>'].First = [alphabet['in']]
    alphabet['<out>'].First = [alphabet['out']]
    alphabet['<if_expression>'].First = [alphabet['if']]
    alphabet['<arithmetic_expression>'].First = [alphabet['ID']]
    alphabet['<arithmetic_expression_body>'].First = [alphabet['<term>']]
    alphabet['<term>'].First = [alphabet['<multiplier>']]
    alphabet['<multiplier>'].First = [alphabet['+'], alphabet['-'], alphabet['<mp_body>']]
    alphabet['<mp_body>'].First = [alphabet['('], alphabet['<value>']]
    alphabet['<value>'].First = [alphabet['constant'], alphabet['ID']]
    alphabet['<operator_1lvl>'].First = [alphabet['+'], alphabet['-']]
    alphabet['<operator_2lvl>'].First = [alphabet['*'], alphabet['/'], alphabet['%']]
    alphabet['<for_cycle>'].First = [alphabet['for']]
    alphabet['<input_param_list>'].First = [alphabet['ID'], alphabet['constant']]
    alphabet['<bool_expression>'].First = [alphabet['<comparable>'], alphabet['true'], alphabet['false']]
    alphabet['<comparable>'].First = [alphabet['ID'], alphabet['constant']]
    alphabet['<bool_operator>'].First = [alphabet['<'], alphabet['>'], alphabet['<='], alphabet['>='],
                                         alphabet['!='], alphabet['==']]
    alphabet['<splitter>'].First = [alphabet[','], alphabet['!'], alphabet['?'], alphabet['\\n'],
                                    alphabet['<'], alphabet['>'], alphabet['<='], alphabet['>='],
                                    alphabet['!='], alphabet['=='], alphabet['&'],
                                    alphabet['='], alphabet['+'],  alphabet['-'], alphabet['*'], alphabet['/'],
                                    alphabet['%'], alphabet['('], alphabet[')'], alphabet['{'], alphabet['}'],
                                    alphabet['['], alphabet[','], alphabet['"'], alphabet[';']]
    alphabet['<+>'].First = [alphabet['+']]
    alphabet['<->'].First = [alphabet['-']]
    alphabet['<param_list1>'].First = [alphabet['<param_list>']]
    alphabet['<block_body1>'].First = [alphabet['<block_body>']]
    alphabet['<arithmetic_expression_body1>'].First = [alphabet['<arithmetic_expression_body>']]
    alphabet['<ID>'].First = [alphabet['ID']]
    alphabet['<constant>'].First = [alphabet['constant']]

    # Last relations
    alphabet['<main>'].Last = [alphabet['<block>']]
    alphabet['<data_type>'].Last = [alphabet['int'], alphabet['float'], alphabet['string'],
                                    alphabet['bool'], alphabet['void']]
    alphabet['<param_list>'].Last = [alphabet['<param_list>'], alphabet['<variable>']]
    alphabet['<variable>'].Last = [alphabet['ID']]
    alphabet['<block>'].Last = [alphabet['}']]
    alphabet['<block_body>'].Last = [alphabet['<block_body>'], alphabet['<source_code_string>']]
    alphabet['<source_code_string>'].Last = [alphabet['\\n']]
    alphabet['<sc_element>'].Last = [alphabet['<variable>'], alphabet['<inp>'], alphabet['<out>'],
                                     alphabet['<if_expression>'], alphabet['<arithmetic_expression>'],
                                     alphabet['<for_cycle>']]
    alphabet['<inp>'].Last = [alphabet[')']]
    alphabet['<out>'].Last = [alphabet[')']]
    alphabet['<if_expression>'].Last = [alphabet['<block>']]
    alphabet['<arithmetic_expression>'].Last = [alphabet['<arithmetic_expression_body>']]
    alphabet['<arithmetic_expression_body>'].Last = [alphabet['<term>'], alphabet['<arithmetic_expression_body>']]
    alphabet['<term>'].Last = [alphabet['<term>'], alphabet['<multiplier>']]
    alphabet['<multiplier>'].Last = [alphabet['<mp_body>']]
    alphabet['<mp_body>'].Last = [alphabet[')'], alphabet['<value>']]
    alphabet['<value>'].Last = [alphabet['constant'], alphabet['ID']]
    alphabet['<operator_1lvl>'].Last = [alphabet['+'], alphabet['-']]
    alphabet['<operator_2lvl>'].Last = [alphabet['*'], alphabet['/'], alphabet['%']]
    alphabet['<for_cycle>'].Last = [alphabet['<block>']]
    alphabet['<input_param_list>'].Last = [alphabet['ID'], alphabet['constant']]
    alphabet['<bool_expression>'].Last = [alphabet['<comparable>'], alphabet['true'], alphabet['false']]
    alphabet['<comparable>'].Last = [alphabet['ID'], alphabet['constant']]
    alphabet['<bool_operator>'].Last = [alphabet['<'], alphabet['>'], alphabet['<='], alphabet['>='],
                                        alphabet['!='], alphabet['==']]
    alphabet['<splitter>'].Last = [alphabet[','], alphabet['!'], alphabet['?'], alphabet['\\n'],
                                   alphabet['<'], alphabet['>'], alphabet['<='], alphabet['>='],
                                   alphabet['!='], alphabet['=='], alphabet['&'],
                                   alphabet['='], alphabet['+'],  alphabet['-'], alphabet['*'], alphabet['/'],
                                   alphabet['%'], alphabet['('], alphabet[')'], alphabet['{'], alphabet['}'],
                                   alphabet['['], alphabet[','], alphabet['"'], alphabet[';']]
    alphabet['<+>'].Last = [alphabet['+']]
    alphabet['<->'].Last = [alphabet['-']]
    alphabet['<param_list1>'].Last = [alphabet['<param_list>']]
    alphabet['<block_body1>'].Last = [alphabet['<block_body>']]
    alphabet['<arithmetic_expression_body1>'].Last = [alphabet['<arithmetic_expression_body>']]
    alphabet['<ID>'].Last = [alphabet['ID']]
    alphabet['<constant>'].Last = [alphabet['constant']]

    # FirstPlus relations
    for i in alphabet:
        alphabet[i].findFirstPlus()

    # LastPlus relations
    #alphabet['<block_body>'].findLastPlus()
    for i in alphabet:
        alphabet[i].findLastPlus()

    return alphabet


if __name__ == '__main__':
    alphabet = init()
    for i in alphabet:
        print("{:30}".format(i), [j.name for j in alphabet[i].Equals])