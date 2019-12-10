inp_f = open('input.txt', 'r')


def get_input(lines):
    inp = []
    for l in lines:
        ll = list(l)
        if '\n' in l:
            ll.remove('\n')
        inp.append(list(ll))
    return inp


pz_inp = get_input(inp_f.readlines())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gradient_from(self, other):
        num = other.y - self.y
        den = other.x - self.x

        slope = None
        if den == 0:
            slope = 'none'
        else:
            slope = num / den

        d = None

        if num < 0 and den < 0:
            d = '3'
        elif num > 0 and den < 0:
            d = '2'
        elif num < 0 and den > 0:
            d = '3'
        elif num > 0 and den > 0:
            d = '1'
        elif num == 0:
            d = '-' if den < 0 else ''
        elif den == 0:
            d = '-' if num < 0 else ''

        return f'{slope}{d}'

    def __str__(self):
        return f'{self.x},{self.y}'

    def __repr__(self):
        return self.__str__()


fp = None
dc = {}
for j in range(0, len(pz_inp)):
    for k in range(0, len(pz_inp[j])):
        if pz_inp[j][k] == '#':
            point = Point(k, j)
            if fp is None:
                fp = point
            gl = set()
            for y in range(0, len(pz_inp)):
                for x in range(0, len(pz_inp[y])):
                    if str(Point(x, y)) == str(point):
                        continue
                    if pz_inp[y][x] == '#':
                        p = Point(x, y)
                        g = point.gradient_from(p)
                        # print(f'{point} || {p} || {g}')
                        gl.add(g)
                    x += 1
                y += 1
            dc[str(point)] = len(gl)
            # print(f'{point}: {dc[str(point)]}')
        k += 1
    j += 1

ans = str(fp)
for c in dc:
    if dc[c] > dc[ans]:
        ans = c

print(f'ans: {ans} | {dc[ans]}')
