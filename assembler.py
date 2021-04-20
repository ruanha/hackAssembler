import sys

if len(sys.argv) !=2:
    raise ValueError('Please provide the name of an assembler file as the only argument.')

def main(filename):
    basename = filename.split('.')[0]
    with open(filename, "r") as asm_file, open(basename+'.hack', 'w') as output_file:
        data = asm_file.read()
        print(data)

if __name__ == "__main__":
    filename = sys.argv[1]

    main(filename)
