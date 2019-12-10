inp_file = open("input.txt", 'r')
pz_inp = list(map(int, inp_file.readline().split(',')))

# pz_inp = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0]
# pz_inp = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
# pz_inp = [104, 1125899906842624, 99]

for i in range(0, 200):
    pz_inp.append(0)


class Op:
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    RELATIVE_BASE = 9
    STOP = 99


class PMode:
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


def get_next_instruction_position_offset(operation):
    if operation is Op.ADD or operation is Op.MULTIPLY \
            or operation is Op.LESS_THAN or operation is Op.EQUALS:
        return 4
    elif operation is Op.INPUT or operation is Op.OUTPUT or Op.RELATIVE_BASE:
        return 2
    elif operation is Op.JUMP_IF_TRUE or operation is Op.JUMP_IF_FALSE:
        return 3


def param_for_read(m, p, pm, rb):
    if pm == PMode.IMMEDIATE:
        return p

    elif pm == PMode.POSITION:
        return m[p]

    elif pm == PMode.RELATIVE:
        return m[p + rb]


def param_for_write(m, p, pm, rb):
    if pm == PMode.POSITION:
        return p

    elif pm == PMode.RELATIVE:
        return p + rb


def op_add(m, p1, pm1, p2, pm2, p3, pm3, rb):
    p1 = param_for_read(m, p1, pm1, rb)
    p2 = param_for_read(m, p2, pm2, rb)
    p3 = param_for_write(m, p3, pm3, rb)

    m[p3] = p1 + p2


def op_multiply(m, p1, pm1, p2, pm2, p3, pm3, rb):
    p1 = param_for_read(m, p1, pm1, rb)
    p2 = param_for_read(m, p2, pm2, rb)
    p3 = param_for_write(m, p3, pm3, rb)

    m[p3] = p1 * p2


def op_input(m, p1, pm1, rb):
    p1 = param_for_write(m, p1, pm1, rb)
    m[p1] = int(input('Enter: '))


def op_output(m, p1, pm1, rb):
    if pm1 == PMode.IMMEDIATE:
        return p1
    else:
        return param_for_read(m, p1, pm1, rb)


def op_jump_if_true(m, i, p1, pm1, p2, pm2, rb):
    p1 = param_for_read(m, p1, pm1, rb)
    p2 = param_for_read(m, p2, pm2, rb)
    return p2 if p1 != 0 else i + 3


def op_jump_if_false(m, i, p1, pm1, p2, pm2, rb):
    p1 = param_for_read(m, p1, pm1, rb)
    p2 = param_for_read(m, p2, pm2, rb)
    return p2 if p1 == 0 else i + 3


def op_less_than(m, p1, pm1, p2, pm2, p3, pm3, rb):
    p1 = param_for_read(m, p1, pm1, rb)
    p2 = param_for_read(m, p2, pm2, rb)
    p3 = param_for_write(m, p3, pm3, rb)

    if p1 < p2:
        m[p3] = 1
    else:
        m[p3] = 0


def op_equals(m, p1, pm1, p2, pm2, p3, pm3, rb):
    p1 = param_for_read(m, p1, pm1, rb)
    p2 = param_for_read(m, p2, pm2, rb)
    p3 = param_for_write(m, p3, pm3, rb)

    if p1 == p2:
        m[p3] = 1
    else:
        m[p3] = 0


def op_relative_base(m, p1, pm1, rb):
    p1 = param_for_read(m, p1, pm1, rb)
    return rb + p1


def process(m):
    i = rb = 0
    count = 0
    while True:
        count += 1

        inst = m[i]

        op_code = inst % 100
        pm1 = int(inst / 100) % 10
        pm2 = int(inst / 1000) % 10
        pm3 = int(inst / 10000) % 10

        if op_code is Op.STOP:
            break

        elif op_code is Op.ADD:
            p1 = m[i + 1]
            p2 = m[i + 2]
            p3 = m[i + 3]
            op_add(m, p1, pm1, p2, pm2, p3, pm3, rb)

        elif op_code is Op.MULTIPLY:
            p1 = m[i + 1]
            p2 = m[i + 2]
            p3 = m[i + 3]
            op_multiply(m, p1, pm1, p2, pm2, p3, pm3, rb)

        elif op_code is Op.INPUT:
            op_input(m, m[i + 1], pm1, rb)

        elif op_code is Op.OUTPUT:
            p1 = m[i + 1]
            print(f'op: {op_output(m, p1, pm1, rb)}')

        elif op_code is Op.JUMP_IF_TRUE:
            p1 = m[i + 1]
            p2 = m[i + 2]
            i = op_jump_if_true(m, i, p1, pm1, p2, pm2, rb)
            continue

        elif op_code is Op.JUMP_IF_FALSE:
            p1 = m[i + 1]
            p2 = m[i + 2]
            i = op_jump_if_false(m, i, p1, pm1, p2, pm2, rb)
            continue

        elif op_code is Op.LESS_THAN:
            p1 = m[i + 1]
            p2 = m[i + 2]
            p3 = m[i + 3]
            op_less_than(m, p1, pm1, p2, pm2, p3, pm3, rb)

        elif op_code is Op.EQUALS:
            p1 = m[i + 1]
            p2 = m[i + 2]
            p3 = m[i + 3]
            op_equals(m, p1, pm1, p2, pm2, p3, pm3, rb)

        elif op_code is Op.RELATIVE_BASE:
            p1 = m[i + 1]
            rb = op_relative_base(m, p1, pm1, rb)

        i += get_next_instruction_position_offset(op_code)


process(pz_inp)
