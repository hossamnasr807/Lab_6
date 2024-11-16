import unittest
from addition import addition

class Test_addition(unittest.TestCase):
    def test_add(self):
        result=addition.add(1,7)
        self.assertEqual(result,8)

        result=addition.add(-2,-2)
        self.assertEqual(result,-4)

        result=addition.add(-3,3)
        self.assertEqual(result,0)

        result=addition.add(0,7)
        self.assertEqual(result,7)

        result=addition.add(0,-4)
        self.assertEqual(result,-4)
if __name__=="__main__":
    unittest.main()
