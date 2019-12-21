from copy import copy
from utils.time import calc_run_time
from utils.progress import print_progress

file = open('input.txt', 'r')
inp_str = file.readline()

pz_input = []
for i in inp_str:
    pz_input.append(int(i))


def get_phase_output(signal, offset):
    phase_output = []
    t = sum(signal[offset:])
    for i in range(offset, len(signal)):
        phase_output.append(t % 10)
        t -= signal[i]

    return phase_output


@calc_run_time
def part_two(ip):
    signal = ip * 10000
    offset = int("".join(list(map(str, signal[:7]))))
    empty = [0] * offset
    outp = []
    for i in range(0, 100):
        print_progress(100, i)
        outp = get_phase_output(signal, offset)
        signal = empty + outp

    return "".join(list(map(str, outp[:8])))


print(f'part 2: {part_two(copy(pz_input))}')
