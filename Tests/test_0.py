import unittest

def cube_area(side):
    if side == 0: raise ValueError
    if not isinstance(side, (int, float)): raise TypeError
    return 6 * side ** 2

class TestCubeArea(unittest.TestCase):
    def test_cube_area(self):
        self.assertEqual(cube_area(3), 54)
    def test_value(self):
        self.assertRaises(ValueError, cube_area, 0)
    def test_types(self):
        self.assertRaises(TypeError, cube_area, True)

if __name__ == "__main__":
    unittest.main()