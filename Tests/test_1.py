import unittest

def func(s):
    return min(set(s), key = lambda x: s.count(x))

class TestFunc(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(func([1, 1, 2]), 2)
        self.assertEqual(func([1, 2, 2]), 1)
    def test_not_normal(self):
        self.assertRaises(ValueError, func, [])

if __name__ == "__main__":
    unittest.main()