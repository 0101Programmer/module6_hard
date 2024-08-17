class Figure:
    SIDES_COUNT = 0

    def __init__(self, filled, r, g, b, *args, sides=None, color=None):
        if filled == 1 or filled == 0:
            self.filled = bool(filled)
        else:
            self.filled = True
        if color is None:
            color = [r, g, b]
            self.color = color
        if sides is None:
            if len(args) == self.SIDES_COUNT:
                self.sides = args
            else:
                self.sides = [self.SIDES_COUNT] * self.SIDES_COUNT

    def get_color(self):
        rgb = range(0, 256)
        print(f'Список RGB цветов: {list(rgb)}')

    def __is_valid_color__(self, r, g, b):
        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            print(f'Цвет ({r},{g},{b}) корректен')
        else:
            print('Цвет некорректен')

    def __is_valid_sides__(self, *args):
        if len(args) == len(self.sides):
            for i in args:
                if i > 0 and i % 1 == 0:
                    i += 1
                    continue
                else:
                    return False
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            self.color[0] = r
            self.color[1] = g
            self.color[2] = b
        else:
            print('Невозможно сменить цвет')

    def get_sides(self):
        return self.sides

    def __len__(self):
        return sum(self.sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.SIDES_COUNT:
            self.sides = new_sides


class Circle(Figure):
    SIDES_COUNT = 1

    def __init__(self, filled, r, g, b, *args):
        super().__init__(filled, r, g, b, *args)
        radius = self.sides[0] / (2 * 3.14)
        radius = round(radius, 2)
        self.radius = radius
        if len(args) == self.SIDES_COUNT:
            self.sides = args
        else:
            self.sides = [self.SIDES_COUNT] * self.SIDES_COUNT

    def get_square(self):
        sqr = 3.14 * (self.radius ** 2)
        sqr = round(sqr, 2)
        print(sqr)


class Triangle(Figure):
    SIDES_COUNT = 3

    def __init__(self, filled, r, g, b, *args):
        super().__init__(filled, r, g, b, *args)
        if len(args) == self.SIDES_COUNT:
            self.sides = args
        else:
            self.sides = [self.SIDES_COUNT] * self.SIDES_COUNT

    def get_square(self):
        p = 0.5 * (sum(self.sides))
        sides_p = p * ((p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))
        sqr = sides_p ** 0.5
        print(round(sqr))


class Cube(Figure):
    SIDES_COUNT = 12

    def __init__(self, filled, r, g, b, *args):
        super().__init__(filled, r, g, b, *args)
        new_args = []
        if len(args) == self.SIDES_COUNT:
            n = args[1]
            for i in args:
                if i == n:
                    new_args.append(i)
                    n = args[1 + 1]
                    continue
                else:
                    self.sides = [self.SIDES_COUNT] * self.SIDES_COUNT
        else:
            self.sides = [self.SIDES_COUNT] * self.SIDES_COUNT

    def get_volume(self):
        vol = self.sides[0] ** 3
        return vol


# код для проверки класса Figure:
# f = Figure(1, 44, 55, 105, 2, 4, 5)
# f.get_color()
# f.__is_valid_color__(1, 4, 6)
# f.__is_valid_color__(1, 4.4, 6)
# print(f.color)
# f.set_color(98, 79, 205)
# print(f.color)
# f.set_color(5.6, 79, 205)
# print(f.color)
# print(f.__is_valid_sides__(3, 10, 15))
# print(f.__is_valid_sides__(3, 1, 15.12))
# print(f.__is_valid_sides__())
# print(f.get_sides())


# код для проверки класса Circle, метода len и метода set_sides:
# c = Circle(1, 55, 105, 44, 101)
# print(c.radius)
# c.get_square()
# print(c.__len__())
# c.set_sides(4)
# print(c.sides)
# c.set_sides(4, 5, 1)
# print(c.sides)
# c2 = Circle(1, 55, 105, 44, 101, 51, 11)
# print(c2.sides)


# код для проверки Triangle:
# t = Triangle(1, 1, 2, 3, 11, 15, 14)
# print(t.sides)
# t.get_square()
# t = Triangle(0, 1, 2, 3, 11, 15, 14, 109, 11)
# print(t.sides)
# t.get_square()

# код для проверки Cube:
# cu = Cube(0, 55, 66, 188, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
# print(cu.sides)
# print(cu.get_volume())
# cu2 = Cube(0, 55, 66, 188, 56)
# print(cu2.sides)
# cu3 = Cube(0, 55, 66, 188, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55, 55)
# print(cu3.sides)
# print(cu3.get_volume())
# cu4 = Cube(0, 55, 66, 188, 55, 55, 55, 55, 55, 55, 10, 55, 55, 55, 55, 55)
# print(cu4.sides)
