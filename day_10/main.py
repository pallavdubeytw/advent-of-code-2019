inp_f = open('input.txt', 'r')


def get_input(lines):
    inp = []
    for l in lines:
        l = list(l)
        if '\n' in l:
            l.remove('\n')
        inp.append(list(l))
    return inp


pz_inp = get_input(inp_f.readlines())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gradient_from(self, other):
        yy = other.y - self.y
        xx = other.x - self.x

        if xx == 0:
            if yy < 0:
                return '-None'
            elif yy > 0:
                return 'None'
        elif yy == 0:
            if xx < 0:
                return '-0'
            elif xx > 0:
                return '0'
        elif xx < 0 and yy < 0:
            return f'{str(yy / xx)}d'
        else:
            return str(yy / xx)

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
            print(f'{point}: {dc[str(point)]}')
        k += 1
    j += 1

ans = str(fp)
for c in dc:
    if dc[c] > dc[ans]:
        ans = c

print(f'ans: {ans}')
