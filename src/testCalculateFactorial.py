from three_operations import ThreerBasicOperations
import unittest

class TestCalculateFactorial(unittest.TestCase):
    def test_calculate_factorial(self):
        infix = []
        infix.append(7)
        infix.append("!")
        self.assertEqual(ThreerBasicOperations.calculateFactorial(infix), "= " + str(5040)) # 7! = 5040

    def test_calculate_0_factorial(self):
        infix = []
        infix.append(0)
        infix.append("!")
        self.assertEqual(ThreerBasicOperations.calculateFactorial(infix), "= " + str(1)) # 0! = 1

    def test_calculate_negative_factorial(self):
        infix = []
        infix.append(-1)
        infix.append("!")
        self.assertEqual(ThreerBasicOperations.calculateFactorial(infix), "[ERROR] Out Of Range") # 음수 팩토리얼

    def test_more_than_two_count_factorial(self):
        infix = []
        infix.append(1)
        infix.append(2)
        infix.append("!")
        self.assertEqual(ThreerBasicOperations.calculateFactorial(infix), "[ERROR] Input Error") # 두개 이상의 숫자가 입력

    def test_not_int_factorial(self):
        infix = []
        infix.append("*")
        infix.append("!")
        self.assertEqual(ThreerBasicOperations.calculateFactorial(infix), "[SYETEM] ERROR! 정수가 아닌 값이 입력되었습니다.") # 정수가 아닌 값 입력


if __name__ == '__main__':
    unittest.main()