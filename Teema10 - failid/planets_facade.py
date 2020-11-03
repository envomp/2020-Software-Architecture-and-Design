# coding: utf-8

import math

import planets


class PSController:
    """
    Fassaadikontroller
    """

    def make_solar_system(self, T=20):
        """
        Seob kontrolleriga päikesesüsteemi mudeli.
        T määrab, mitu atomaarset tick sammu on Maa aastas
        """
        self._sys = planets.PlanetarySystem()
        # Päikesesüsteemi infol, koosneb paaridest  (aasta pikkus, kaugus päikesest)) 
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
            self.system().append(planets.Planet(r, 0.0, (2 * math.pi) / (o * T)))

    def get_planetary_item(self, id) -> planets.Planet:
        return self.system().get(id)

    def add_space_ship(self, x, y, dx, dy):
        self.system().append(planets.SpaceShip(x, y, dx, dy))

    def system(self):
        """
        Tagastab kontrolleriga seotud süsteemi
        """
        return self._sys

    def tick(self):
        """
        Muudab planeedisüsteemi elementide koordinaate atomaarse sammu võrra
        """
        self.system().tick()

    def multi_tick(self, N=100):
        """
        Muudab planeedisüsteemi elementide koordinaate N sammu võrra
        """
        for i in range(N):
            self.tick()
