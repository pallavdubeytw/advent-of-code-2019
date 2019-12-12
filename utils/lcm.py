def hcf(x, y):
    min_no = min(x, y)

    for i in range(min_no, 1, -1):
        if x % i == 0 and y % i == 0:
            return i


def inner_lcm(x, y):
    return (x * y) / hcf(x, y)


def lcm(*args):
    result = inner_lcm(args[0], args[1])
    for i in range(2, len(args)):
        result = inner_lcm(result, args[i])
    return result
