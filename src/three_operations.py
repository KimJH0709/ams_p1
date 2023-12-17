from stack import Stack
from error_check import opr_error, correct_opr_error, val_error, number_of_inputs_error
from easter_egg_list import find_easter, able_easter
import string
import threading
import sys
import math

stop_event = threading.Event()


class ThreerBasicOperations:
  operator = ["+", "-", "*","!"]

  def show_operators():
    print('[사용 가능한 연산자 : +, - , *, !]')
      
  def precedence(op):
    if op == '*': return 1
    elif op == '+' or op == '-': return 0
    elif op == '!': return 2
    else: return -1

  #사용자 입력 ex) 5+3*2
  def make_infix():
    infix = []
    while True:
      userInput = input('입력하세요: ')
      if userInput == '!':
        infix.append(userInput)
        break
      if userInput == '=':
        break

      #이스터에그 처리
      elif able_easter(userInput):
        find_easter(userInput)
        sys.exit(0)
      infix.append(userInput)

    return infix
  
  def infix_check(infix):
    if infix[-1] == '!':  # 팩토리얼 계산일 때
        return 1

    # 저장된 값의 개수가 홀수일 때(마지막 입력 숫자 X) Error!
    error_message = number_of_inputs_error(len(infix))
    if error_message:
      print(error_message)
      return error_message

    firstOp = ""
    if len(infix) > 1:
        firstOp = infix[1]
        error_message = correct_opr_error(firstOp)
        if error_message:
              print(error_message)
              return error_message  # 첫 번째 연산자 "+", "-", "*" 가 아닐 시 Error!

    for index, item in enumerate(infix):
        if index % 2:
            error_message = opr_error(firstOp, item)  # 첫 번째 연산자와 다를 시 Error!
            if error_message:
              print(error_message)
              return error_message

        else:
            error_message = val_error(item)
            if error_message:
              print(error_message)
              return error_message  # 짝수 인덱스의 값이 정수가 아닐 시 Error!

    return 2
   

  # 후위표기법 적용 ex) 532*+
  def make_postfix(infix):
    postfix = Stack()
    output = []
    for item in infix:
      if item in ThreerBasicOperations.operator:
        while not postfix.isEmpty():
          op = postfix.peek()
          
          #우선순위 높은 연산자 먼저 꺼내기
          if ThreerBasicOperations.precedence(item) <= ThreerBasicOperations.precedence(op):
            output.append(op)
            postfix.pop()
          else:
            break
        postfix.push(item)
      else:
        output.append(item)

    while not postfix.isEmpty():
      output.append(postfix.pop())

    return output

  #연산결과 출력
  def calculate(postfix):
    s = Stack()
    for token in postfix:
      #연산자 만나면
      if token in ThreerBasicOperations.operator:
        val2 = s.pop()
        val1 = s.pop()
        if token == '+': s.push(val1 + val2)
        elif token == '-': s.push(val1 - val2)
        elif token == '*': s.push(val1 * val2)
      #피연산자는 스택으로 출력
      else:
        item = int(token)
        s.push(item)
    return s.pop()

  def calculateFactorial(infix):
    if len(infix) != 2:
      return '[ERROR] Input Error'
    if not(is_integer(infix[0])):
      return '[SYETEM] ERROR! 정수가 아닌 값이 입력되었습니다.'
    infix[0] = int(infix[0])
    if infix[0] < 0:
      return '[ERROR] Out Of Range'
    
    return "= " + str(math.factorial(infix[0]))
  
def is_integer(n):
  try:
      float(n)
  except ValueError:
      return False
  return float(n).is_integer()

  