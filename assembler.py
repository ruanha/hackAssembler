import sys

if len(sys.argv) !=2:
    raise ValueError('Please provide the name of an assembler file as the only argument.')

def translate_a_instruction(line):
    opt_code = line[0]
    address_decimal = int(line[1:])
    address_binary = '{:015b}'.format(address_decimal)
    return address_binary

def main(filename):
    basename = filename.split('.')[0]
    with open(filename, "r") as asm_file, open(basename+'.hack', 'w') as output_file:
        for line in asm_file:
            if (line[0] == "@"):
                output_file.write('0' + translate_a_instruction(line) + '\n')

if __name__ == "__main__":
    filename = sys.argv[1]

    main(filename)
