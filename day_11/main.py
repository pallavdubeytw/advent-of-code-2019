inp_file = open("input.txt", 'r')
pz_inp = list(map(int, inp_file.readline().split(',')))

for i in range(0, 999):
    pz_inp.append(0)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x},{self.y}'

    def __repr__(self):
        return self.__str__()


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


class Move:
    Left = 0
    Right = 1


class Color:
    Black = False
    White = True


class Task:
    Move = 0
    Paint = 1


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


def op_input(m, p1, pm1, rb, inp):
    p1 = param_for_write(m, p1, pm1, rb)
    # m[p1] = int(input('Enter: '))
    m[p1] = inp


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


def process(m, inp):
    dc = {}
    i = rb = 0
    count = 0
    origin = Point(10, 10)
    current_point = origin
    current_dir = 'u'
    task = Task.Paint
    while True:
        count += 1
        # print(f'count: {count}')
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
            op_input(m, m[i + 1], pm1, rb, inp[0])
            inp = inp[1:]

        elif op_code is Op.OUTPUT:
            p1 = m[i + 1]
            output = op_output(m, p1, pm1, rb)
            # print(f'out: {output}')
            if task == Task.Paint:
                task = Task.Move
                if str(current_point) not in dc:
                    dc[str(current_point)] = output
                else:
                    dc[str(current_point)] = output
            else:
                task = Task.Paint

                if output == 0:
                    if current_dir == 'u':
                        current_point.x -= 1
                        current_dir = 'l'
                    elif current_dir == 'l':
                        current_point.y -= 1
                        current_dir = 'd'
                    elif current_dir == 'd':
                        current_point.x += 1
                        current_dir = 'r'
                    elif current_dir == 'r':
                        current_point.y += 1
                        current_dir = 'u'
                elif output == 1:
                    if current_dir == 'u':
                        current_point.x += 1
                        current_dir = 'r'
                    elif current_dir == 'r':
                        current_point.y -= 1
                        current_dir = 'd'
                    elif current_dir == 'd':
                        current_point.x -= 1
                        current_dir = 'l'
                    elif current_dir == 'l':
                        current_point.y += 1
                        current_dir = 'u'
                if str(current_point) in dc:
                    inp.append(dc[str(current_point)])
                else:
                    inp.append(0)

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

    return dc


dc = process(pz_inp, [1])

plist = []
for i in dc:
    s = i.split(',')
    plist.append([Point(int(s[0]), int(s[1])), dc[i]])

max_x = 0
for p in plist:
    if p[0].x > max_x:
        max_x = p[0].x

max_y = 0
for p in plist:
    if p[0].y > max_y:
        max_y = p[0].y

plot = []
for y in range(0, max_y):
    plot.append([])
    for x in range(0, max_x):
        plot[y].append(0)

for i in plist:
    p = i[0]
    plot[p.y - 1][p.x - 1] = int(i[1])

for r in range(len(plot)):
    for i in range(len(plot[r])):
        plot[r][i] = str(plot[r][i])

for i in range(max_y - 1, 0, -1):
    print(str.join(" ", plot[i]).replace('0', ' ').replace('1', '#'))
