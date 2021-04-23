import sys
import os
from instructions import *  

def main(filepath):
    basename = os.path.basename(filepath).split('.')[0]
    with open(filepath, "r") as asm_file, open(basename + '.hack', 'w') as output_file:
        count = 0
        for line in asm_file:    
            if (line[0] == "@"):
                output_file.write('0' + translate_a_instruction(line) + '\n')
            elif (line[0] != '/' and line[0].strip() != ''):
                output_file.write('1' + translate_c_instruction(line) + '\n')

if __name__ == "__main__":
    if len(sys.argv) !=2:
        raise ValueError('Please provide the name of an assembler file as the only argument.')
    filepath = sys.argv[1]

    main(filepath)
