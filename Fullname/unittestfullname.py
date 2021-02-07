import unittest
import fullname

class TestCase(unittest.TestCase):
    def test_name1(self):
        self.assertEqual(fullname.fullname("Jacob","Urenda"), "Jacob Urenda")

    def test_name2(self):
        with self.assertRaises(Exception):
            fullname.fullname("","")
    
    def test_name3(self):
        with self.assertRaises(TypeError):
            fullname.fullname(1,1)
        

if __name__ == '__main__':
    unittest.main(verbosity= 2)