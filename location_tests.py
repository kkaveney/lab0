import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")

    def test_1(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1, loc2)

    def test_2(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("LA", 35.7, -110.2)
        self.assertNotEqual(loc1,loc2)

    def test_repr_2(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertNotEqual(loc, "Location('LA', 35.7, -110.2)")

    # Add more tests!


if __name__ == "__main__":
    unittest.main()