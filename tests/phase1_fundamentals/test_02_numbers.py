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


class TestPracticalUsage:
    """실무 활용 - 실제로 이렇게 씁니다"""

    def test_even_odd_check(self):
        """짝수/홀수 판별 - 나머지 연산 활용"""
        number = 7
        is_even = number % 2 == 0  # 2로 나눈 나머지가 0이면 짝수
        is_odd = number % 2 == 1  # 2로 나눈 나머지가 1이면 홀수

        assert is_odd is True
        assert is_even is False

        # 여러 숫자 판별
        assert 10 % 2 == 0  # 짝수
        assert 15 % 2 == 1  # 홀수

    def test_cyclic_index(self):
        """순환 인덱스 - 요일, 시간 등에 활용"""
        # 실전 활용: 순환 인덱스 (0, 1, 2, 0, 1, 2, ...)
        days = ["월", "화", "수", "목", "금", "토", "일"]

        # 오늘이 월요일(0)이고 10일 후는?
        today = 0
        day_number = 10
        future_day = (today + day_number) % 7
        assert future_day == 3  # 목요일

        # 시계 계산: 현재 10시, 5시간 후는?
        current_hour = 10
        hours_later = 5
        new_hour = (current_hour + hours_later) % 12
        assert new_hour == 3  # 3시

    def test_divmod_time_conversion(self):
        """divmod()로 시간 변환하기"""
        # divmod(a, b)는 (a // b, a % b)를 튜플로 반환
        quotient, remainder = divmod(17, 5)
        assert quotient == 3  # 몫
        assert remainder == 2  # 나머지

        # 실전 활용: 초를 시:분:초로 변환
        total_seconds = 3725  # 3725초

        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)

        assert hours == 1
        assert minutes == 2
        assert seconds == 5
        # 3725초 = 1시간 2분 5초

    def test_discount_calculation(self):
        """할인가 계산"""
        original_price = 50000
        discount_percent = 30

        discount_price = original_price * (1 - discount_percent / 100)
        assert discount_price == 35000.0

        # 다른 방식
        discount_amount = original_price * discount_percent / 100
        final_price = original_price - discount_amount
        assert final_price == 35000.0

    def test_average_calculation(self):
        """평균 계산"""
        scores = [85, 92, 78, 96, 88]
        average = sum(scores) / len(scores)
        assert average == 87.8

        # 반올림해서 정수로
        rounded_avg = round(average)
        assert rounded_avg == 88

    def test_circle_area(self):
        """원의 넓이 계산"""
        radius = 5
        area = math.pi * radius**2
        assert round(area, 2) == 78.54

        # 둘레
        circumference = 2 * math.pi * radius
        assert round(circumference, 2) == 31.42

    def test_pythagorean_theorem(self):
        """피타고라스 정리 - 직각삼각형 빗변"""
        a, b = 3, 4
        c = math.sqrt(a**2 + b**2)
        assert c == 5.0

        # math.hypot()을 사용하면 더 간단
        assert math.hypot(3, 4) == 5.0

    def test_compound_interest(self):
        """복리 이자 계산"""
        # A = P(1 + r/n)^(nt)
        principal = 1000000  # 원금 100만원
        rate = 0.05  # 연 5%
        times_per_year = 12  # 월복리
        years = 3  # 3년

        amount = principal * (1 + rate / times_per_year) ** (times_per_year * years)
        assert round(amount) == 1161617  # 약 116만원

    def test_number_formatting(self):
        """숫자 포맷팅 - 보기 좋게 출력하기"""
        number = 1234567.89

        # 천 단위 구분자
        formatted = f"{number:,}"
        assert formatted == "1,234,567.89"

        # 소수점 자릿수 지정
        pi = 3.14159265
        assert f"{pi:.2f}" == "3.14"  # 소수점 2자리
        assert f"{pi:.4f}" == "3.1416"  # 소수점 4자리

        # 고정 너비 (공백 채움)
        assert f"{42:5d}" == "   42"  # 5자리, 오른쪽 정렬
        assert f"{42:<5d}" == "42   "  # 5자리, 왼쪽 정렬
        assert f"{42:05d}" == "00042"  # 5자리, 0으로 채움

        # 퍼센트
        ratio = 0.8567
        assert f"{ratio:.1%}" == "85.7%"

    def test_convert_bases(self):
        """진수 변환 함수들"""
        number = 42

        # bin(): 2진수 문자열
        assert bin(number) == "0b101010"

        # oct(): 8진수 문자열
        assert oct(number) == "0o52"

        # hex(): 16진수 문자열
        assert hex(number) == "0x2a"

        # 접두사 없이 얻고 싶다면
        assert bin(number)[2:] == "101010"
        assert format(number, "b") == "101010"

        # 문자열을 특정 진수로 해석
        assert int("1010", 2) == 10  # 2진수 "1010" → 10
        assert int("ff", 16) == 255  # 16진수 "ff" → 255


class TestEdgeCases:
    """주의사항 - 자주 하는 실수와 함정"""

    def test_float_precision_trap(self):
        """실수의 정밀도 문제 - 컴퓨터는 소수를 정확히 저장 못해요!"""
        # 컴퓨터는 2진수를 쓰기 때문에 일부 소수를 정확히 표현 못합니다
        # 이건 Python만의 문제가 아니라 모든 프로그래밍 언어의 문제예요

        result = 0.1 + 0.2
        # 놀랍게도 정확히 0.3이 아닙니다!
        assert result != 0.3  # 0.30000000000000004 같은 값이 나옴

        # 해결책 1: 근사값 비교 (차이가 매우 작으면 같다고 판단)
        assert abs(result - 0.3) < 0.0001

        # 해결책 2: math.isclose() 사용 (권장)
        assert math.isclose(result, 0.3)

        # 해결책 3: 정확한 계산이 필요하면 Decimal 모듈 사용
        from decimal import Decimal

        precise = Decimal("0.1") + Decimal("0.2")
        assert precise == Decimal("0.3")

    def test_division_always_float(self):
        """나눗셈(/)은 항상 float를 반환"""
        # 정수끼리 나눠도 float!
        result = 10 / 2
        assert result == 5.0
        assert type(result) == float  # int가 아님!

        # 정수 결과가 필요하면 // 사용
        result_int = 10 // 2
        assert result_int == 5
        assert type(result_int) == int

    def test_int_truncation_not_rounding(self):
        """int()는 반올림이 아니라 버림!"""
        # int()는 소수점 아래를 그냥 버립니다 (0 방향으로)
        assert int(3.9) == 3  # 반올림이면 4겠지만, 버림이라 3
        assert int(3.1) == 3

        # 음수도 0 방향으로 버림
        assert int(-3.9) == -3  # -4가 아님!
        assert int(-3.1) == -3

        # 반올림을 원하면 round() 사용
        assert round(3.9) == 4
        assert round(3.1) == 3

    def test_bankers_rounding(self):
        """Python의 round()는 '은행원 반올림'을 사용"""
        # 정확히 0.5일 때 가장 가까운 '짝수'로 반올림
        # 일반적인 사사오입과 다릅니다!

        assert round(0.5) == 0  # 0.5 → 0 (짝수)
        assert round(1.5) == 2  # 1.5 → 2 (짝수)
        assert round(2.5) == 2  # 2.5 → 2 (짝수) - 3이 아님!
        assert round(3.5) == 4  # 3.5 → 4 (짝수)

        # 0.5가 아닌 경우는 일반적인 반올림
        assert round(2.4) == 2
        assert round(2.6) == 3

    def test_negative_division_gotcha(self):
        """음수 나눗셈 주의"""
        # // 는 항상 "내림" (더 작은 정수 방향)
        assert 7 // 3 == 2  # 2.33... → 2
        assert -7 // 3 == -3  # -2.33... → -3 (내림이라 -3)

        # % 결과의 부호는 나누는 수의 부호를 따름
        assert 7 % 3 == 1
        assert -7 % 3 == 2  # -1이 아님! (3 - 1 = 2)
        assert 7 % -3 == -2
        assert -7 % -3 == -1

    def test_operator_precedence_trap(self):
        """연산자 우선순위 함정"""
        # ** 는 오른쪽에서 왼쪽으로 결합
        assert 2**3**2 == 512  # 2^(3^2) = 2^9 = 512, (2^3)^2 = 64가 아님!

        # 음수 거듭제곱 주의!
        assert -2**2 == -4  # -(2**2) = -4
        assert (-2) ** 2 == 4  # (-2) ** 2 = 4

        # 헷갈리면 괄호 사용!
        assert (2**3) ** 2 == 64

    def test_zero_division(self):
        """0으로 나누기"""
        import pytest

        # 정수/실수를 0으로 나누면 ZeroDivisionError
        with pytest.raises(ZeroDivisionError):
            result = 10 / 0

        with pytest.raises(ZeroDivisionError):
            result = 10 // 0

        with pytest.raises(ZeroDivisionError):
            result = 10 % 0

    def test_very_large_float(self):
        """float의 범위 제한"""
        # float는 크기 제한이 있음 (약 1.8 * 10^308)
        # 너무 크면 inf(무한대)가 됨
        huge = 1e308
        assert huge * 10 == float("inf")

        # int는 크기 제한 없음 (Python의 장점!)
        very_big = 10**1000  # 이건 가능
        assert type(very_big) == int


