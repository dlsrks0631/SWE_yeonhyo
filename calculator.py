import re

# Constants
EASTER_EGG_CODE = '987654321987654321'

ERROR_MESSAGE = "ERROR!"
EASTER_EGG_MESSAGE = "Hello! This Is Team Yeonhyo Easter Egg!!"

class Operator: # 연산자 클래스
    def add(num1, num2): # 덧셈.
        return int(num1) + int(num2)

    def sub(num1, num2): # 뺄셈.
        return int(num1) - int(num2)

    def mul(num1, num2): # 곱셈.
        return int(num1) * int(num2)
    
    operate = { # 연산자 메소드 딕셔너리
        '+': add,
        '-': sub,
        '*': mul,
    }

# 정규표현식을 이용한 정수 확인 함수
def is_integer(str):
    """Return True if the string is an integer."""
    return re.match("[-]?\d+$", str) != None

def run_calculator():
    """Run calculator and return the result"""
    result = 0 # 계산 결과
    operand = None # 피연산자
    operator = None # 연산자
    is_error = False # 오류 Flag
    is_easter_egg = False # 이스터에그 Flag

    '''
    반복문 Logic
    1. 사용자 입력
    2. 입력에 따른 처리
        - 피연산자, 연산자가 번갈아 입력된다고 가정한다.
        2.1. 피연산자가 입력된 경우 
            - 피연산자를 operand 변수에 저장
        2.2. 연산자가 입력된 경우
            - 저장된 result, operand, operator를 이용해 연산
            - 결과를 result에 저장
            - 입력받은 연산자를 operator 변수에 저장
            - 등호가 입력된 경우 결과를 반환한다.                
    '''
    while True:
        user_input = input() # 사용자 입력을 문자열 형태로 저장

        if user_input == EASTER_EGG_CODE: # 이스터에그 코드
            is_easter_egg = True
            break

        if is_integer(user_input): # 정수가 입력된 경우
            # 정수가 연속으로 입력된 경우 에러메세지 출력
            if operand != None: 
                is_error = True
                break

            operand = int(user_input) # 사용자 입력을 피연산자 변수에 저장

        elif user_input in Operator.operate or user_input == '=': # 연산자 또는 등호가 입력된 경우
            # 첫 입력이 연산자인 경우 또는 연산자가 연속으로 입력된 경우 에러메세지 출력 
            if operand == None: 
                is_error = True
                break
            
            if operator == None: # 숫자가 처음으로 입력된 경우
                result = operand
            else: # 연산 후 결과를 result에 저장
                result = Operator.operate[operator](result, operand)
            operand = None # 연산 후 피연산자 초기화

            operator = user_input # 사용자 입력을 연산자 변수에 저장

            if operator == '=': # 등호가 입력된 경우 반복문 종료 후 결과 출력
                break

        else: # 연산자, 정수 외의 입력에 대해 에러메세지 출력
            is_error = True
            break

    if is_easter_egg:
        return EASTER_EGG_MESSAGE
    if is_error:
        return ERROR_MESSAGE
    return result


def main():
    print(run_calculator())

if __name__ == "__main__":
    main()