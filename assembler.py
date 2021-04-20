import sys
import re

dest_map = {
        'null': '000',
        'M'   : '001',
        'D'   : '010',
        'MD'  : '011',
        'A'   : '100',
        'AM'  : '101',
        'AD'  : '110',
        'AMD' : '111'
        }

jump_map = {
        'null': '000',
        'JGT' : '001',
        'JEQ' : '010',
        'JGE' : '011',
        'JLT' : '100',
        'JNE' : '101',
        'JLE' : '110',
        'JMP' : '111'
        }

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
    c = [None] * 7
    
    result = re.search(r'\W', comp) # search for non-lettter chars \W 
    if result:
        operator = result.group()
    
    if result and operator:
        res = split(comp, operator)

    else: # no operator: assignment without negation eg.D=A, D=1
        c[0] = 0
        c[1] = 0
        c[2] = 0
        c[3] = 0
        c[4] = 0
        c[5] = 0 #no operator -> no + or & operator
        c[6] = 0 #no operator -> no ! operator
        #identify operand/constant
        if comp == 'A':
            c[1] = 1
            c[2] = 1
        elif comp == 'D':
            c[3] = 1
            c[4] = 1
        elif comp == 'M':
            c[0] = 1
            c[1] = 1
            c[2] = 1

    if (any(x is None for x in c)):
        raise ValueError("Can't translate c-instruction")
    
    return ''.join(map(str, c))

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
    line_no_whitespace = re.sub(r'[\s\n]', '', line.content)
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
