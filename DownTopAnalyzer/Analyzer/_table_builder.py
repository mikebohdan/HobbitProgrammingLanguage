from collections import OrderedDict
from Analyzer.common import init, Element


def create_table():
    alphabet = init()
    t = len(alphabet)

    table = OrderedDict(
        [
            (
                ti, OrderedDict([
                    (tj, '')
                    for tj in alphabet
                ])
            )
            for ti in alphabet
        ]
    )

    # Step 1
    for i in alphabet:
        for j in alphabet[i].Equals:
            if table[i][j.name] == '=':
                continue
            table[i][j.name] += '='

    # Step 2
    for i in alphabet:

        for j in alphabet[i].LastPlus:
            # for all elements before vertical bold line
            if not Element.is_non_terminal(j):
                break
            table[i][j.name] += '<'

    # Step 3
    for i in alphabet:
        # for all elements before horizontal bold line
        if not Element.is_non_terminal(alphabet[i]):
            break

        for j in alphabet[i].Equals:
            # A <element> = <another_element>
            if Element.is_non_terminal(j):
                # for all elements in <element> LastPlus
                for pi in alphabet[i].LastPlus:
                    # for all elements in <another_element> FirstPlus
                    for pj in j.FirstPlus:
                        try:
                            if table[pi.name][pj.name][-1] == '>':
                                continue
                        except IndexError:
                            pass
                        table[pi.name][pj.name] += '>'
            # B <element> = another_element
            else:
                # for all elements in <element> LastPlus
                for pi in alphabet[i].LastPlus:
                    try:
                        if table[pi.name][j.name][-1] == '>':
                            continue
                    except IndexError:
                        pass
                    table[pi.name][j.name] += '>'

    return table

if __name__ == '__main__':
    table = create_table()

    for i in table:
        for j in table[i]:
            print('[{:2}]'.format(table[i][j]), end='')
        print()