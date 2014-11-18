"""
For using this analyzer you may pas into stdin few files at special order:
    * first argument is input file
    * optional second argument is output file for json notation
    * optional third argument is output file for main tokens table
    * optional fourth argument is output file for variable tokens table
    * optional fifth argument is output file for constant tokens table

ATTENTION:    I guess that all files is located in runtime directory!

:author Mike Bohdan
:version 1.0.1
:date November 16, 2014
:licence GPLv2

Good luck and have fun with this simple lexical analyzer for hobbit programming language.
"""

import json
from os import getcwd
from sys import argv
from tokenizer import Tokenizer
try:
    input_file = open(getcwd()+'/'+argv[1])

    # analyzing of input file
    tz = Tokenizer(file_to_analyze=input_file)
    try:
        tz = tz.analyze()
    except Exception as e:
        print(e)
    input_file.close()

    # writing analyzed data to json file
    try:
        output_file = open(getcwd()+'/'+argv[2], 'w')
    except Exception:
        output_file = open(getcwd()+'/output.json', 'w')
    json.dump({'tokens':       [i.toDict() for i in tz['tokens']],
               'variables':    [i.toDict() for i in tz['variables']],
               'constants':    [i.toDict() for i in tz['constants']]},
              output_file, separators=(',', ':'), indent=4)
    output_file.close()

    # writing tokens table into simple txt file for better reading experience
    try:
        output_token_file = open(getcwd()+'/'+argv[3], 'w')
        for token in tz['tokens']:
            output_token_file.write(token.__str__()+'\n')
        output_token_file.close()
    except Exception:
        pass

    # writing variables table into simple txt file for better reading experience
    try:
        output_variables_file = open(getcwd()+'/'+argv[4], 'w')
        for variable in tz['variables']:
            output_variables_file.write(variable.__str__()+'\n')
        output_variables_file.close()
    except Exception:
        pass

    # writing constants table into simple txt file for better reading experience
    try:
        output_constants_file = open(getcwd()+'/'+argv[5], 'w')
        for constant in tz['constants']:
            output_constants_file.write(constant.__str__()+'\n')
        output_constants_file.close()
    except Exception:
        pass

except Exception as e:
    print("Hobbit token analyzer version 1.0")
    print()
    print("You must input date in special format:")
    print("\thobbit.py <input file>"+
          "[<output json file>] [<output tokens txt file>] [<output variable table>] [<output constant table>]")