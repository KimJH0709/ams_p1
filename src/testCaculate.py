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
    
    
    """
    def test_calculate_diff_operation(self):
        infix = [3, "*", 6, "-", 9]
        result = ThreerBasicOperations.infix_check(infix)
        postfix = ThreerBasicOperations.make_postfix(infix)
        self.assertEqual(ThreerBasicOperations.calculate(postfix), "[SYSTEM] ERROR! 연산자가 올바르지 않습니다.") # 다른 연산자 입력

    def test_calculate_two_num(self):
        infix = [3, 6, "*", 9]
        postfix = ThreerBasicOperations.make_postfix(infix)
        self.assertEqual(ThreerBasicOperations.calculate(postfix), "[SYSTEM] ERROR! 입력받은 값의 개수가 올바르지 않습니다.") # 숫자 연속 입력

    def test_calculate_div(self):
        infix = [3, "/", 6]
        postfix = ThreerBasicOperations.make_postfix(infix)
        self.assertEqual(ThreerBasicOperations.calculate(postfix), "[SYSTEM] ERROR! 사용 가능한 연산자가 아닙니다.") # 나누기 입력 -> 에러

    def test_calculate_not_num(self):
        infix = ['a', "*", 6]
        postfix = ThreerBasicOperations.make_postfix(infix)
        self.assertEqual(ThreerBasicOperations.calculate(postfix), "[SYSTEM] ERROR! 정수가 아닌 값이 입력되었습니다..") # 정수가 아닌 값 입력 -> 에러

    """

if __name__ == '__main__':
    unittest.main()