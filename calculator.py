import re

# 상수
EASTER_EGG_CODE = '987654321987654321'
ERROR_MESSAGE = "ERROR!"
EASTER_EGG_MESSAGE = "Hello! This Is Team Yeonhyo Easter Egg!!"

# 이스터에그 예외 정의
class EasterEggException(Exception):
    def __init__(self, message=EASTER_EGG_MESSAGE):
        super().__init__(message)

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

    # 연산자 우선순위 딕셔너리
    precedence = {
        '+': 1, 
        '-': 1,
        '*': 2,
    }

# 정규표현식을 이용한 정수 확인 함수
def is_integer(str):
    """Returns True if the string is an integer."""
    return re.match("[-]?\d+$", str) != None

# 후위표현식 계산 함수
def calc_postfix_expr(postfix_expression):
    """Calculate postfix expression"""
    # 피연산자 스택
    operand_stack = []

    for element in postfix_expression:
        # 피연산자인 경우
        if is_integer(element):
            # 피연산자 스택에 삽입
            operand_stack.append(int(element))
        # 연산자인 경우
        elif element in Operator.operate:
            # 피연산자 스택에서 두 피연산자를 추출
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()

            # 연산자와 피연산자들로 연산 수행 후 result에 저장
            result = Operator.operate[element](operand1, operand2)
            
            # 피연산자 스택에 결과 삽입
            operand_stack.append(result)

    return operand_stack.pop()

# 중위표현식을 후위표현식으로 변환
def infix_to_postfix(infix_expression):
    """Converts an infix expression to a postfix expression"""
    # 연산자 스택
    operator_stack = []
    # 후위표현식 리스트
    postfix_expression = []

    for element in infix_expression:
        # 피연산자인 경우
        if is_integer(element):
            # 후위표현식 리스트에 삽입
            postfix_expression.append(element)
        # 연산자인 경우
        elif element in Operator.operate:
            # 스택의 상단에 있는 연산자와 현재 연산자의 우선순위를 비교
            # - 현재 연산자보다 상단의 연산자 우선순위가 낮으면 현재 연산자를 스택에 삽입
            # - 현재 연산자보다 상단의 연산자 우선순위가 높거나 같으면 스택에서 pop하여 후위표현식 리스트에 삽입
            while operator_stack:
                operator = operator_stack[-1]
                if Operator.precedence[element] <= Operator.precedence[operator]:
                    postfix_expression.append(operator)
                    operator_stack.pop()
                else:
                    break
            operator_stack.append(element)

    # 스택에 남은 연산자들을 후위표현식에 삽입
    while operator_stack:
        postfix_expression.append(operator_stack.pop())

    return postfix_expression

# 사용자 입력을 이용해 계산하고 결과를 반환한다.
def calculate(user_inputs):
    # 사용자 입력을 중위표현식에서 후위표현식으로 변환
    user_inputs_postfix = infix_to_postfix(user_inputs)
    # 변환된 입력을 이용해 계산
    result = calc_postfix_expr(user_inputs_postfix)
    # 계산 결과 반환
    return result

def get_user_input():
    """Gets user inpus and return input as a list"""
    user_inputs = []
    user_input = None

    # 등호가 입력될 때까지 반복
    while True:
        # 사용자 입력을 문자열 형태로 저장
        user_input = input()
        if user_input == '=':
            break
        
        # 사용자 입력을 inputs 리스트에 삽입
        user_inputs.append(user_input)
        
        # 이스터에그 코드가 입력된 경우 즉시 반환
        if user_input == EASTER_EGG_CODE: 
            raise EasterEggException
        
    return user_inputs

# 사용자 입력에 오류가 있는지 확인한다.
def has_error(user_inputs):
    # 사용자 입력이 없는 경우 ('='만 입력된 경우)
    is_empty = len(user_inputs) == 0
    # 마지막 입력이 연산자인 경우
    is_operator_last_elem = user_inputs[-1] in Operator.operate
    # 모든 짝수 번째 요소들이 정수인 경우
    is_integer_even_elem = all(is_integer(element) for element in user_inputs[0::2])
    # 모든 홀수 번째 요소들이 연산자인 경우
    is_operator_odd_elem = all((element in Operator.operate) for element in user_inputs[1::2])
    
    return is_empty or is_operator_last_elem or not (is_integer_even_elem and is_operator_odd_elem)


def run_calculator():
    """Run calculator and return the result."""
    # 사용자 입력
    try:
        user_inputs = get_user_input()
    # 이스터에그 코드 입력 시 즉시 이스터에그 메시지 출력
    except EasterEggException as message:
        return message
    
    # 입력 오류 존재 시 오류 메시지 반환
    if has_error(user_inputs):
        return ERROR_MESSAGE

    # 입력 식 계산
    result = calculate(user_inputs)

    # 계산 결과 반환
    return result

def main():
    print(run_calculator())

if __name__ == "__main__":
    main()