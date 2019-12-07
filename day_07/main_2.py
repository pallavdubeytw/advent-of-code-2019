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


# puzzle_input = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]

# puzzle_input = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6,
#                 99, 0, 0, 5]


# puzzle_input = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
#                 -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
#                 53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]


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


def process(program, next_inst, phase_setting, amp_signal, requires_ps):
    i = next_inst
    amp_output = None
    halted = 0
    while i < len(program):
        instruction = program[i]

        op_code = get_op_code(instruction)

        param_1 = first_param_mode = param_2 = param_3 = second_param_mode = None

        if op_code != Operation.STOP:
            param_1 = program[i + 1]
            first_param_mode = get_first_param_mode(instruction)

        if op_code != Operation.INPUT and op_code != Operation.OUTPUT and op_code != Operation.STOP:
            param_2 = program[i + 2]
            second_param_mode = get_second_param_mode(instruction)

        if op_code == Operation.ADD or op_code == Operation.MULTIPLY \
                or op_code == Operation.EQUALS or op_code == Operation.LESS_THAN:
            param_3 = program[i + 3]

        if op_code is Operation.STOP:
            halted = 1
            break

        i += get_next_instruction_position_offset(op_code)

        if op_code is Operation.ADD:
            op_add(program, param_1, first_param_mode, param_2, second_param_mode, param_3)

        elif op_code is Operation.MULTIPLY:
            op_multiply(program, param_1, first_param_mode, param_2, second_param_mode, param_3)

        elif op_code is Operation.INPUT:
            if requires_ps:
                op_input(program, param_1, phase_setting)
                requires_ps = False
            else:
                op_input(program, param_1, amp_signal)

        elif op_code is Operation.OUTPUT:
            amp_output = op_output(program, param_1, first_param_mode)
            break

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

    return [program, i, amp_output, halted]


def amp_controller(int_code, phase_inputs):
    amp_no = 0

    all_out = set()
    amp_output = [0] * 5
    amp_halt_state = [0] * 5
    next_inst = [0] * 5
    amp_memory = [int_code.copy()] * 5
    requires_ps = True

    while amp_halt_state[4] != 1:
        second_ip = amp_output[amp_no - 1] if amp_no != 0 else amp_output[4]

        amp_return = process(amp_memory[amp_no].copy(), next_inst[amp_no], phase_inputs[amp_no], second_ip, requires_ps)

        amp_memory[amp_no] = amp_return[0]
        next_inst[amp_no] = amp_return[1]

        if amp_return[2] is not None:
            amp_output[amp_no] = amp_return[2]

        amp_halt_state[amp_no] = amp_return[3]

        all_out.add(amp_output[amp_no])

        if amp_no == 4:
            requires_ps = False

        amp_no = amp_no + 1 if amp_no + 1 < 5 else 0

    return max(all_out)


def permutation(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []

    for i in range(len(lst)):
        m = lst[i]

        rem_lst = lst[:i] + lst[i + 1:]

        for p in permutation(rem_lst):
            l.append([m] + p)
    return l


def main():
    # phase_settings = [0, 1, 2, 3, 4]
    phase_settings = [5, 6, 7, 8, 9]
    p_1 = permutation(phase_settings)
    outputs = []

    for p in p_1:
        outputs.append(amp_controller(puzzle_input.copy(), p))

    # outputs.append(amp_controller(puzzle_input.copy(), [5, 8, 9, 7, 6]))

    return max(outputs)


start = timeit.default_timer()
print(f'output: {main()}')
stop = timeit.default_timer()
print('Time: ', stop - start)
