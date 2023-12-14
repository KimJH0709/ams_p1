from three_operations import ThreerBasicOperations
import unittest

class TestCalculate(unittest.TestCase):
    def test_calculate_add(self):
        infix = [3, "+", 6]
        postfix = ThreerBasicOperations.make_postfix(infix)
        self.assertEqual(ThreerBasicOperations.calculate(postfix), 9) # 3+6=9

    def test_calculate_sub(self):
        infix = [3, "-", 6]
        postfix = ThreerBasicOperations.make_postfix(infix)
        self.assertEqual(ThreerBasicOperations.calculate(postfix), -3) # 3-6=-3
    
    def test_calculate_mul(self):
        infix = [3, "*", 6]
        postfix = ThreerBasicOperations.make_postfix(infix)
        self.assertEqual(ThreerBasicOperations.calculate(postfix), 18) # 3*6=18

if __name__ == '__main__':
    unittest.main()