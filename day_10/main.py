import math

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

    def distance(self, other):
        return math.sqrt((other.y - self.y) ** 2 + (other.x - self.x) ** 2)

    def angle(self, other):
        num = other.y - self.y
        den = other.x - self.x

        if den == 0:
            return 90 if num > 0 else 270
        if num == 0:
            return 0 if den > 0 else 180

        deg = math.degrees(math.atan(num / den))
        if num < 0 and den < 0:
            return deg + 180
        elif num > 0 and den > 0:
            return deg
        elif num > 0 and den < 0:
            return deg + 180
        elif num < 0 and den > 0:
            return deg + 360

    def __str__(self):
        return f'{self.x},{self.y}'

    def __repr__(self):
        return self.__str__()


class Attr:
    def __init__(self, slope, dist):
        self.slope = slope
        self.dist = dist


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
                    op = Point(x, y)
                    if str(op) == str(point):
                        continue
                    if pz_inp[y][x] == '#':
                        angle = point.angle(op)
                        gl.add(angle)
                        # print(f'{point} | {op} | {angle}')
                    x += 1
                y += 1
            # print(f'{str(point)} ------- {len(gl)}')
            dc[str(point)] = len(gl)
        k += 1
    j += 1

ans = str(fp)
for c in dc:
    if dc[c] > dc[ans]:
        ans = c

print(f'ans: {ans} | {dc[ans]}')

sp = Point(11, 13)
