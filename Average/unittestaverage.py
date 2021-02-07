import unittest
import average

lst1 = [15, 9, 55, 41, 35, 20, 62, 49]
lst2 = [-12, -5, -7, -21, -16, -40, -69]
lst3 = []
class TestCase(unittest.TestCase):
    def test_avg1(self):
        self.assertEqual(average.Average(lst1), 35.75)

    def test_avg2(self):
        with self.assertRaises(ZeroDivisionError):
            average.Average(lst3)

    def test_avg3(self):
        self.assertEqual(average.Average(lst2), -24.29)



if __name__ == '__main__':
    unittest.main(verbosity= 2)
