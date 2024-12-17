def parse_input(input_text):
    regs = {'A': 0, 'B': 0, 'C': 0}
    program = []
    for line in input_text.splitlines():
        if line.startswith('Register'):
            reg, val = line.split(': ')
            regs[reg[-1]] = int(val)
        elif line.startswith('Program:'):
            program = [int(x) for x in line.split(': ')[1].split(',')]
    return regs, program

def get_operand_value(operand, operand_type, regs):
    if operand_type == 'literal':
        return operand
    elif operand_type == 'combo':
        if operand <= 3:
            return operand
        elif operand == 4:
            return regs['A']
        elif operand == 5:
            return regs['B']
        elif operand == 6:
            return regs['C']
    return 0

def run_program(regs, program, max_steps=1000):
    outputs = []
    ip = 0
    steps = 0
    
    while ip < len(program) - 1 and steps < max_steps:
        steps += 1
        opcode = program[ip]
        operand = program[ip + 1]
        
        if opcode == 0:
            val = get_operand_value(operand, 'combo', regs)
            regs['A'] = regs['A'] // (1 << val) if val < 64 else 0
        elif opcode == 1:
            regs['B'] ^= operand
        elif opcode == 2:
            val = get_operand_value(operand, 'combo', regs) % 8
            regs['B'] = val
        elif opcode == 3:
            if regs['A'] != 0:
                ip = operand
                continue
        elif opcode == 4:
            regs['B'] ^= regs['C']
        elif opcode == 5:
            val = get_operand_value(operand, 'combo', regs) % 8
            outputs.append(val)
        elif opcode == 6:
            val = get_operand_value(operand, 'combo', regs)
            regs['B'] = regs['A'] // (1 << val) if val < 64 else 0
        elif opcode == 7:
            val = get_operand_value(operand, 'combo', regs)
            regs['C'] = regs['A'] // (1 << val) if val < 64 else 0
            
        ip += 2
        
        if len(outputs) >= len(program):
            break 
    return outputs
def solve(input_text):
    regs, program = parse_input(input_text)
    outputs = run_program(regs.copy(), program)
    part1 = ','.join(str(x) for x in outputs)    
    return part1

with open('/Users/.../Advent-Of-Code/2024/input.txt') as f:
    input_text = f.read()

part1 = solve(input_text)
print(part1)
