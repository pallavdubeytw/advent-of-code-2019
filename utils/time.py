import timeit


def calc_run_time(func):
    def timed(*args):
        start = timeit.default_timer()

        result = func(*args)

        stop = timeit.default_timer()
        print(f'Method: {func.__name__} | ', end='')
        print(f'Time elapsed: {int(stop - start)}s')

        return result

    return timed
