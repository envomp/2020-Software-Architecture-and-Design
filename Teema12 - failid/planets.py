# coding: utf-8
import math

import geom


class SpaceShip(geom.Point):
    """Planeet omab koordinaate ja nurkkiirust. Tiirleb ümber koordinaatide alguspunkti."""

    def __init__(self, x, y, dx, dy):
        geom.Point.__init__(self, x, y)
        self._dx = dx
        self._dy = dy

    def dx(self):
        return self._dx

    def dy(self):
        return self._dy

    def tick(self):
        """
        Atomaarne samm kosmose laeva simulatsioonis.
        Kosmose laeva koordinaadid muutuvad dx ja dy võrra
        """
        self.translate(self.dx(), self.dy())


class Planet(geom.Point):
    """Planeet omab koordinaate ja nurkkiirust. Tiirleb ümber koordinaatide alguspunkti."""

    def __init__(self, x, y, omega):
        geom.Point.__init__(self, x, y)
        self._omega = omega

    def omega(self):
        "Nurkkiirus radiaanides"
        return self._omega

    def tick(self):
        """
        Atomaarne samm planeedi simulatsioonis.
        Planeedi koordinaadid muutuvad nurkkiiruse võrra
        """
        self.centre_rotate(self.omega())


class PlanetarySystem(list):
    """Planeetide hulk (list)"""

    def __init__(self):
        super().__init__()

        astro_data = [
            (87.97 / 365.26, 0.39),
            (227.7 / 365.26, 0.72),
            (1.0, 1.0),
            (686.98 / 365.26, 1.52),
            (11.86, 5.2),
            (29.46, 9.54),
            (84.01, 19.18),
            (164.81, 30.06),
            (247.7, 39.75)
        ]

        for o, r in astro_data:
            self.append(Planet(r, 0.0, (2 * math.pi) / (o * 20)))
