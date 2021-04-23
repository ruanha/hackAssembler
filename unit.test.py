from assembler import translate_a_instruction, assemble_destination, assemble_jump, assemble_compute
from symbols import symbol_table, create_symbol_table

assert translate_a_instruction('@1') == '000000000000001', "should be 000000000000001"
assert translate_a_instruction('@9') == '000000000001001', "should be 000000000001001"

# Test assemble_destination
assert assemble_destination('null') == '000', 'should be 000'
assert assemble_destination('MD') == '011', 'should be 011'

# Test assemble_jump
assert assemble_jump('null') == '000', 'should be 000'
assert assemble_jump('JLT') == '100', 'should be 100'

# Test assemble_compute
assert assemble_compute('D') == '0001100'
assert assemble_compute('A') == '0110000'
assert assemble_compute('M') == '1110000'

# Test symbol table
def test_predefined_symbols(table):
    assert create_symbol_table([]) == table, 'should return the symbol_table'

def test_label_symbols(table):
    table['LOOP'] = 1
    assert create_symbol_table(['(LOOP)', '@12', 'D=A','@LOOP','0;JMP']) == table, 'should equal the symbol_table with LOOP: 1, added'

def test_variable_symbols(table):
    table['my_var'] = 16
    table['my_second_var'] = 17
    assert create_symbol_table(['@my_var', '123', '@43', 'M=D', 'my_second_var', '89']) == table

test_predefined_symbols(symbol_table)
test_label_symbols(symbol_table)
test_variable_symbols(symbol_table)
print('All tests passed')

