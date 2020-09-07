import math

class Point:
    "Two-dimensional points"

    def __init__(self, x=0.0, y=0.0):
        self._rho = math.sqrt(x**2 + y**2)
        self._theta = math.atan2(y, x)

    def __str__(self):
        result = "\n".join(["x: %f" % self.x(),
                            "y: %f" % self.y(),
                            "rho: %f" % self.rho(),
                            "theta: %f" % self.theta()])
        return result

# Queries

    def x(self):
        "Abscissa"
        return self.rho()*math.cos(self.theta())

    def y(self):
        "Ordinate"
        return self.rho()*math.sin(self.theta())

    def rho(self):
        "Distance to origin (0, 0)"
        return self._rho

    def theta(self):
        "Angle to horizontal axis"
        return self._theta

    def distance(self, other):
        "Distance to other"
        return self.vectorTo(other).rho()

    def vectorTo(self, other):
        "Returns the Point representing the vector from self to other Point"
        return Point(other.x() - self.x(), other.y() - self.y())

# Commands

    def translate(self, dx, dy):
        "Move by dx horizontally, dy vertically"
        x = self.x() + dx
        y = self.y() + dy
        self._rho = math.sqrt(x**2 + y**2)
        self._theta = math.atan2(y, x)
   
    def scale(self, factor):
        "Scale by factor"
        self._rho *= factor

    def centre_rotate(self, angle):
        "Rotate around origin (0, 0) by angle"
        self._theta = (self._theta + angle) % (2 * math.pi)
        
    def rotate(self, p, angle):
        "Rotate around p by angle"
        self.translate(-p.x(), -p.y())
        self.centre_rotate(angle)
        self.translate(p.x(), p.y())
