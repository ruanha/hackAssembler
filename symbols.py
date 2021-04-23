symbol_table = {
    'R0'     : 0,
    'R1'     : 1,
    'R2'     : 2,
    'R3'     : 3,
    'R4'     : 4,
    'R5'     : 5,
    'R6'     : 6,
    'R7'     : 7,
    'R8'     : 8,
    'R9'     : 9,
    'R10'    : 10,
    'R11'    : 11,
    'R12'    : 12,
    'R13'    : 13,
    'R14'    : 14,
    'R15'    : 15,
    'SCREEN' : 16384,
    'KBD'    : 24576,
    'SP'     : 0,
    'LCL'    : 1,
    'ARG'    : 2,
    'THIS'   : 3,
    'THAT'   : 4
    }

def create_symbol_table(file):
    #first pass
    count = 0
    for line in file:
        if (line[0] == '('):
            symbol = line.replace('(', '').replace(')', '')
            symbol_table[symbol] = count + 1
        count = count + 1
    
    #second pass
    count = 16
    for line in file:
        if (line[0] == '@' and type(line[1]) != int):
            symbol = line[1:]
            if (symbol not in symbol_table):
                symbol_table[symbol] = count
                count = count + 1

    return symbol_table


