import unittest
from app import add

class TestApp(unittest.TestCase):
    def Test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(1,1),2)
        self.assertEqual(add(2,2),4)
        self.assertEqual(add(3,3),6)
        self.assertEqual(add(4,4),8)   

if __name__=='__main__':
    unittest.main()

