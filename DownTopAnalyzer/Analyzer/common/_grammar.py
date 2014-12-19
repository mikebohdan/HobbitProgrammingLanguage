from collections import OrderedDict
from Analyzer.common._element import Element


def init():
    alphabet = OrderedDict([
        # Non terminals
        ('<main>', Element('<main>')),
        ('<data_type>', Element('<data_type>')),
        ('<param_list>', Element('<param_list>')),
        ('<variable>', Element('<variable>')),
        ('<constant>', Element('<constant>')),
        ('<block>', Element('<block>')),
        ('<block_body>', Element('<block_body>')),
        ('<source_code_string>', Element('<source_code_string>')),
        ('<sc_element>', Element('<sc_element>')),
        ('<inp>', Element('<inp>')),
        ('<out>', Element('<out>')),
        ('<if_expression>', Element('<if_expression>')),
        ('<arithmetic_expression>', Element('<arithmetic_expression>')),
        ('<arithmetic_expression_body>', Element('<arithmetic_expression_body>')),
        ('<term>', Element('<term>')),
        ('<multiplier>', Element('<multiplier>')),
        ('<mp_body>', Element('<mp_body>')),
        ('<value>', Element('<value>')),
        ('<operator_1lvl>', Element('<operator_1lvl>')),
        ('<operator_2lvl>', Element('<operator_2lvl>')),
        ('<for_cycle>', Element('<for_cycle>')),
        ('<input_param_list>', Element('<input_param_list>')),
        ('<name>', Element('<name>')),
        ('<name_tail>', Element('<name_tail>')),
        ('<number>', Element('<number>')),
        ('<bool_expression>', Element('<bool_expression>')),
        ('<comparable>', Element('<comparable>')),
        ('<bool_operator>', Element('<bool_operator>')),
        ('<char>', Element('<char>')),
        ('<int>', Element('<int>')),
        ('<float>', Element('<float>')),
        ('<string>', Element('<string>')),
        ('<text>', Element('<text>')),
        ('<comment>', Element('<comment>')),
        ('<letter>', Element('<letter>')),
        ('<splitter>', Element('<splitter>')),
        ('<digit>', Element('<digit>')),
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
        ('),', Element('),')),
        ('<', Element('<')),
        ('>', Element('>')),
        ('<=', Element('<=')),
        ('>=', Element('>=')),
        ('!=', Element('!=')),
        ('==', Element('==')),
        ('.', Element('.')),
        ('e', Element('e')),
        ('"', Element('"')),
        ('#', Element('#')),
        ('a', Element('a')),
        ('b', Element('b')),
        ('c', Element('c')),
        ('d', Element('d')),
        ('f', Element('f')),
        ('g', Element('g')),
        ('h', Element('h')),
        ('i', Element('i')),
        ('j', Element('j')),
        ('k', Element('k')),
        ('l', Element('l')),
        ('m', Element('m')),
        ('n', Element('n')),
        ('o', Element('o')),
        ('p', Element('p')),
        ('q', Element('q')),
        ('r', Element('r')),
        ('s', Element('s')),
        ('t', Element('t')),
        ('u', Element('u')),
        ('v', Element('v')),
        ('w', Element('w')),
        ('x', Element('x')),
        ('y', Element('y')),
        ('z', Element('z')),
        ('A', Element('A')),
        ('B', Element('B')),
        ('C', Element('C')),
        ('D', Element('D')),
        ('E', Element('E')),
        ('F', Element('F')),
        ('G', Element('G')),
        ('H', Element('H')),
        ('I', Element('I')),
        ('J', Element('J')),
        ('K', Element('K')),
        ('L', Element('L')),
        ('M', Element('M')),
        ('N', Element('N')),
        ('O', Element('O')),
        ('P', Element('P')),
        ('Q', Element('Q')),
        ('R', Element('R')),
        ('S', Element('S')),
        ('T', Element('T')),
        ('U', Element('U')),
        ('V', Element('V')),
        ('W', Element('W')),
        ('X', Element('X')),
        ('Y', Element('Y')),
        ('Z', Element('Z')),
        ('_', Element('_')),
        ('\\t', Element('\\t')),
        (' ', Element(' ')),
        ('!', Element('!')),
        (',', Element(',')),
        ('?', Element('?')),
        ('&', Element('&')),
        ('`', Element('`')),
        ('\'', Element('\'')),
        (';', Element(';')),
        (':', Element(':')),
        ('[', Element('[')),
        (']', Element(']')),
        ('0', Element('0')),
        ('1', Element('1')),
        ('2', Element('2')),
        ('3', Element('3')),
        ('4', Element('4')),
        ('5', Element('5')),
        ('6', Element('6')),
        ('7', Element('7')),
        ('8', Element('8')),
        ('9', Element('9')),
        ('ID', Element('ID')),
        ('=', Element('='))
        # ==================
    ])

    # Equal relations
    alphabet['<data_type>'].Equals = [alphabet['ID']]
    alphabet['<param_list>'].Equals = [alphabet[')']]
    alphabet['<variable>'].Equals = [alphabet[',']]
    alphabet['<block>'].Equals = [alphabet['else']]
    alphabet['<block_body>'].Equals = [alphabet['}']]
    alphabet['<source_code_string>'].Equals = [alphabet['<block_body>']]
    alphabet['<sc_element>'].Equals = [alphabet['\\n'], alphabet['<comment>']]
    alphabet['<arithmetic_expression>'].Equals = [alphabet['to']]
    alphabet['<arithmetic_expression_body>'].Equals = [alphabet[')'], alphabet['do']]
    alphabet['<term>'].Equals = [alphabet['<operator_1lvl>']]
    alphabet['<multiplier>'].Equals = [alphabet['<operator_2lvl>']]
    alphabet['<operator_1lvl>'].Equals = [alphabet['<arithmetic_expression_body>']]
    alphabet['<operator_2lvl>'].Equals = [alphabet['<term>']]
    alphabet['<input_param_list>'].Equals = [alphabet[')']]
    alphabet['<name>'].Equals = [alphabet['('], alphabet['='], alphabet[',']]
    alphabet['<number>'].Equals = [alphabet['<text>']]
    alphabet['<bool_expression>'].Equals = [alphabet[')']]
    alphabet['<comparable>'].Equals = [alphabet['<bool_operator>']]
    alphabet['<bool_operator>'].Equals = [alphabet['<comparable>']]
    alphabet['<int>'].Equals = [alphabet['.'], alphabet['e']]
    alphabet['<string>'].Equals = [alphabet[','], alphabet[')']]
    alphabet['<text>'].Equals = [alphabet['"']]
    alphabet['<comment>'].Equals = [alphabet['\\n']]
    alphabet['<letter>'].Equals = [alphabet['<name_tail>'], alphabet['<text>']]
    alphabet['<splitter>'].Equals = [alphabet['<text>']]
    alphabet['<digit>'].Equals = [alphabet['<name_tail>'], alphabet['<int>']]
    alphabet['{'].Equals = [alphabet['<block_body>']]
    alphabet['in'].Equals = [alphabet['(']]
    alphabet['out'].Equals = [alphabet['(']]
    alphabet['if'].Equals = [alphabet['(']]
    alphabet['('].Equals = [alphabet['<param_list>'], alphabet['<input_param_list>'],
                            alphabet['<string>'], alphabet['<bool_expression>'],
                            alphabet['<arithmetic_expression_body>']]
    alphabet[')'].Equals = [alphabet['<block>']]
    alphabet['else'].Equals = [alphabet['<block>']]
    alphabet['+'].Equals = [alphabet['<mp_body>']]
    alphabet['-'].Equals = [alphabet['<mp_body>'], alphabet['<int>']]
    alphabet['for'].Equals = [alphabet['<arithmetic_expression>']]
    alphabet['to'].Equals = [alphabet['<arithmetic_expression_body>']]
    alphabet['do'].Equals = [alphabet['<block>']]
    alphabet[','].Equals = [alphabet['<param_list>']]
    alphabet['.'].Equals = [alphabet['<int>']]
    alphabet['e'].Equals = [alphabet['<int>'], alphabet['-'], alphabet['+']]
    alphabet['"'].Equals = [alphabet['<text>']]
    alphabet['#'].Equals = [alphabet['<text>']]
    alphabet['='].Equals = [alphabet['<arithmetic_expression_body>']]

    # First relations
    alphabet['<main>'].First = [alphabet['<data_type>']]
    alphabet['<data_type>'].First = [alphabet['int'], alphabet['float'], alphabet['string'],
                                      alphabet['bool'], alphabet['void']]
    alphabet['<param_list>'].First = [alphabet['<variable>']]
    alphabet['<variable>'].First = [alphabet['<data_type>']]
    alphabet['<constant>'].First = [alphabet['<number>'], alphabet['<string>'],
                                     alphabet['true'], alphabet['false']]
    alphabet['<block>'].First = [alphabet['{']]
    alphabet['<block_body>'].First = [alphabet['<source_code_string>']]
    alphabet['<source_code_string>'].First = [alphabet['<sc_element>'], alphabet['\\n']]
    alphabet['<sc_element>'].First = [alphabet['<variable>'], alphabet['<inp>'], alphabet['<out>'],
                                       alphabet['<if_expression>'], alphabet['<arithmetic_expression>'],
                                       alphabet['<for_cycle>']]
    alphabet['<inp>'].First = [alphabet['in']]
    alphabet['<out>'].First = [alphabet['out']]
    alphabet['<if_expression>'].First = [alphabet['if']]
    alphabet['<arithmetic_expression>'].First = [alphabet['<name>']]
    alphabet['<arithmetic_expression_body>'].First = [alphabet['<term>']]
    alphabet['<term>'].First = [alphabet['<multiplier>']]
    alphabet['<multiplier>'].First = [alphabet['+'], alphabet['-'], alphabet['<mp_body>']]
    alphabet['<mp_body>'].First = [alphabet['('], alphabet['<value>']]
    alphabet['<value>'].First = [alphabet['<number>'], alphabet['<name>']]
    alphabet['<operator_1lvl>'].First = [alphabet['+'], alphabet['-']]
    alphabet['<operator_2lvl>'].First = [alphabet['*'], alphabet['/'], alphabet['%']]
    alphabet['<for_cycle>'].First = [alphabet['for']]
    alphabet['<input_param_list>'].First = [alphabet['<name>'], alphabet['<constant>']]
    alphabet['<name>'].First = [alphabet['<letter>']]
    alphabet['<name_tail>'].First = [alphabet['<digit>'], alphabet['<letter>']]
    alphabet['<number>'].First = [alphabet['<int>'], alphabet['<float>']]
    alphabet['<bool_expression>'].First = [alphabet['<comparable>'], alphabet['true'], alphabet['false']]
    alphabet['<comparable>'].First = [alphabet['<name>'], alphabet['<constant>']]
    alphabet['<bool_operator>'].First = [alphabet['<'], alphabet['>'], alphabet['<='], alphabet['>='],
                                          alphabet['!='], alphabet['==']]
    alphabet['<char>'].First = [alphabet['<letter>'], alphabet['<splitter>']]
    alphabet['<int>'].First = [alphabet['<digit>']]
    alphabet['<float>'].First = [alphabet['<int>']]
    alphabet['<string>'].First = [alphabet['"']]
    alphabet['<text>'].First = [alphabet['<letter>'], alphabet['<number>'], alphabet['<splitter>']]
    alphabet['<comment>'].First = [alphabet['#']]
    alphabet['<letter>'].First = [alphabet['a'], alphabet['b'], alphabet['c'], alphabet['d'], alphabet['e'],
                                  alphabet['f'], alphabet['g'], alphabet['h'], alphabet['i'], alphabet['j'],
                                  alphabet['k'], alphabet['l'], alphabet['m'], alphabet['n'], alphabet['o'],
                                  alphabet['p'], alphabet['q'], alphabet['r'], alphabet['s'], alphabet['t'],
                                  alphabet['u'], alphabet['v'], alphabet['w'], alphabet['x'], alphabet['y'],
                                  alphabet['z'],
                                  alphabet['A'], alphabet['B'], alphabet['C'], alphabet['D'], alphabet['E'],
                                  alphabet['F'], alphabet['G'], alphabet['H'], alphabet['I'], alphabet['J'],
                                  alphabet['K'], alphabet['L'], alphabet['M'], alphabet['N'], alphabet['O'],
                                  alphabet['P'], alphabet['Q'], alphabet['R'], alphabet['S'], alphabet['T'],
                                  alphabet['U'], alphabet['V'], alphabet['W'], alphabet['X'], alphabet['Y'],
                                  alphabet['Z'],
                                  alphabet['_']]
    alphabet['<splitter>'].First = [alphabet['.'], alphabet[','], alphabet['!'], alphabet['?'], alphabet['\\n'],
                                    alphabet['\\t'], alphabet['<'], alphabet['>'], alphabet['<='], alphabet['>='],
                                    alphabet['!='], alphabet['=='], alphabet['&'],  alphabet['`'], alphabet['#'],
                                    alphabet['='], alphabet['+'],  alphabet['-'], alphabet['*'], alphabet['/'],
                                    alphabet['%'], alphabet['('], alphabet[')'], alphabet['{'], alphabet['}'],
                                    alphabet['['], alphabet['\''], alphabet[','], alphabet['"'], alphabet[';'],
                                    alphabet[':'], alphabet[' ']]
    alphabet['<digit>'].First = [alphabet['0'], alphabet['1'], alphabet['2'], alphabet['3'], alphabet['4'],
                                  alphabet['5'], alphabet['6'], alphabet['7'], alphabet['8'], alphabet['9']]

    # Last relations
    alphabet['<main>'].Last = [alphabet['<block>']]
    alphabet['<data_type>'].Last = [alphabet['int'], alphabet['float'], alphabet['string'],
                                    alphabet['bool'], alphabet['void']]
    alphabet['<param_list>'].Last = [alphabet['<param_list>']]
    alphabet['<variable>'].Last = [alphabet['<name>']]
    alphabet['<constant>'].Last = [alphabet['<number>'], alphabet['<string>'],
                                    alphabet['true'], alphabet['false']]
    alphabet['<block>'].Last = [alphabet['}']]
    alphabet['<block_body>'].Last = [alphabet['<source_code_string>'], alphabet['<block_body>']]
    alphabet['<source_code_string>'].Last = [alphabet['\\n']]
    alphabet['<sc_element>'].Last = [alphabet['<variable>'], alphabet['<inp>'], alphabet['<out>'],
                                      alphabet['<if_expression>'], alphabet['<arithmetic_expression>'],
                                      alphabet['<for_cycle>']]
    alphabet['<inp>'].Last = [alphabet[')']]
    alphabet['<out>'].Last = [alphabet[')']]
    alphabet['<if_expression>'].Last = [alphabet['<block>']]
    alphabet['<arithmetic_expression>'].Last = [alphabet['<arithmetic_expression_body>']]
    alphabet['<arithmetic_expression_body>'].Last = [alphabet['<arithmetic_expression_body>']]
    alphabet['<term>'].Last = [alphabet['<multiplier>'], alphabet['<term>']]
    alphabet['<multiplier>'].Last = [alphabet['<mp_body>']]
    alphabet['<mp_body>'].Last = [alphabet[')'], alphabet['<value>']]
    alphabet['<value>'].Last = [alphabet['<number>'], alphabet['<name>']]
    alphabet['<operator_1lvl>'].Last = [alphabet['+'], alphabet['-']]
    alphabet['<operator_2lvl>'].Last = [alphabet['*'], alphabet['/'], alphabet['%']]
    alphabet['<for_cycle>'].Last = [alphabet['<block>']]
    alphabet['<input_param_list>'].Last = [alphabet['<name>'], alphabet['<constant>'],
                                            alphabet['<input_param_list>']]
    alphabet['<name>'].Last = [alphabet['<name_tail>']]
    alphabet['<name_tail>'].Last = [alphabet['<digit>'], alphabet['<letter>'], alphabet['<name_tail>']]
    alphabet['<number>'].Last = [alphabet['<int>'], alphabet['<float>']]
    alphabet['<bool_expression>'].Last = [alphabet['<comparable>'], alphabet['true'], alphabet['false']]
    alphabet['<comparable>'].Last = [alphabet['<name>'], alphabet['<constant>']]
    alphabet['<bool_operator>'].Last = [alphabet['<'], alphabet['>'], alphabet['<='], alphabet['>='],
                                         alphabet['!='], alphabet['==']]
    alphabet['<char>'].Last = [alphabet['<letter>'], alphabet['<splitter>']]
    alphabet['<int>'].Last = [alphabet['<digit>'], alphabet['<int>']]
    alphabet['<float>'].Last = [alphabet['<int>']]
    alphabet['<string>'].Last = [alphabet['"']]
    alphabet['<text>'].Last = [alphabet['<text>']]
    alphabet['<comment>'].Last = [alphabet['<text>']]
    alphabet['<letter>'].Last = [alphabet['a'], alphabet['b'], alphabet['c'], alphabet['d'], alphabet['e'],
                                 alphabet['f'], alphabet['g'], alphabet['h'], alphabet['i'], alphabet['j'],
                                 alphabet['k'], alphabet['l'], alphabet['m'], alphabet['n'], alphabet['o'],
                                 alphabet['p'], alphabet['q'], alphabet['r'], alphabet['s'], alphabet['t'],
                                 alphabet['u'], alphabet['v'], alphabet['w'], alphabet['x'], alphabet['y'],
                                 alphabet['z'],
                                 alphabet['A'], alphabet['B'], alphabet['C'], alphabet['D'], alphabet['E'],
                                 alphabet['F'], alphabet['G'], alphabet['H'], alphabet['I'], alphabet['J'],
                                 alphabet['K'], alphabet['L'], alphabet['M'], alphabet['N'], alphabet['O'],
                                 alphabet['P'], alphabet['Q'], alphabet['R'], alphabet['S'], alphabet['T'],
                                 alphabet['U'], alphabet['V'], alphabet['W'], alphabet['X'], alphabet['Y'],
                                 alphabet['Z'],
                                 alphabet['_']]
    alphabet['<splitter>'].Last = [alphabet['.'], alphabet[','], alphabet['!'], alphabet['?'], alphabet['\\n'],
                                   alphabet['\\t'], alphabet['<'], alphabet['>'], alphabet['<='], alphabet['>='],
                                   alphabet['!='], alphabet['=='], alphabet['&'],  alphabet['`'], alphabet['#'],
                                   alphabet['='], alphabet['+'],  alphabet['-'], alphabet['*'], alphabet['/'],
                                   alphabet['%'], alphabet['('], alphabet[')'], alphabet['{'], alphabet['}'],
                                   alphabet['['], alphabet['\''], alphabet[','], alphabet['"'], alphabet[';'],
                                   alphabet[':'], alphabet[' ']]
    alphabet['<digit>'].Last = [alphabet['0'], alphabet['1'], alphabet['2'], alphabet['3'], alphabet['4'],
                                 alphabet['5'], alphabet['6'], alphabet['7'], alphabet['8'], alphabet['9']]

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