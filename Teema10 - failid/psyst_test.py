import math
import unittest

from planets import Planet, PlanetarySystem, SpaceShip


class PlanetTest(unittest.TestCase):

    def setUp(self):
        self.p1 = Planet(5.0, 0.0, 0.1)

    def testInitial(self):
        self.assertAlmostEqual(self.p1.rho(), 5.0)
        self.assertAlmostEqual(self.p1.theta(), 0.0)

    def testOneMove(self):
        self.p1.tick()
        self.assertAlmostEqual(self.p1.rho(), 5.0)
        self.assertAlmostEqual(self.p1.theta(), 0.1)


class PSTest(unittest.TestCase):

    def setUp(self):
        self.ps = PlanetarySystem()
        self.ps.append(Planet(1.0, 1.0, 0.1))
        self.ps.append(Planet(-1.0, 1.0, 0.2))
        self.ps.append(Planet(1.2, 3.4, math.pi / 10))
        self.ps.append(SpaceShip(10, 0, 0.1, 0.1))

    def testOneTick(self):
        self.ps.tick()
        self.assertAlmostEqual(self.ps[0].theta(), math.pi / 4 + 0.1)
        self.assertAlmostEqual(self.ps[1].theta(), 3 * math.pi / 4 + 0.2)
        self.assertAlmostEqual(self.ps[3].x(), 10.1)
        self.assertAlmostEqual(self.ps[3].y(), 0.1)

    def testFullCircle(self):
        for i in range(20):
            self.ps.tick()

        self.assertAlmostEqual(self.ps[2].x(), 1.2)
        self.assertAlmostEqual(self.ps[2].y(), 3.4)

        self.assertAlmostEqual(self.ps[3].x(), 12)
        self.assertAlmostEqual(self.ps[3].y(), 2)


if __name__ == "__main__":
    unittest.main()
