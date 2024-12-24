from pathlib import Path
def solve(text):
    wires = {}
    gates = []
    
    for line in text.splitlines():
        if not line.strip():
            continue
        if ':' in line:
            name, value = line.strip().split(': ')
            wires[name] = int(value)
        else:
            inputs, output = line.split(' -> ')
            if 'AND' in inputs:
                a, b = inputs.split(' AND ')
                gates.append(('AND', a, b, output))
            elif 'XOR' in inputs:
                a, b = inputs.split(' XOR ')
                gates.append(('XOR', a, b, output))
            elif 'OR' in inputs:
                a, b = inputs.split(' OR ')
                gates.append(('OR', a, b, output))

    while gates:
        remaining_gates = []
        for gate_type, in1, in2, out in gates:
            if in1 in wires and in2 in wires:
                if gate_type == 'AND':
                    wires[out] = wires[in1] & wires[in2]
                elif gate_type == 'XOR':
                    wires[out] = wires[in1] ^ wires[in2]
                else:  
                    wires[out] = wires[in1] | wires[in2]
            else:
                remaining_gates.append((gate_type, in1, in2, out))
        gates = remaining_gates
    
    z_wires = [(k, v) for k, v in sorted(wires.items()) if k.startswith('z')]
    
    result = 0
    for _, bit in reversed(z_wires):  
        result = (result << 1) | bit
    return result
print(solve(Path("/Users/.../Advent-Of-Code/2024/input.txt").read_text()))