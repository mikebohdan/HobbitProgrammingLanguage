from DownTopAnalizer.Analyzer.common._element import Element

_alphabet = {}


def init():
    global _alphabet
    _alphabet = dict({
        # Non terminals
        '<main>': Element('<main>'),
        '<data_type>': Element('<data_type>'),
        '<param_list>': Element('<param_list>'),
        '<variable>': Element('<variable>'),
        '<constant>': Element('<constant>'),
        '<block>': Element('<block>'),
        '<block_body>': Element('<block_body>'),
        '<source_code_string>': Element('<source_code_string>'),
        '<sc_element>': Element('<sc_element>'),
        '<inp>': Element('<inp>'),
        '<out>': Element('<out>'),
        '<if_expression>': Element('<if_expression>'),
        '<arithmetic_expression>': Element('<arithmetic_expression>'),
        '<arithmetic_expression_body>': Element('<arithmetic_expression_body>'),
        '<term>': Element('<term>'),
        '<multiplier>': Element('<multiplier>'),
        '<mp_body>': Element('<mp_body>'),
        '<value>': Element('<value>'),
        '<operator_1lvl>': Element('<operator_1lvl>'),
        '<operator_2lvl>': Element('<operator_2lvl>'),
        '<for_cycle>': Element('<for_cycle>'),
        '<input_param_list>': Element('<input_param_list>'),
        '<name>': Element('<name>'),
        '<name_tail>': Element('<name_tail>'),
        '<number>': Element('<number>'),
        '<bool_expression>': Element('<bool_expression>'),
        '<comparable>': Element('<comparable>'),
        '<bool_operator>': Element('<bool_operator>'),
        '<char>': Element('<char>'),
        '<int>': Element('<int>'),
        '<float>': Element('<float>'),
        '<string>': Element('<string>'),
        '<text>': Element('<text>'),
        '<comment>': Element('<comment>'),
        '<letter>': Element('<letter>'),
        '<splitter>': Element('<splitter>'),
        '<digit>': Element('<digit>'),
        # =================

        # Terminals
        'int': Element('int'),
        'float': Element('float'),
        'string': Element('string'),
        'bool': Element('bool'),
        'void': Element('void'),
        'true': Element('true'),
        'false': Element('false'),
        '{': Element('{'),
        '}': Element('}'),
        '\\n': Element('\\n'),
        'in': Element('in'),
        'out': Element('out'),
        'if': Element('if'),
        '(': Element('('),
        ')': Element(')'),
        'else': Element('else'),
        '+': Element('+'),
        '-': Element('-'),
        '*': Element('*'),
        '/': Element('/'),
        '%': Element('%'),
        'for': Element('for'),
        'to': Element('to'),
        'do': Element('do'),
        ',': Element(','),
        '<': Element('<'),
        '>': Element('>'),
        '<=': Element('<='),
        '>=': Element('>='),
        '!=': Element('!='),
        '==': Element('=='),
        '.': Element('.'),
        'e': Element('e'),
        '"': Element('"'),
        '#': Element('#'),
        'a': Element('a'),
        'b': Element('b'),
        'c': Element('c'),
        'd': Element('d'),
        'f': Element('f'),
        'g': Element('g'),
        'h': Element('h'),
        'i': Element('i'),
        'j': Element('j'),
        'k': Element('k'),
        'l': Element('l'),
        'm': Element('m'),
        'n': Element('n'),
        'o': Element('o'),
        'p': Element('p'),
        'q': Element('q'),
        'r': Element('r'),
        's': Element('s'),
        't': Element('t'),
        'u': Element('u'),
        'v': Element('v'),
        'w': Element('w'),
        'x': Element('x'),
        'y': Element('y'),
        'z': Element('z'),
        'A': Element('A'),
        'B': Element('B'),
        'C': Element('C'),
        'D': Element('D'),
        'E': Element('E'),
        'F': Element('F'),
        'G': Element('G'),
        'H': Element('H'),
        'I': Element('I'),
        'J': Element('J'),
        'K': Element('K'),
        'L': Element('L'),
        'M': Element('M'),
        'N': Element('N'),
        'O': Element('O'),
        'P': Element('P'),
        'Q': Element('Q'),
        'R': Element('R'),
        'S': Element('S'),
        'T': Element('T'),
        'U': Element('U'),
        'V': Element('V'),
        'W': Element('W'),
        'X': Element('X'),
        'Y': Element('Y'),
        'Z': Element('Z'),
        '_': Element('_'),
        '\\t': Element('\\t'),
        ' ': Element(' '),
        '!': Element('!'),
        '?': Element('?'),
        '&': Element('&'),
        '`': Element('`'),
        '\'': Element('\''),
        ';': Element(';'),
        ':': Element(':'),
        '[': Element('['),
        ']': Element(']'),
        '0': Element('0'),
        '1': Element('1'),
        '2': Element('2'),
        '3': Element('3'),
        '4': Element('4'),
        '5': Element('5'),
        '6': Element('6'),
        '7': Element('7'),
        '8': Element('8'),
        '9': Element('9'),
        'ID': Element('ID'),
        '=': Element('=')
        # ==================
    })

    # Equal relations
    _alphabet['<data_type>'].Equals = [_alphabet['ID']]
    _alphabet['<param_list>'].Equals = [_alphabet[')']]
    _alphabet['<variable>'].Equals = [_alphabet[',']]
    _alphabet['<block>'].Equals = [_alphabet['else']]
    _alphabet['<block_body>'].Equals = [_alphabet['}']]
    _alphabet['<source_code_string>'].Equals = [_alphabet['<block_body>']]
    _alphabet['<sc_element>'].Equals = [_alphabet['\\n'], _alphabet['<comment>']]
    _alphabet['<arithmetic_expression>'].Equals = [_alphabet['to']]
    _alphabet['<arithmetic_expression_body>'].Equals = [_alphabet[')'], _alphabet['do']]
    _alphabet['<term>'].Equals = [_alphabet['<operator_1lvl>']]
    _alphabet['<multiplier>'].Equals = [_alphabet['<operator_2lvl>']]
    _alphabet['<operator_1lvl>'].Equals = [_alphabet['<arithmetic_expression_body>']]
    _alphabet['<operator_2lvl>'].Equals = [_alphabet['<term>']]
    _alphabet['<input_param_list>'].Equals = [_alphabet[')']]
    _alphabet['<name>'].Equals = [_alphabet['('], _alphabet['='], _alphabet[',']]
    _alphabet['<number>'].Equals = [_alphabet['<text>']]
    _alphabet['<bool_expression>'].Equals = [_alphabet[')']]
    _alphabet['<comparable>'].Equals = [_alphabet['<bool_operator>']]
    _alphabet['<bool_operator>'].Equals = [_alphabet['<comparable>']]
    _alphabet['<int>'].Equals = [_alphabet['.'], _alphabet['e']]
    _alphabet['<string>'].Equals = [_alphabet[','], _alphabet[')']]
    _alphabet['<text>'].Equals = [_alphabet['"']]
    _alphabet['<comment>'].Equals = [_alphabet['\\n']]
    _alphabet['<letter>'].Equals = [_alphabet['<name_tail>'], _alphabet['<text>']]
    _alphabet['<splitter>'].Equals = [_alphabet['<text>']]
    _alphabet['<digit>'].Equals = [_alphabet['<name_tail>'], _alphabet['<int>']]
    _alphabet['{'].Equals = [_alphabet['<block_body>']]
    _alphabet['in'].Equals = [_alphabet['(']]
    _alphabet['out'].Equals = [_alphabet['(']]
    _alphabet['if'].Equals = [_alphabet['(']]
    _alphabet['('].Equals = [_alphabet['<param_list>'], _alphabet['<input_param_list>'],
                             _alphabet['<string>'], _alphabet['<bool_expression>'],
                             _alphabet['<arithmetic_expression_body>']]
    _alphabet[')'].Equals = [_alphabet['<block>']]
    _alphabet['else'].Equals = [_alphabet['<block>']]
    _alphabet['+'].Equals = [_alphabet['<mp_body>']]
    _alphabet['-'].Equals = [_alphabet['<mp_body>'], _alphabet['<int>']]
    _alphabet['for'].Equals = [_alphabet['<arithmetic_expression>']]
    _alphabet['to'].Equals = [_alphabet['<arithmetic_expression_body>']]
    _alphabet['do'].Equals = [_alphabet['<block>']]
    _alphabet[','].Equals = [_alphabet['<param_list>']]
    _alphabet['.'].Equals = [_alphabet['<int>']]
    _alphabet['e'].Equals = [_alphabet['<int>'], _alphabet['-'], _alphabet['+']]
    _alphabet['"'].Equals = [_alphabet['<text>']]
    _alphabet['#'].Equals = [_alphabet['<text>']]
    _alphabet['='].Equals = [_alphabet['<arithmetic_expression_body>']]

    # First relations
    _alphabet['<main>'].First = [_alphabet['<data_type>']]
    _alphabet['<data_type>'].First = [_alphabet['int'], _alphabet['float'], _alphabet['string'],
                                      _alphabet['bool'], _alphabet['void']]
    _alphabet['<param_list>'].First = [_alphabet['<variable>']]
    _alphabet['<variable>'].First = [_alphabet['<data_type>']]
    _alphabet['<constant>'].First = [_alphabet['<number>'], _alphabet['<string>'],
                                     _alphabet['true'], _alphabet['false']]
    _alphabet['<block>'].First = [_alphabet['{']]
    _alphabet['<block_body>'].First = [_alphabet['<source_code_string>']]
    _alphabet['<source_code_string>'].First = [_alphabet['<sc_element>'], _alphabet['\\n']]
    _alphabet['<sc_element>'].First = [_alphabet['<variable>'], _alphabet['<inp>'], _alphabet['<out>'],
                                       _alphabet['<if_expression>'], _alphabet['<arithmetic_expression>'],
                                       _alphabet['<for_cycle>']]
    _alphabet['<inp>'].First = [_alphabet['in']]
    _alphabet['<out>'].First = [_alphabet['out']]
    _alphabet['<if_expression>'].First = [_alphabet['if']]
    _alphabet['<arithmetic_expression>'].First = [_alphabet['<name>']]
    _alphabet['<arithmetic_expression_body>'].First = [_alphabet['<term>']]
    _alphabet['<term>'].First = [_alphabet['<multiplier>']]
    _alphabet['<multiplier>'].First = [_alphabet['+'], _alphabet['-'], _alphabet['<mp_body>']]
    _alphabet['<mp_body>'].First = [_alphabet['('], _alphabet['<value>']]
    _alphabet['<value>'].First = [_alphabet['<number>'], _alphabet['<name>']]
    _alphabet['<operator_1lvl>'].First = [_alphabet['+'], _alphabet['-']]
    _alphabet['<operator_2lvl>'].First = [_alphabet['*'], _alphabet['/'], _alphabet['%']]
    _alphabet['<for_cycle>'].First = [_alphabet['for']]
    _alphabet['<input_param_list>'].First = [_alphabet['<name>'], _alphabet['<constant>']]
    _alphabet['<name>'].First = [_alphabet['<letter>']]
    _alphabet['<name_tail>'].First = [_alphabet['<digit>'], _alphabet['<letter>']]
    _alphabet['<number>'].First = [_alphabet['<int>'], _alphabet['<float>']]
    _alphabet['<bool_expression>'].First = [_alphabet['<comparable>'], _alphabet['true'], _alphabet['false']]
    _alphabet['<comparable>'].First = [_alphabet['<name>'], _alphabet['<constant>']]
    _alphabet['<bool_operator>'].First = [_alphabet['<'], _alphabet['>'], _alphabet['<='], _alphabet['>='],
                                          _alphabet['!='], _alphabet['==']]
    _alphabet['<char>'].First = [_alphabet['<letter>'], _alphabet['<splitter>']]
    _alphabet['<int>'].First = [_alphabet['<digit>']]
    _alphabet['<float>'].First = [_alphabet['<int>']]
    _alphabet['<string>'].First = [_alphabet['"']]
    _alphabet['<text>'].First = [_alphabet['<letter>'], _alphabet['<number>'], _alphabet['<splitter>']]
    _alphabet['<comment>'].First = [_alphabet['#']]
    _alphabet['<letter>'].First = [_alphabet['a'], _alphabet['b'], _alphabet['c'], _alphabet['d'], _alphabet['e'],
                                   _alphabet['f'], _alphabet['g'], _alphabet['h'], _alphabet['i'], _alphabet['j'],
                                   _alphabet['k'], _alphabet['l'], _alphabet['m'], _alphabet['n'], _alphabet['o'],
                                   _alphabet['p'], _alphabet['q'], _alphabet['r'], _alphabet['s'], _alphabet['t'],
                                   _alphabet['u'], _alphabet['v'], _alphabet['w'], _alphabet['x'], _alphabet['y'],
                                   _alphabet['z'],
                                   _alphabet['A'], _alphabet['B'], _alphabet['C'], _alphabet['D'], _alphabet['E'],
                                   _alphabet['F'], _alphabet['G'], _alphabet['H'], _alphabet['I'], _alphabet['J'],
                                   _alphabet['K'], _alphabet['L'], _alphabet['M'], _alphabet['N'], _alphabet['O'],
                                   _alphabet['P'], _alphabet['Q'], _alphabet['R'], _alphabet['S'], _alphabet['T'],
                                   _alphabet['U'], _alphabet['V'], _alphabet['W'], _alphabet['X'], _alphabet['Y'],
                                   _alphabet['Z'],
                                   _alphabet['_']]
    _alphabet['<splitter>'].First = [_alphabet['.'], _alphabet[','], _alphabet['!'], _alphabet['?'], _alphabet['\\n'],
                                     _alphabet['\\t'], _alphabet['<'], _alphabet['>'], _alphabet['<='], _alphabet['>='],
                                     _alphabet['!='], _alphabet['=='], _alphabet['&'],  _alphabet['`'], _alphabet['#'],
                                     _alphabet['='], _alphabet['+'],  _alphabet['-'], _alphabet['*'], _alphabet['/'],
                                     _alphabet['%'], _alphabet['('], _alphabet[')'], _alphabet['{'], _alphabet['}'],
                                     _alphabet['['], _alphabet['\''], _alphabet[','], _alphabet['"'], _alphabet[';'],
                                     _alphabet[':'], _alphabet[' ']]
    _alphabet['<digit>'].First = [_alphabet['0'], _alphabet['1'], _alphabet['2'], _alphabet['3'], _alphabet['4'],
                                  _alphabet['5'], _alphabet['6'], _alphabet['7'], _alphabet['8'], _alphabet['9']]

    # Last relations
    _alphabet['<main>'].Last = [_alphabet['<block>']]
    _alphabet['<data_type>'].Last = [_alphabet['int'], _alphabet['float'], _alphabet['string'],
                                    _alphabet['bool'], _alphabet['void']]
    _alphabet['<param_list>'].Last = [_alphabet['<param_list>']]
    _alphabet['<variable>'].Last = [_alphabet['<name>']]
    _alphabet['<constant>'].Last = [_alphabet['<number>'], _alphabet['<string>'],
                                    _alphabet['true'], _alphabet['false']]
    _alphabet['<block>'].Last = [_alphabet['}']]
    _alphabet['<block_body>'].Last = [_alphabet['<source_code_string>'], _alphabet['<block_body>']]
    _alphabet['<source_code_string>'].Last = [_alphabet['\\n']]
    _alphabet['<sc_element>'].Last = [_alphabet['<variable>'], _alphabet['<inp>'], _alphabet['<out>'],
                                      _alphabet['<if_expression>'], _alphabet['<arithmetic_expression>'],
                                      _alphabet['<for_cycle>']]
    _alphabet['<inp>'].Last = [_alphabet[')']]
    _alphabet['<out>'].Last = [_alphabet[')']]
    _alphabet['<if_expression>'].Last = [_alphabet['<block>']]
    _alphabet['<arithmetic_expression>'].Last = [_alphabet['<arithmetic_expression_body>']]
    _alphabet['<arithmetic_expression_body>'].Last = [_alphabet['<arithmetic_expression_body>']]
    _alphabet['<term>'].Last = [_alphabet['<multiplier>'], _alphabet['<term>']]
    _alphabet['<multiplier>'].Last = [_alphabet['<mp_body>']]
    _alphabet['<mp_body>'].Last = [_alphabet[')'], _alphabet['<value>']]
    _alphabet['<value>'].Last = [_alphabet['<number>'], _alphabet['<name>']]
    _alphabet['<operator_1lvl>'].Last = [_alphabet['+'], _alphabet['-']]
    _alphabet['<operator_2lvl>'].Last = [_alphabet['*'], _alphabet['/'], _alphabet['%']]
    _alphabet['<for_cycle>'].Last = [_alphabet['<block>']]
    _alphabet['<input_param_list>'].Last = [_alphabet['<name>'], _alphabet['<constant>'],
                                            _alphabet['<input_param_list>']]
    _alphabet['<name>'].Last = [_alphabet['<name_tail>']]
    _alphabet['<name_tail>'].Last = [_alphabet['<digit>'], _alphabet['<letter>'], _alphabet['<name_tail>']]
    _alphabet['<number>'].Last = [_alphabet['<int>'], _alphabet['<float>']]
    _alphabet['<bool_expression>'].Last = [_alphabet['<comparable>'], _alphabet['true'], _alphabet['false']]
    _alphabet['<comparable>'].Last = [_alphabet['<name>'], _alphabet['<constant>']]
    _alphabet['<bool_operator>'].Last = [_alphabet['<'], _alphabet['>'], _alphabet['<='], _alphabet['>='],
                                         _alphabet['!='], _alphabet['==']]
    _alphabet['<char>'].Last = [_alphabet['<letter>'], _alphabet['<splitter>']]
    _alphabet['<int>'].Last = [_alphabet['<digit>'], _alphabet['<int>']]
    _alphabet['<float>'].Last = [_alphabet['<int>']]
    _alphabet['<string>'].Last = [_alphabet['"']]
    _alphabet['<text>'].Last = [_alphabet['<text>']]
    _alphabet['<comment>'].Last = [_alphabet['<text>']]
    _alphabet['<letter>'].Last = [_alphabet['a'], _alphabet['b'], _alphabet['c'], _alphabet['d'], _alphabet['e'],
                                  _alphabet['f'], _alphabet['g'], _alphabet['h'], _alphabet['i'], _alphabet['j'],
                                  _alphabet['k'], _alphabet['l'], _alphabet['m'], _alphabet['n'], _alphabet['o'],
                                  _alphabet['p'], _alphabet['q'], _alphabet['r'], _alphabet['s'], _alphabet['t'],
                                  _alphabet['u'], _alphabet['v'], _alphabet['w'], _alphabet['x'], _alphabet['y'],
                                  _alphabet['z'],
                                  _alphabet['A'], _alphabet['B'], _alphabet['C'], _alphabet['D'], _alphabet['E'],
                                  _alphabet['F'], _alphabet['G'], _alphabet['H'], _alphabet['I'], _alphabet['J'],
                                  _alphabet['K'], _alphabet['L'], _alphabet['M'], _alphabet['N'], _alphabet['O'],
                                  _alphabet['P'], _alphabet['Q'], _alphabet['R'], _alphabet['S'], _alphabet['T'],
                                  _alphabet['U'], _alphabet['V'], _alphabet['W'], _alphabet['X'], _alphabet['Y'],
                                  _alphabet['Z'],
                                  _alphabet['_']]
    _alphabet['<splitter>'].Last = [_alphabet['.'], _alphabet[','], _alphabet['!'], _alphabet['?'], _alphabet['\\n'],
                                    _alphabet['\\t'], _alphabet['<'], _alphabet['>'], _alphabet['<='], _alphabet['>='],
                                    _alphabet['!='], _alphabet['=='], _alphabet['&'],  _alphabet['`'], _alphabet['#'],
                                    _alphabet['='], _alphabet['+'],  _alphabet['-'], _alphabet['*'], _alphabet['/'],
                                    _alphabet['%'], _alphabet['('], _alphabet[')'], _alphabet['{'], _alphabet['}'],
                                    _alphabet['['], _alphabet['\''], _alphabet[','], _alphabet['"'], _alphabet[';'],
                                    _alphabet[':'], _alphabet[' ']]
    _alphabet['<digit>'].Last = [_alphabet['0'], _alphabet['1'], _alphabet['2'], _alphabet['3'], _alphabet['4'],
                                 _alphabet['5'], _alphabet['6'], _alphabet['7'], _alphabet['8'], _alphabet['9']]

    # FirstPlus relations
    for i in _alphabet:
        _alphabet[i].findFirstPlus()

    # LastPlus relations
    #_alphabet['<block_body>'].findLastPlus()
    for i in _alphabet:
        _alphabet[i].findLastPlus()


if __name__ == '__main__':
    init()
    for i in _alphabet:
        print("{:30}".format(i), [j.name for j in _alphabet[i].Equals])