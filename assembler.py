import sys
import re

dest_map = {
        'null': '000',
        'M': '001',
        'D': '010',
        'MD': '011',
        'A': '100',
        'AM': '101',
        'AD': '110',
        'AMD': '111'
        }

def translate_a_instruction(line):
    opt_code = line[0]
    address_decimal = int(line[1:])
    address_binary = '{:015b}'.format(address_decimal)
    return address_binary

def assemble_destination(dest):
    return dest_map[dest]

def assemble_c_instruction(parts):
    assembly = ''
    dest = parts[0]
    comp = parts[1]
    if len(parts > 2):
        jump = parts[2]
    return assemble_destination(dest)

def translate_c_instruction(line):
    #remove all whitespace
    #split at '=' and ';' to get dest = comp ; jump
    line_no_whitespace = re.sub(r'[\s\n]', '', line)
    parts = re.split(r'[=;]', line_no_whitespace)
    assemble_c_instruction(parts)
    return '1110000111111111'
   

def main(filename):
    basename = filename.split('.')[0]
    with open(filename, "r") as asm_file, open(basename+'.hack', 'w') as output_file:
        for line in asm_file:
            if (line[0] == "@"):
                output_file.write('0' + translate_a_instruction(line) + '\n')
            else:
                output_file.write('1' + translate_c_instruction(line) + '\n')
            # TODO handle comments

if __name__ == "__main__":
    if len(sys.argv) !=2:
        raise ValueError('Please provide the name of an assembler file as the only argument.')

    filename = sys.argv[1]

    main(filename)
