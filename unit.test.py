from assembler import translate_a_instruction

assert translate_a_instruction('@1') == '000000000000001', "should be 000000000000001"

print('All tests passed')

