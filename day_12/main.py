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
        return f'Pos : {self.position.x},{self.position.y},{self.position.z} || Vel {self.velocity.x},{self.velocity.y},{self.velocity.z} || KE: {self.kinetic()} || PE: {self.potential()}'


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
steps = 1000
for step in range(0, steps):
    for i in range(0, len(moons)):
        for j in range(0, len(moons)):
            if i != j:
                moons[i].calc_velocity(moons[j])

    for m in moons:
        m.move()

total = 0
for m in moons:
    total += (m.kinetic() * m.potential())

print(f'part 1: {total}')
