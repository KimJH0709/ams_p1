from stack import Stack
from error_check import opr_error, correct_opr_error, val_error, number_of_inputs_error, chech_minus_factorial
from easter_egg_list import find_easter, able_easter
import string
import threading
import sys
import keyboard
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
      infix.append(userInput)


    return infix
  
  def infix_check(infix):
    if infix[1] != '!':
      number_of_inputs_error(len(infix))  # 저장된 값의 개수가 짝수일 때(마지막 입력 숫자 X) Error!
      firstOp = ""

    if len(infix) > 1:
      firstOp = infix[1]
      correct_opr_error(firstOp) # 첫 번째 연산자 "+", "-", "*" 가 아닐 시 Error!

    for index, item in enumerate(infix):
      if index % 2:
        opr_error(firstOp, item) # 첫 번째 연산자와 다를 시 Error!
      else:
        val_error(item) # 짝수 인덱스의 값이 정수가 아닐 시 Error!
   

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
    fac_check = False
    for token in postfix:
      #연산자 만나면
      if token in ThreerBasicOperations.operator:
        val2 = s.pop()
        val1 = s.pop()
        if token == '+': s.push(val1 + val2)
        elif token == '-': s.push(val1 - val2)
        elif token == '*': s.push(val1 * val2)
        elif token == '!':
          chech_minus_factorial(val2)
          s.push(math.factorial(val2))
          fac_check = True
      #피연산자는 스택으로 출력
      else:
        item = int(token)
        s.push(item)

    if fac_check == False:
      return print(s.pop())
    else:
      return print("= "+str(s.pop()))
  
  
ThreerBasicOperations.show_operators()




while True:
    
  infix= ThreerBasicOperations.make_infix()
  try:
    ThreerBasicOperations.infix_check(infix)
  except:
     continue  # 에러 발생 시 결과값을 출력하지 않고 다시 입력을 받음
  postfix = ThreerBasicOperations.make_postfix(infix)
  result = ThreerBasicOperations.calculate(postfix)

  user_input = input("계속 사용 하시겠습니까? (y/n)")
  if user_input.lower() != 'y':
    sys.exit()
    break  # 종료 조건