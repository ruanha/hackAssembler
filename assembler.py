import sys
import os
from instructions import *  
from symbols import replace_symbols

def main(filepath):

    commands = []
    with open(filepath, 'r') as asm_file:
        for line in asm_file:
            #remove all whitespace
            clean = re.sub(r'[\s\n]', '', line)
            if ( len(clean) > 0 and line[0] != '/' ):
                commands.append(clean)

    commandsL = replace_symbols(commands)

    basename = os.path.basename(filepath).split('.')[0]
    with open(basename + '.hack', 'w') as output_file:
        for command in commandsL: 
            if (command[0] == "@"):
                output_file.write('0' + translate_a_instruction(command) + '\n')
            else:
                output_file.write('1' + translate_c_instruction(command) + '\n')

if __name__ == "__main__":
    if len(sys.argv) !=2:
        raise ValueError('Please provide the name of an assembler file as the only argument.')
    filepath = sys.argv[1]

    main(filepath)
