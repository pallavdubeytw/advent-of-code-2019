from copy import copy
from utils.time import calc_run_time
from utils.progress import print_progress

file = open('input.txt', 'r')
inp_str = file.readline()
inp_str = '03081770884921959731165446850517'

pz_input = []
for i in inp_str:
    pz_input.append(int(i))


# @calc_run_time
def get_element(signal, element):
    # cycle = int(len(signal) / element)
    total = sum(signal[element:])
    return total % 10


# @calc_run_time
def get_phase_output(signal, offset):
    length = len(signal) - offset
    phase_output = [0] * length
    index = length - 1
    for i in range(len(signal) - 1, offset - 1, -1):
        phase_output[index] = get_element(signal, i)
        index -= 1

    return phase_output


@calc_run_time
def part_two(ip):
    signal = ip * 10000
    offset = int("".join(list(map(str, signal[:7]))))
    empty = [0] * offset
    outp = []
    for i in range(0, 100):
        print(f'phase: {i}')
        outp = get_phase_output(signal, offset)
        signal = empty + outp

    return "".join(list(map(str, outp[:8])))


print(f'part 2: {part_two(copy(pz_input))}')
