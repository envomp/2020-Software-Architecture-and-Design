import unittest
import math

class TestRadians(unittest.TestCase):

    def assertRadiansEqual(self, expected, actual, places=7, msg=""):
        return self.assertAlmostEqual(0.0, (expected-actual) % (2*math.pi), places, msg)

    def testRadianEquality(self):
        self.assertRadiansEqual(1.0, 1.0, "Simple equality failure")
        self.assertRadiansEqual((3/2)*math.pi, -(1/2)*math.pi, "Negative radian equality failure")
        self.assertRadiansEqual((3/2)*math.pi, (7/2)*math.pi, "Modulo radian equality failure")
        self.assertRadiansEqual((3/2)*math.pi, -(5/2)*math.pi, "Negative modulo radian equality failure")
        

if __name__ == '__main__':
    unittest.main()
