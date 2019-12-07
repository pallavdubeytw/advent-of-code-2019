import timeit

puzzle_input = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 46, 55, 72, 85, 110, 191, 272, 353, 434, 99999, 3, 9, 1002, 9,
                5, 9, 1001, 9, 2, 9, 102, 3, 9, 9, 101, 2, 9, 9, 102, 4, 9, 9, 4, 9, 99, 3, 9, 102, 5, 9, 9, 4, 9, 99,
                3, 9, 1002, 9, 2, 9, 101, 2, 9, 9, 1002, 9, 2, 9, 4, 9, 99, 3, 9, 1002, 9, 4, 9, 101, 3, 9, 9, 4, 9, 99,
                3, 9, 1002, 9, 3, 9, 101, 5, 9, 9, 1002, 9, 3, 9, 101, 3, 9, 9, 1002, 9, 5, 9, 4, 9, 99, 3, 9, 1001, 9,
                2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2,
                9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2,
                9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9,
                1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3,
                9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9,
                99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9,
                4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 2,
                9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102,
                2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9,
                1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3,
                9, 1001, 9, 1, 9, 4, 9, 99, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4,
                9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9,
                4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 99]

puzzle_input = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]


class Operation:
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    STOP = 99


class ParameterMode:
    POSITION = 0
    IMMEDIATE = 1


def get_nth_digit(instruction, n):
    if len(str(instruction)) < n:
        return None
    return int(str(instruction)[0 - n])


def get_op_code(instruction):
    return int(str(instruction)[-2:])


def get_first_param_mode(instruction):
    mode = get_nth_digit(instruction, 3)
    if mode is None or mode is 0:
        return ParameterMode.POSITION
    return ParameterMode.IMMEDIATE


def get_second_param_mode(instruction):
    mode = get_nth_digit(instruction, 4)
    if mode is None or mode is 0:
        return ParameterMode.POSITION
    return ParameterMode.IMMEDIATE


def get_next_instruction_position_offset(operation):
    if operation is Operation.ADD or operation is Operation.MULTIPLY \
            or operation is Operation.LESS_THAN or operation is Operation.EQUALS:
        return 4
    elif operation is Operation.INPUT or operation is Operation.OUTPUT:
        return 2
    elif operation is Operation.JUMP_IF_TRUE or operation is Operation.JUMP_IF_FALSE:
        return 3


def op_add(program, param_1, first_param_mode, param_2, second_param_mode, param_3):
    op_1 = param_1 if first_param_mode == ParameterMode.IMMEDIATE else program[param_1]
    op_2 = param_2 if second_param_mode == ParameterMode.IMMEDIATE else program[param_2]

    program[param_3] = op_1 + op_2


def op_multiply(program, param_1, first_param_mode, param_2, second_param_mode, param_3):
    op_1 = param_1 if first_param_mode == ParameterMode.IMMEDIATE else program[param_1]
    op_2 = param_2 if second_param_mode == ParameterMode.IMMEDIATE else program[param_2]

    program[param_3] = op_1 * op_2


def op_input(program, param_1, param_2):
    program[param_1] = param_2


def op_output(program, param_1, first_param_mode):
    if first_param_mode == ParameterMode.IMMEDIATE:
        return param_1
    else:
        return program[param_1]


def op_jump_if_true(program, param_1, first_param_mode, param_2, second_param_mode):
    op_1 = param_1 if first_param_mode == ParameterMode.IMMEDIATE else program[param_1]
    op_2 = param_2 if second_param_mode == ParameterMode.IMMEDIATE else program[param_2]

    if op_1 != 0:
        return op_2


def op_jump_if_false(program, param_1, first_param_mode, param_2, second_param_mode):
    op_1 = param_1 if first_param_mode == ParameterMode.IMMEDIATE else program[param_1]
    op_2 = param_2 if second_param_mode == ParameterMode.IMMEDIATE else program[param_2]

    if op_1 == 0:
        return op_2


def op_less_than(program, param_1, first_param_mode, param_2, second_param_mode, param_3):
    op_1 = param_1 if first_param_mode == ParameterMode.IMMEDIATE else program[param_1]
    op_2 = param_2 if second_param_mode == ParameterMode.IMMEDIATE else program[param_2]

    if op_1 < op_2:
        program[param_3] = 1
    else:
        program[param_3] = 0


def op_equals(program, param_1, first_param_mode, param_2, second_param_mode, param_3):
    op_1 = param_1 if first_param_mode == ParameterMode.IMMEDIATE else program[param_1]
    op_2 = param_2 if second_param_mode == ParameterMode.IMMEDIATE else program[param_2]

    if op_1 == op_2:
        program[param_3] = 1
    else:
        program[param_3] = 0


def process(program, phase_setting, amp_signal):
    i = 0
    input_no = 1
    amp_output = -0.1
    while i < len(program) - 3:
        instruction = program[i]

        op_code = get_op_code(instruction)

        param_1 = program[i + 1]
        param_2 = program[i + 2]
        param_3 = program[i + 3]
        first_param_mode = get_first_param_mode(instruction)
        second_param_mode = get_second_param_mode(instruction)

        if op_code is Operation.ADD:
            op_add(program, param_1, first_param_mode, param_2, second_param_mode, param_3)

        elif op_code is Operation.MULTIPLY:
            op_multiply(program, param_1, first_param_mode, param_2, second_param_mode, param_3)

        elif op_code is Operation.INPUT:
            if input_no == 1:
                op_input(program, param_1, phase_setting)
                input_no += 1
            elif input_no == 2:
                op_input(program, param_1, amp_signal)

        elif op_code is Operation.OUTPUT:
            amp_output = op_output(program, param_1, first_param_mode)

        elif op_code is Operation.JUMP_IF_TRUE:
            index = op_jump_if_true(program, param_1, first_param_mode, param_2, second_param_mode)
            if index is not None:
                i = index
                continue

        elif op_code is Operation.JUMP_IF_FALSE:
            index = op_jump_if_false(program, param_1, first_param_mode, param_2, second_param_mode)
            if index is not None:
                i = index
                continue

        elif op_code is Operation.LESS_THAN:
            op_less_than(program, param_1, first_param_mode, param_2, second_param_mode, param_3)

        elif op_code is Operation.EQUALS:
            op_equals(program, param_1, first_param_mode, param_2, second_param_mode, param_3)

        elif op_code is Operation.STOP:
            break

        i += get_next_instruction_position_offset(op_code)

    return amp_output


start = timeit.default_timer()
amp_output = process(puzzle_input, 4, 0)
print(amp_output)
stop = timeit.default_timer()
print('Time: ', stop - start)
