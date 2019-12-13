from copy import deepcopy

from utils.time import calc_run_time

inp_file = open("input.txt", 'r')
pz_inp = list(map(int, inp_file.readline().split(',')))

# add quarters
pz_inp[0] = 2

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


class Task:
    Move = 0
    Paint = 1


class Tile:
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    HORIZONTAL_PADDLE = 3
    BALL = 4


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


@calc_run_time
def process(m):
    inp = []
    dc = {}
    point = Point(0, 0)
    ball_position = Point(0, 0)
    paddle_position = Point(0, 0)
    i = rb = 0
    count = 0
    current_score = 0
    step = 0
    while True:
        inst = m[i]

        op_code = inst % 100
        pm1 = int(inst / 100) % 10
        pm2 = int(inst / 1000) % 10
        pm3 = int(inst / 10000) % 10

        if op_code is Op.STOP:
            break

        elif op_code is Op.ADD:
            p1, p2, p3 = m[i + 1], m[i + 2], m[i + 3]
            op_add(m, p1, pm1, p2, pm2, p3, pm3, rb)

        elif op_code is Op.MULTIPLY:
            p1, p2, p3 = m[i + 1], m[i + 2], m[i + 3]
            op_multiply(m, p1, pm1, p2, pm2, p3, pm3, rb)

        elif op_code is Op.INPUT:
            op_input(m, m[i + 1], pm1, rb, step)
            # inp = inp[1:]

        elif op_code is Op.OUTPUT:
            p1 = m[i + 1]
            output = op_output(m, p1, pm1, rb)
            if count == 0:
                point.x = output
                count += 1
            elif count == 1:
                point.y = output
                count += 1
            elif count == 2:
                if output > 4:
                    current_score = output
                elif output == 4:
                    ball_position = deepcopy(point)
                    step = get_step(ball_position, paddle_position)
                elif output == 3:
                    paddle_position = deepcopy(point)
                    step = get_step(ball_position, paddle_position)
                count = 0

        elif op_code is Op.JUMP_IF_TRUE:
            p1, p2 = m[i + 1], m[i + 2]
            i = op_jump_if_true(m, i, p1, pm1, p2, pm2, rb)
            continue

        elif op_code is Op.JUMP_IF_FALSE:
            p1, p2 = m[i + 1], m[i + 2]
            i = op_jump_if_false(m, i, p1, pm1, p2, pm2, rb)
            continue

        elif op_code is Op.LESS_THAN:
            p1, p2, p3 = m[i + 1], m[i + 2], m[i + 3]
            op_less_than(m, p1, pm1, p2, pm2, p3, pm3, rb)

        elif op_code is Op.EQUALS:
            p1, p2, p3 = m[i + 1], m[i + 2], m[i + 3]
            op_equals(m, p1, pm1, p2, pm2, p3, pm3, rb)

        elif op_code is Op.RELATIVE_BASE:
            p1 = m[i + 1]
            rb = op_relative_base(m, p1, pm1, rb)

        i += get_next_instruction_position_offset(op_code)

    return current_score


def get_step(ball_position, paddle_position):
    if ball_position.x > paddle_position.x:
        step = 1
    elif ball_position.x < paddle_position.x:
        step = -1
    elif ball_position.x == paddle_position.x:
        step = 0
    return step


final_score = process(pz_inp)

print(f'part 2: {final_score}')
