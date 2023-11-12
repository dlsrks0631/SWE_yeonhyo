import re

# 상수
EASTER_EGG_CODE = '987654321987654321'
ERROR_MESSAGE = "ERROR!"
EASTER_EGG_MESSAGE = "Hello! This Is Team Yeonhyo Easter Egg!!"

# 연산자 클래스
class Operator: 
    # 덧셈
    def add(num1, num2): 
        return int(num1) + int(num2)

    # 뺄셈
    def sub(num1, num2): 
        return int(num1) - int(num2)

    # 곱셈
    def mul(num1, num2): 
        return int(num1) * int(num2)
    
    # 연산자 메소드 딕셔너리
    operate = { 
        '+': add,
        '-': sub,
        '*': mul,
    }

# 정규표현식을 이용한 정수 확인 함수
def is_integer(str):
    """Return True if the string is an integer."""
    return re.match("[-]?\d+$", str) != None

def run_calculator():
    """Run calculator and return the result."""
    result = None # 계산 결과
    operand = None # 피연산자
    operator = None # 연산자
    is_error = False # 오류 Flag
    is_easter_egg = False # 이스터에그 Flag

    '''
    반복문 Logic
    1. 사용자 입력
    2. 입력에 따른 처리
        - 피연산자, 연산자가 번갈아 입력된다고 가정
        2.1. 피연산자가 입력된 경우
            2.1.1. 피연산자가 처음 입력된 경우
                - result에 입력된 피연산자 저장
            2.1.2. 피연산자와 연산자가 저장된 상태에서 피연산자가 입력된 경우
                - 저장된 result, operand, operator를 이용해 연산
                - 결과를 result에 저장
        2.2. 연산자가 입력된 경우
            - 입력받은 연산자를 operator 변수에 저장
        2.3. 등호가 입력된 경우
            - 결과 반환
        2.4. 이스터에그 코드가 입력된 경우
            - 이스터에그 메세지 출력
    '''
    while True:
        # 사용자 입력을 문자열 형태로 저장
        user_input = input() 

        # 이스터에그 코드가 입력된 경우
        if user_input == EASTER_EGG_CODE: 
            is_easter_egg = True
            break

        # 등호가 입력된 경우
        if user_input == '=': 
            # 연잔사 입력 후 '='가 입력된 경우 에러메시지 출력
            if operator != None:
                is_error = True
            break

        # 정수가 입력된 경우
        if is_integer(user_input): 
            # 피연산자가 연속으로 입력된 경우 에러메시지 출력
            if operator == None and result != None: 
                is_error = True
                break

            # 사용자 입력을 피연산자 변수에 저장
            operand = int(user_input) 
            
            # 피연산자가 처음으로 입력된 경우 입력을 result에 저장
            if result == None: 
                result = operand
            else: 
                # 저장된 연산자와 피연산자를 이용해 연산 후 결과를 result에 저장
                result = Operator.operate[operator](result, operand)
            
            # 연산 후 연산자/피연산자 변수 초기화
            operator = None 
            operand = None 

        # 연산자가 입력된 경우
        elif user_input in Operator.operate: 
            # 첫 입력이 연산자인 경우 에러메시지 출력
            # 연산자가 연속으로 입력된 경우 에러메시지 출력 
            if result == None or operator != None:
                is_error = True
                break

            # 사용자 입력을 연산자 변수에 저장
            operator = user_input 

        # 연산자, 정수 외의 입력에 대해 에러메시지 출력
        else: 
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