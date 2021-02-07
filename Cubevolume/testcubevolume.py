#File to unit test the cubevolume function
import unittest
import cubevolume

#Passing test cases
class TestCase(unittest.TestCase):
    def test_cubevolume1(self):
        self.assertEqual(cubevolume.cubevolume(12), 1728)

    def test_cubevolmune2(self):
        with self.assertRaises(Exception):
            cubevolume.cubevolume(-12)

    def test_cubevolmune3(self):
        with self.assertRaises(TypeError):
            cubevolume.cubevolume("12")


    

if __name__ == '__main__':
    unittest.main(verbosity= 2)