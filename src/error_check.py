import sys

def opr_error(op1, op2):
    if op1 != op2:
        error_message = '[SYSTEM] ERROR! 연산자가 올바르지 않습니다.'
        return error_message

def correct_opr_error(op):
    if not(op == "+" or op == "-" or op == "*" or op == "!"):
        error_message = '[SYSTEM] ERROR! 사용 가능한 연산자가 아닙니다.'
        return error_message
def val_error(val):
    try:
        int(val)
    except ValueError:
        error_message = '[SYSTEM] ERROR! 정수가 아닌 값이 입력되었습니다.'
        return error_message
def number_of_inputs_error(length):
    if not(length % 2):
        error_message = '[SYSTEM] ERROR! 입력받은 값의 개수가 올바르지 않습니다.'
        return error_message