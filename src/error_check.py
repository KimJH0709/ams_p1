import sys

def opr_error(op1, op2):
    if op1 != op2:
        print('[SYETEM] ERROR! 연산자가 올바르지 않습니다.')
        sys.exit(0)
def correct_opr_error(op):
    if not(op == "+" or op == "-" or op == "*" or op == "!"):
        print('[SYETEM] ERROR! 사용 가능한 연산자가 아닙니다.')
        sys.exit(0)
def val_error(val):
    try:
        int(val)
    except ValueError:
        print('[SYETEM] ERROR! 정수가 아닌 값이 입력되었습니다.')
        sys.exit(0)
def number_of_inputs_error(length):
    if not(length % 2):
        print('[SYETEM] ERROR! 입력받은 값의 개수가 올바르지 않습니다.')
        sys.exit(0)

def chech_minus_factorial(num):
    if num < 0:
        print('[SYSTEM] ERROR! Out Of Range')
        sys.exit(0)