from three_operations import ThreerBasicOperations
import unittest

class TestCalculateFactorial(unittest.TestCase):

    def test_valid_input(self):
        infix = [7, "!"]
        result = ThreerBasicOperations.calculateFactorial(infix)
        self.assertEqual(result, '= 5040') # 7! = 5040

    def test_zero_factorial(self):
        infix = [0, "!"]
        result = ThreerBasicOperations.calculateFactorial(infix)
        self.assertEqual(result, '= 1') # 0! = 1

    def test_negative_input(self):
        infix = [-1, "!"]
        result = ThreerBasicOperations.calculateFactorial(infix)
        self.assertEqual(result, "[ERROR] Out Of Range") # 음수 팩토리얼

    def test_invalid_input(self):
        infix = [1, 2, "!"]
        result = ThreerBasicOperations.calculateFactorial(infix)
        self.assertEqual(result, "[ERROR] Input Error") # 두개 이상의 숫자가 입력

    def test_non_number_input(self):
        infix = ['*', '!']
        result = ThreerBasicOperations.calculateFactorial(infix)
        self.assertEqual(result, "[SYETEM] ERROR! 정수가 아닌 값이 입력되었습니다.") # 실수가 아닌 값 입력

    def test_not_integer_number_input(self):
        infix = [7.33, "!"]
        result = ThreerBasicOperations.calculateFactorial(infix)
        self.assertEqual(result, "[SYETEM] ERROR! 정수가 아닌 값이 입력되었습니다.") # 정수가 아닌 실수 값

if __name__ == '__main__':
    unittest.main()