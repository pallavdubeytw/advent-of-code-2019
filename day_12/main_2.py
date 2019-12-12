import timeit
from copy import deepcopy
from utils.lcm import lcm

start = timeit.default_timer()


def print_elapsed_time():
    stop = timeit.default_timer()
    print(f'Time elapsed: {int(stop - start)} seconds', end='\r')


class Point:
    def __init__(self, x, y, z):
        self.z = z
        self.y = y
        self.x = x


class Velocity:
    def __init__(self, x, y, z):
        self.z = z
        self.y = y
        self.x = x


class Moon:
    def __init__(self, position, velocity):
        self.velocity = velocity
        self.position = position

    def calc_velocity(self, other_moon):
        if other_moon.position.x > self.position.x:
            self.velocity.x += 1
        elif other_moon.position.x < self.position.x:
            self.velocity.x -= 1
        if other_moon.position.y > self.position.y:
            self.velocity.y += 1
        elif other_moon.position.y < self.position.y:
            self.velocity.y -= 1
        if other_moon.position.z > self.position.z:
            self.velocity.z += 1
        elif other_moon.position.z < self.position.z:
            self.velocity.z -= 1

    def move(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.position.z += self.velocity.z

    def potential(self):
        return abs(self.position.x) + abs(self.position.y) + abs(self.position.z)

    def kinetic(self):
        return abs(self.velocity.x) + abs(self.velocity.y) + abs(self.velocity.z)

    def __repr__(self):
        return f'Pos : {self.position.x},{self.position.y},{self.position.z} ' \
               f'|| Vel {self.velocity.x},{self.velocity.y},{self.velocity.z} ' \
               f'|| KE: {self.kinetic()} || PE: {self.potential()}'

    def compare_x(self, other):
        return self.position.x == other.position.x and self.velocity.x == other.velocity.x

    def compare_y(self, other):
        return self.position.y == other.position.y and self.velocity.y == other.velocity.y

    def compare_z(self, other):
        return self.position.z == other.position.z and self.velocity.z == other.velocity.z


io = Moon(Point(4, 12, 13), Velocity(0, 0, 0))
europa = Moon(Point(-9, 14, -3), Velocity(0, 0, 0))
ganymede = Moon(Point(-7, -1, 2), Velocity(0, 0, 0))
callisto = Moon(Point(-11, 17, -1), Velocity(0, 0, 0))

# Prasanna
# io = Moon(Point(-19, -4, 2), Velocity(0, 0, 0))
# europa = Moon(Point(-9, 8, -16), Velocity(0, 0, 0))
# ganymede = Moon(Point(-4, 5, -11), Velocity(0, 0, 0))
# callisto = Moon(Point(1, 9, -13), Velocity(0, 0, 0))

# example
# io = Moon(Point(-1, 0, 2), Velocity(0, 0, 0))
# europa = Moon(Point(2, -10, -7), Velocity(0, 0, 0))
# ganymede = Moon(Point(4, -8, 8), Velocity(0, 0, 0))
# callisto = Moon(Point(3, 5, -1), Velocity(0, 0, 0))

# example 2
# io = Moon(Point(-8, -10, 0), Velocity(0, 0, 0))
# europa = Moon(Point(5, 5, 10), Velocity(0, 0, 0))
# ganymede = Moon(Point(2, -7, 3), Velocity(0, 0, 0))
# callisto = Moon(Point(9, -8, -3), Velocity(0, 0, 0))

moons = [io, europa, ganymede, callisto]
initial_state = deepcopy(moons)

count = 1
repeat = {'x': 0, 'y': 0, 'z': 0}

while True:
    print_elapsed_time()
    for i in range(0, len(moons)):
        for j in range(0, len(moons)):
            if i != j:
                moons[i].calc_velocity(moons[j])

    for m in moons:
        m.move()

    if repeat['x'] == 0:
        x_flag = True
        for i in range(0, 4):
            if not initial_state[i].compare_x(moons[i]):
                x_flag = False
                break
        if x_flag:
            repeat['x'] = count

    if repeat['y'] == 0:
        y_flag = True
        for i in range(0, 4):
            if not initial_state[i].compare_y(moons[i]):
                y_flag = False
                break
        if y_flag:
            repeat['y'] = count

    if repeat['z'] == 0:
        z_flag = True
        for i in range(0, 4):
            if not initial_state[i].compare_z(moons[i]):
                z_flag = False
                break
        if z_flag:
            repeat['z'] = count

    loop_break = True
    for i in repeat:
        if repeat[i] == 0:
            loop_break = False

    if loop_break:
        break

    count += 1

x = repeat['x']
y = repeat['y']
z = repeat['z']

ans = int(lcm(x, y, z))

print(f'part 2: {ans}')

print_elapsed_time()
