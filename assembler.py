import sys
import re
from binary_maps import comp_map, dest_map, jump_map

def translate_a_instruction(line):
    opt_code = line[0]
    address_decimal = int(line[1:])
    address_binary = '{:015b}'.format(address_decimal)
    return address_binary

def assemble_destination(dest):
    return dest_map[dest]

def assemble_jump(jump):
    return jump_map[jump]

def assemble_compute(comp):
    return comp_map[comp]

def assemble_c_instruction(parts):
    dest = parts[0]
    comp = parts[1]
    jump = ''
    if len(parts) > 2:
        jump = parts[2]
    junk = '11'
    return junk + assemble_compute(comp) + assemble_destination(dest) + assemble_jump(jump)

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
        count = 0
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
