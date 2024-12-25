data = open("input.txt").read().splitlines()
reg_a = int(data[0].split(":")[1])
reg_b = int(data[1].split(":")[1])
reg_c = int(data[2].split(":")[1])
program = data[4].split(" ")[1].split(",")
int_program = [int(x) for x in program]

print(f"register a: {reg_a}, register b: {reg_b}, register c: {reg_c}, program: {program}")

def combo_operand_to_value(operand):
    match operand:
        case '0':
            return 0
        case '1':
            return 1
        case '2':
            return 2
        case '3':
            return 3
        case '4':
            return reg_a
        case '5':
            return reg_b
        case '6':
            return reg_c

def power_of_two(p):
    res = 1
    for _ in range(p):
        res <<= 1

    return res

print(power_of_two(3))

def execute_op_code(opcode, x, ip, result):
    global reg_a, reg_b, reg_c
    new_ip = ip
    match opcode:
        case '0':
            reg_a = int(reg_a/power_of_two(combo_operand_to_value(x)))
            new_ip += 2
        case '1':
            reg_b = reg_b ^ int(x)
            new_ip += 2
        case '2':
            reg_b = combo_operand_to_value(x) & 0b111
            new_ip += 2
        case '3':
            if reg_a != 0:
                new_ip = int(x)
            else:
                new_ip += 2
        case '4':
            reg_b = reg_b ^ reg_c
            new_ip += 2
        case '5':
            result.append(combo_operand_to_value(x) & 0b111)
            new_ip += 2
        case '6':
            reg_b = int(reg_a/power_of_two(combo_operand_to_value(x)))
            new_ip += 2
        case '7':
            reg_c = int(reg_a/power_of_two(combo_operand_to_value(x)))
            new_ip += 2
        
    return new_ip

def run_program(program, val):
    global reg_a
    reg_a = val
    ip = 0
    result = []
    while ip < len(program):
        ip = execute_op_code(program[ip], program[ip+1], ip, result)

    return result


reg_a_list = [0b0000, 0b0001, 0b0010, 0b0011, 0b0100, 0b0101, 0b0110, 0b0111]

a = 0
res = []
queue = [0]


while len(res) < len(int_program):
    a = queue.pop(0)
    a = a << 3
    for num in reg_a_list:
        res = run_program(program, a+num)
        if res == int_program[len(int_program) - len(res):]:
            print(res)
            queue.append(a+num)
            print(f"Found solution: {a+num}")




