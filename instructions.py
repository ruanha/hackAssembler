from binary_maps import *
import re

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

def assemble_c_instruction(dest, comp, jump):
    junk = '11'
    return junk + assemble_compute(comp) + assemble_destination(dest) + assemble_jump(jump)

def translate_c_instruction(line):
    split_at_equal = line.split('=')
    dest = 'null'
    comp = 'null'
    jump = 'null'
    if (len(split_at_equal) == 1):
        comp, jump = split_at_equal[0].split(';')
    else:
        dest = split_at_equal[0]
        split_at_semi = split_at_equal[1].split(';')
        if (len(split_at_semi) == 1):
            comp = split_at_semi[0]
        else:
            comp, jump = split_at_semi
    return assemble_c_instruction(dest, comp, jump)
 
