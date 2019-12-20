from copy import copy

from utils.time import calc_run_time
from utils.progress import print_progress

file = open('input.txt', 'r')
inp_str = file.readline()
# inp_str = '59768092839927758565191298625215106371890118051426250855924764194411528004718709886402903435569627982485301921649240820059827161024631612290005106304724846680415690183371469037418126383450370741078684974598662642956794012825271487329243583117537873565332166744128845006806878717955946534158837370451935919790469815143341599820016469368684893122766857261426799636559525003877090579845725676481276977781270627558901433501565337409716858949203430181103278194428546385063911239478804717744977998841434061688000383456176494210691861957243370245170223862304663932874454624234226361642678259020094801774825694423060700312504286475305674864442250709029812379'
# inp_str = '03036732577212944063491565474664'

pz_input = []
for i in inp_str:
    pz_input.append(int(i))

base_input = [0, 1, 0, -1]


# @calc_run_time
def get_element(signal, pattern):
    j = 1
    total = 0
    k = 0
    for i in signal:
        # print_progress(len(signal), k)
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
        # print(f'element: {i}')
        element_pattern = get_pattern(base_pattern, i + 1)
        phase_output.append(get_element(signal, element_pattern))

    return phase_output


@calc_run_time
def part_one(ip):
    for i in range(0, 100):
        ip = get_phase_output(ip, base_input)

    return "".join(list(map(str, ip[:8])))


print(f'part 1: {part_one(copy(pz_input))}')


@calc_run_time
def part_two(ip):
    signal = ip * 10000
    for i in range(0, 100):
        print(f'phase: {i}')
        signal = get_phase_output(signal, base_input)

    offset = int("".join(list(map(str, signal[:7]))))
    return "".join(list(map(str, signal[offset - 1::8])))


# print(f'part 2: {part_two(copy(pz_input))}')
