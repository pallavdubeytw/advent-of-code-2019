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

p = list(map(int, ans.split(',')))
sp = Point(p[0], p[1])
# sp = Point(2, 2)
dc2 = {}
for y in range(0, len(pz_inp)):
    for x in range(0, len(pz_inp[y])):
        op = Point(x, y)
        if str(op) == str(sp):
            continue
        if pz_inp[y][x] == '#':
            angle = sp.angle(op)
            dist = sp.distance(op)
            if angle in dc2:
                if dist < dc2[angle][1]:
                    dc2[angle] = [op, dist]
            else:
                dc2[angle] = [op, dist]
        x += 1
    y += 1

tot = len(dc2)

l1 = []
l4 = []
l3 = []
l2 = []
for a in dc2:
    if a >= 270 and a < 360:
        l1.append(a)
    elif a >= 0 and a < 90:
        l2.append(a)
    elif a >= 90 and a < 180:
        l3.append(a)
    elif a >= 180 and a < 270:
        l4.append(a)
    else:
        print(a)

tot = len(l1) + len(l2) + len(l3) + len(l4)

l1.sort()
l4.sort()
l3.sort()
l2.sort()

tot = len(l1) + len(l2) + len(l3) + len(l4)

print(dc2)
# print(l1)
# print(l2)
# print(l3)
# print(l4)

i = 0
for a in l1:
    i += 1
    print(f'{i} : {a} : {dc2[a][0]}')
for a in l2:
    i += 1
    print(f'{i} : {a} : {dc2[a][0]}')
for a in l3:
    i += 1
    print(f'{i} : {a} : {dc2[a][0]}')
for a in l4:
    i += 1
    if a == 360:
        print(f'{i} : {a} : {dc2[0][0]}')
    else:
        print(f'{i} : {a} : {dc2[a][0]}')
