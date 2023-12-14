import unittest
from three_operations import ThreerBasicOperations

class ErrorTest(unittest.TestCase):

    def test_calculate_diff_operation(self):
        infix = [3, "*", 6, "-", 9]
        errorMessage = ThreerBasicOperations.infix_check(infix)
        self.assertEqual(errorMessage, "[SYSTEM] ERROR! 연산자가 올바르지 않습니다.")

    def test_calculate_two_num(self):
        infix = [3, 6, "*", 9]
        errorMessage = ThreerBasicOperations.infix_check(infix)
        self.assertEqual(errorMessage, "[SYSTEM] ERROR! 입력받은 값의 개수가 올바르지 않습니다.") # 숫자 연속 입력
        
    def test_calculate_div(self):
        infix = [3, "/", 6]
        errorMessage = ThreerBasicOperations.infix_check(infix)
        self.assertEqual(errorMessage, "[SYSTEM] ERROR! 사용 가능한 연산자가 아닙니다.") # 나누기 입력 -> 에러

    def test_calculate_not_num(self):
        infix = ['a', "*", 6]
        errorMessage = ThreerBasicOperations.infix_check(infix)
        self.assertEqual(errorMessage, "[SYSTEM] ERROR! 정수가 아닌 값이 입력되었습니다.") # 정수가 아닌 값 입력 -> 에러
if __name__ == '__main__':
    unittest.main()
