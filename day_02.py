int_code = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 6, 19, 23, 2, 23, 6, 27, 1, 5, 27,
            31, 1, 31, 9, 35, 2, 10, 35, 39, 1, 5, 39, 43, 2, 43, 10, 47, 1, 47, 6, 51, 2, 51, 6, 55, 2, 55, 13,
            59, 2, 6, 59, 63, 1, 63, 5, 67, 1, 6, 67, 71, 2, 71, 9, 75, 1, 6, 75, 79, 2, 13, 79, 83, 1, 9, 83, 87,
            1, 87, 13, 91, 2, 91, 10, 95, 1, 6, 95, 99, 1, 99, 13, 103, 1, 13, 103, 107, 2, 107, 10, 111, 1, 9,
            111, 115, 1, 115, 10, 119, 1, 5, 119, 123, 1, 6, 123, 127, 1, 10, 127, 131, 1, 2, 131, 135, 1, 135,
            10, 0, 99, 2, 14, 0, 0]

expected_value = 19690720


def process_int_code(int_code):
    index = 0
    while True:
        operator_code = int_code[index]

        if operator_code == 99:
            break

        operator_one = int_code[index + 1]
        operator_two = int_code[index + 2]
        result_index = int_code[index + 3]

        if operator_one > len(int_code) or operator_two > len(int_code) or result_index > len(int_code):
            break

        if operator_code == 1:
            int_code[result_index] = int_code[operator_one] + int_code[operator_two]

        if operator_code == 2:
            int_code[result_index] = int_code[operator_one] * int_code[operator_two]

        index = index + 4
    return int_code


print(process_int_code(int_code))


def find_noun_and_verb(memory, expected_value_at_address_0):
    memory_copy = memory.copy()
    noun = 0
    while noun < 99:
        verb = 0
        while verb < 99:
            memory_copy[1] = noun
            memory_copy[2] = verb
            new_array = process_int_code(memory_copy)
            if new_array[0] == expected_value_at_address_0:
                return noun * 100 + verb
            else:
                verb = verb + 1
            memory_copy = memory.copy()
        noun = noun + 1
    return


print(find_noun_and_verb(int_code, expected_value))
