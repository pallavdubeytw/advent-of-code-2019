import timeit


def has_adj_numbers(number):
    string = str(number)

    i = 0
    while i < len(string) - 1:
        if string[i] == string[i + 1]:
            return True
        i += 1

    return False


def is_decreasing(number):
    string = str(number)

    i = 0
    while i < len(string) - 1:
        if int(string[i]) > int(string[i + 1]):
            return True
        i += 1

    return False


def get_each_no_count(number):
    string = str(number)

    count_dict = {}

    for ch in string:
        if ch in count_dict:
            count_dict[ch] += 1
        else:
            count_dict[ch] = 1

    return count_dict


def second_filter(number):
    ch_count = get_each_no_count(number)

    for c in ch_count:
        if ch_count[c] == 2:
            return True


def main():
    given_range = range(382345, 843167)

    start = "1" + ("0" * 9)
    end = "9" * 10
    given_range = range(int(start), int(end))
    print(f'start: {start}')
    print(f'start: {end}')

    first_filtered_values = []
    for i in given_range:
        if has_adj_numbers(i) and not is_decreasing(i):
            first_filtered_values.append(i)

    print(f'count of filter one values: {len(first_filtered_values)}')

    second_filtered_values = []
    for i in first_filtered_values:
        if second_filter(i):
            second_filtered_values.append(i)

    print(f'count of filter two values: {len(second_filtered_values)}')


start = timeit.default_timer()

main()

stop = timeit.default_timer()

print('Time: ', stop - start)
