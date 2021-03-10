

class Rectangle(object):
    def __init__(self, left_x, bottom_y, width, height):
        self.left_x = left_x
        self.bottom_y = bottom_y
        self.width = width
        self.height = height

    @property
    def right_x(self):
        return self.left_x + self.width

    @property
    def top_y(self):
        return self.bottom_y + self.height

    def __str__(self):
        return "<Rectangle> left_x={left_x}, bottom_y={bottom_y}, width={width}, height={height}".format(
            left_x=self.left_x,
            bottom_y=self.bottom_y,
            width=self.width,
            height=self.height,
        )

    def as_tuple(self):
        return self.left_x, self.bottom_y, self.width, self.height

    def __eq__(self, other):
        if other is None:
            return False
        return self.as_tuple() == other.as_tuple()


def overlap_rec(r1, r2):
    x = overlap_dim((r1.left_x, r1.right_x), (r2.left_x, r2.right_x))
    if x is None:
        return None
    y = overlap_dim((r1.bottom_y, r1.top_y), (r2.bottom_y, r2.top_y))
    if y is None:
        return None

    left_x, width = x[0], x[1] - x[0]
    bottom_y, height = y[0], y[1] - y[0]
    return Rectangle(left_x, bottom_y, width, height)


def overlap_dim(r1_dim, r2_dim):
    ranges = sorted([r1_dim, r2_dim])
    r1_dim, r2_dim = ranges
    # disjoint
    if r1_dim[1] <= r2_dim[0]:
        return None
    min_dim = max(r1_dim[0], r2_dim[0])
    max_dim = min(r1_dim[1], r2_dim[1])
    return min_dim, max_dim


r1 = Rectangle(0, 0, 5, 10)
r2 = Rectangle(6, 12, 4, 8)

assert overlap_rec(r1, r2) is None

r3 = Rectangle(0, 0, 3, 8)
assert overlap_rec(r1, r3) == r3

r4 = Rectangle(1, 1, 4, 9)
assert overlap_rec(r1, r4) == r4

assert overlap_rec(r3, r4) == Rectangle(1, 1, 2, 7)

assert overlap_rec(r3, r2) is None

