from assembler import translate_a_instruction, assemble_destination, assemble_jump, assemble_compute

assert translate_a_instruction('@1') == '000000000000001', "should be 000000000000001"
assert translate_a_instruction('@9') == '000000000001001', "should be 000000000001001"

# Test assemble_destination
assert assemble_destination('null') == '000', 'should be 000'
assert assemble_destination('MD') == '011', 'should be 011'

# Test assemble_jump
assert assemble_jump('null') == '000', 'should be 000'
assert assemble_jump('JLT') == '100', 'should be 100'

# Test assemble_compute
assert assemble_compute('D-A') == '010011'
assert assemble_compute('A+1') == '110111'

print('All tests passed')

