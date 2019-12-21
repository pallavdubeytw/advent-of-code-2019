from copy import copy

from utils.time import calc_run_time
from utils.progress import print_progress

file = open('input.txt', 'r')
inp_str = file.readline()

pz_input = []
for i in inp_str:
    pz_input.append(int(i))

base_input = [0, 1, 0, -1]


def get_element(signal, pattern):
    j = 1
    total = 0
    k = 0
    for i in signal:
        k += 1
        if j == len(pattern):
            j = 0
        total = total + i * pattern[j]
        j += 1
    return int(str(total)[-1])


def get_pattern(base_pattern, position):
    pattern = []
    for j in base_pattern:
        for i in range(0, position):
            pattern.append(j)

    return pattern


def get_phase_output(signal, base_pattern):
    phase_output = []
    for i in range(0, len(signal)):
        element_pattern = get_pattern(base_pattern, i + 1)
        phase_output.append(get_element(signal, element_pattern))

    return phase_output


@calc_run_time
def part_one(ip):
    for i in range(0, 100):
        ip = get_phase_output(ip, base_input)

    return "".join(list(map(str, ip[:8])))


print(f'part 1: {part_one(copy(pz_input))}')
