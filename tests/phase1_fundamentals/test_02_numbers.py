"""
Phase 1 - Numbers (숫자)
========================
학습 목표: Python에서 숫자를 다루는 모든 방법을 익힙니다.

핵심 개념:
- int(정수): 소수점 없는 숫자 (1, -5, 1000)
- float(실수): 소수점 있는 숫자 (3.14, -0.5)
- 산술 연산자: +, -, *, /, //, %, **
- 진수 변환: 2진수, 8진수, 16진수
- 숫자 관련 내장 함수들
"""

import math


class TestBasicConcept:
    """기본 개념 - 가장 먼저 알아야 할 것"""

    def test_integer_basics(self):
        """정수(int)의 기본 - 소수점 없는 숫자"""
        # 정수는 소수점이 없는 숫자입니다
        age = 25
        temperature = -10  # 음수도 정수
        population = 51_000_000  # 큰 숫자는 언더스코어로 구분 가능 (Python 3.6+)

        assert age == 25
        assert temperature == -10
        assert population == 51000000  # 언더스코어는 값에 영향 없음

        # type() 함수로 타입 확인
        assert type(age) == int
        assert type(100) == int

    def test_float_basics(self):
        """실수(float)의 기본 - 소수점 있는 숫자"""
        # 실수는 소수점이 있는 숫자입니다
        pi = 3.14159
        height = 175.5
        tiny = 0.001
        negative_float = -273.15  # 절대 영도

        assert type(pi) == float
        assert type(height) == float

        # 정수처럼 보여도 소수점이 있으면 float
        whole_float = 10.0
        assert type(whole_float) == float

    def test_basic_arithmetic(self):
        """기본 사칙연산 (+, -, *, /)"""
        a, b = 10, 3

        # 덧셈
        assert a + b == 13

        # 뺄셈
        assert a - b == 7

        # 곱셈
        assert a * b == 30

        # 나눗셈 - 항상 float 결과!
        assert a / b == 10 / 3  # 3.333...
        assert type(a / b) == float

        # 정수끼리 나눠도 float!
        assert 10 / 2 == 5.0
        assert type(10 / 2) == float

    def test_integer_division_and_modulo(self):
        """정수 나눗셈(//)과 나머지(%) - 매우 자주 쓰임!"""
        # // (정수 나눗셈): 몫만 구함 (소수점 버림)
        assert 10 // 3 == 3  # 10 ÷ 3 = 3 나머지 1
        assert 17 // 5 == 3  # 17 ÷ 5 = 3 나머지 2

        # % (나머지 연산 = 모듈로): 나머지만 구함
        assert 10 % 3 == 1  # 10을 3으로 나눈 나머지
        assert 17 % 5 == 2  # 17을 5로 나눈 나머지

    def test_power_operator(self):
        """거듭제곱(**) - 제곱, 세제곱 등"""
        # ** 연산자로 거듭제곱
        assert 2**3 == 8  # 2의 3제곱 = 2 * 2 * 2
        assert 3**2 == 9  # 3의 제곱 = 3 * 3
        assert 10**0 == 1  # 모든 수의 0제곱은 1

        # 소수 지수도 가능
        assert 4**0.5 == 2.0  # 4의 제곱근 = √4 = 2
        assert 8 ** (1 / 3) == 2.0  # 8의 세제곱근 = ³√8 = 2

        # pow() 함수도 동일한 기능
        assert pow(2, 3) == 8

    def test_type_conversion(self):
        """타입 변환 - int와 float 사이 변환"""
        # float → int: 소수점 아래 버림 (반올림 아님!)
        assert int(3.7) == 3  # 3.7에서 .7을 버림
        assert int(3.2) == 3
        assert int(-3.7) == -3  # 음수도 0 방향으로 버림

        # int → float: 그냥 .0이 붙음
        assert float(5) == 5.0

        # 문자열 → 숫자
        assert int("42") == 42
        assert float("3.14") == 3.14

        # 숫자 → 문자열
        assert str(123) == "123"
        assert str(3.14) == "3.14"

    def test_binary_octal_hex(self):
        """다양한 진수로 숫자 표현하기"""
        # 2진수: 0b 또는 0B 접두사
        binary = 0b1010  # 2진수 1010 = 10진수 10
        assert binary == 10

        # 8진수: 0o 또는 0O 접두사
        octal = 0o17  # 8진수 17 = 10진수 15
        assert octal == 15

        # 16진수: 0x 또는 0X 접두사
        hexa = 0xFF  # 16진수 FF = 10진수 255
        assert hexa == 255

        # 모두 같은 숫자!
        assert 0b11111111 == 0o377 == 0xFF == 255


