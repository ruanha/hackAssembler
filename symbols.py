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

def get_label(s):
    return s.replace('(', '').replace(')', '')

def is_label(c):
    return c[0] == '('

def is_symbol(c):
    return (c[0] == '@' and not c[1].isdigit())

def create_symbol_table(file):
    #first pass
    count = 0
    for line in file:
        if is_label(line):
            symbol = get_label(line)
            symbol_table[symbol] = count + 1
        count = count + 1
    
    #second pass
    count = 16
    for line in file:
        if (is_symbol(line)):
            symbol = line[1:]
            if (symbol not in symbol_table):
                symbol_table[symbol] = count
                count = count + 1
    print(symbol_table)
    return symbol_table

def replace_symbols(commands):
    symbol_table = create_symbol_table(commands)
    commandsL = []
    for command in commands:
        if is_symbol(command):
            commandsL.append( '@' + str( symbol_table[command[1:]] ) )
        elif not is_label(command):
            commandsL.append(command)
    return commandsL


