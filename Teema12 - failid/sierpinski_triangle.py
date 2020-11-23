import numpy as np

from geom import Point


def points_inside_triangle(a: Point, b: Point, c: Point):
    xs = [x.x() for x in (a, b, c)]
    ys = [x.y() for x in (a, b, c)]

    xs = np.array(xs, dtype=float)
    ys = np.array(ys, dtype=float)

    # The possible range of coordinates that can be returned
    x_range = np.arange(np.min(xs), np.max(xs) + 1)
    y_range = np.arange(np.min(ys), np.max(ys) + 1)

    # Set the grid of coordinates on which the triangle lies. The centre of the
    # triangle serves as a criterion for what is inside or outside the triangle.
    X, Y = np.meshgrid(x_range, y_range)
    xc = np.mean(xs)
    yc = np.mean(ys)

    # From the array 'triangle', points that lie outside the triangle will be
    # set to 'False'.
    triangle = np.ones(X.shape, dtype=bool)
    for i in range(3):
        ii = (i + 1) % 3
        if xs[i] == xs[ii]:
            include = X * (xc - xs[i]) / abs(xc - xs[i]) > xs[i] * (xc - xs[i]) / abs(xc - xs[i])
        else:
            poly = np.poly1d([(ys[ii] - ys[i]) / (xs[ii] - xs[i]), ys[i] - xs[i] * (ys[ii] - ys[i]) / (xs[ii] - xs[i])])
            include = Y * (yc - poly(xc)) / abs(yc - poly(xc)) > poly(X) * (yc - poly(xc)) / abs(yc - poly(xc))
        triangle *= include

    xs = X[triangle]
    ys = Y[triangle]
    return [Point(x, y) for x, y in zip(xs, ys)]


class SierpinskiTriangle(list):
    def __init__(self, level, p1, p2, p3):
        super().__init__()
        self.generate_triangle(level, p1, p2, p3)

    def generate_triangle(self, level, p1, p2, p3):
        if level <= 1:
            for point in points_inside_triangle(p1, p2, p3):
                self.append(point)
        else:
            p4 = p1.midpoint(p2)
            p5 = p2.midpoint(p3)
            p6 = p1.midpoint(p3)
            self.generate_triangle(level - 1, p1, p4, p6)
            self.generate_triangle(level - 1, p4, p2, p5)
            self.generate_triangle(level - 1, p6, p5, p3)


if __name__ == "__main__":
    p = Point(0, 0)
    q = Point(5, 0)
    r = Point(0, 5)

    print(points_inside_triangle(p, q, r))
