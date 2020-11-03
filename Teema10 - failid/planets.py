# coding: utf-8
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

    def tick(self):
        """
        Atomaarne samm planeedisüsteemi simulatsioonis.
        Kõigi planeedisüsteemi elementide tick opertsiooni sooritamine
        """
        for item in self:
            item.tick()

    def get(self, i):
        """Tagastada element indeksiga i"""
        return self[i]

    def distance(self, i1, i2):
        """Kaugus indekseid i1 ja i2 omavate süsteemi elementide vahel"""
        return self[i1].distance(self[i2])

    def __str__(self):
        """Planeedisüsteemi kirjeldav string (print ja str operatsioonid)"""
        return '\n---\n'.join([str(p) for p in self])
