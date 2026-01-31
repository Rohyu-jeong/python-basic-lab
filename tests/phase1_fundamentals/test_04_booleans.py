"""
Phase 1 - Booleans (불리언)
===========================
학습 목표: True/False의 개념과 다양한 값들의 참/거짓 판별법 이해

핵심 개념:
- bool 타입은 True와 False 두 가지 값만 가짐
- 모든 파이썬 객체는 불리언으로 평가될 수 있음 (truthy/falsy)
- 비교 연산자와 논리 연산자로 조건을 만들 수 있음
"""


class TestBasicConcept:
    """기본 개념 - 가장 먼저 알아야 할 것"""

    def test_true_and_false(self):
        """불리언의 두 가지 값: True와 False"""
        # 불리언은 "예/아니오"를 나타내는 타입
        # 반드시 대문자로 시작해야 함 (true나 false는 에러!)
        is_sunny = True
        is_raining = False

        assert is_sunny == True
        assert is_raining == False

        # 타입 확인
        assert type(True) == bool
        assert type(False) == bool

    def test_comparison_operators(self):
        """비교 연산자 - 두 값을 비교하면 불리언이 나옴"""
        # == : 같은가?
        assert (5 == 5) == True
        assert (5 == 3) == False

        # != : 다른가?
        assert (5 != 3) == True
        assert (5 != 5) == False

        # > : 큰가?
        assert (5 > 3) == True
        assert (3 > 5) == False

        # < : 작은가?
        assert (3 < 5) == True
        assert (5 < 3) == False

        # >= : 크거나 같은가?
        assert (5 >= 5) == True
        assert (5 >= 3) == True

        # <= : 작거나 같은가?
        assert (3 <= 5) == True
        assert (3 <= 3) == True

    def test_logical_operators(self):
        """논리 연산자 - 여러 조건을 조합"""
        # and: 둘 다 True여야 True
        # "비가 오고 AND 우산이 없으면" 처럼 사용
        assert (True and True) == True
        assert (True and False) == False
        assert (False and True) == False
        assert (False and False) == False

        # or: 하나라도 True면 True
        # "토요일 OR 일요일이면 쉰다" 처럼 사용
        assert (True or True) == True
        assert (True or False) == True
        assert (False or True) == True
        assert (False or False) == False

        # not: 반대로 뒤집기
        assert (not True) == False
        assert (not False) == True

    def test_bool_is_number(self):
        """놀라운 사실: True는 1이고, False는 0"""
        # 파이썬에서 bool은 int의 자식 클래스
        # 그래서 숫자처럼 연산 가능!
        assert True == 1
        assert False == 0
        assert True + True == 2
        assert True * 10 == 10
        assert False * 100 == 0

        # 이걸 활용하면 True 개수를 셀 수 있음
        conditions = [True, False, True, True, False]
        true_count = sum(conditions)  # True는 1로 계산됨
        assert true_count == 3


class TestPracticalUsage:
    """실무 활용 - 실제로 이렇게 씁니다"""

    def test_truthy_values(self):
        """Truthy - True처럼 취급되는 값들"""
        # 파이썬에서는 True가 아니어도 "참으로 취급"되는 값들이 있음
        # bool() 함수로 어떤 값이든 True/False로 변환 가능

        # 숫자: 0이 아닌 모든 수는 truthy
        assert bool(1) == True
        assert bool(42) == True
        assert bool(-1) == True
        assert bool(0.1) == True

        # 문자열: 비어있지 않으면 truthy
        assert bool("hello") == True
        assert bool(" ") == True  # 공백도 문자!
        assert bool("0") == True  # 문자 "0"은 비어있지 않음

        # 컬렉션: 뭔가 들어있으면 truthy
        assert bool([1, 2, 3]) == True
        assert bool({"key": "value"}) == True
        assert bool((1,)) == True

    def test_falsy_values(self):
        """Falsy - False처럼 취급되는 값들 (외워두면 좋음!)"""
        # 이 6가지만 기억하면 됨!

        # 1. False 자체
        assert bool(False) == False

        # 2. None (값이 없음을 나타냄)
        assert bool(None) == False

        # 3. 숫자 0 (정수, 실수 모두)
        assert bool(0) == False
        assert bool(0.0) == False

        # 4. 빈 문자열
        assert bool("") == False

        # 5. 빈 리스트, 빈 튜플
        assert bool([]) == False
        assert bool(()) == False

        # 6. 빈 딕셔너리, 빈 집합
        assert bool({}) == False
        assert bool(set()) == False

    def test_short_circuit_evaluation(self):
        """단락 평가 - 파이썬의 똑똑한 계산법"""
        # and: 앞이 False면 뒤는 볼 필요 없음
        # or: 앞이 True면 뒤는 볼 필요 없음

        # and는 첫 번째 falsy 값 또는 마지막 값을 반환
        assert (0 and "hello") == 0  # 0이 falsy라 바로 반환
        assert ("hello" and "world") == "world"  # 둘 다 truthy면 마지막 값

        # or는 첫 번째 truthy 값 또는 마지막 값을 반환
        assert (0 or "hello") == "hello"  # 0이 falsy라 다음으로
        assert ("hello" or "world") == "hello"  # hello가 truthy라 바로 반환
        assert (0 or "" or None) == None  # 다 falsy면 마지막 값

    def test_default_value_pattern(self):
        """or를 이용한 기본값 패턴"""
        # 값이 없을 때 기본값을 설정하는 흔한 패턴

        user_input = ""  # 사용자가 아무것도 입력 안 함
        name = user_input or "익명"  # 빈 문자열은 falsy라 "익명" 사용
        assert name == "익명"

        user_input = "철수"
        name = user_input or "익명"  # "철수"는 truthy라 그대로 사용
        assert name == "철수"


class TestEdgeCases:
    """주의사항 - 자주 하는 실수와 함정"""

    def test_equality_vs_identity(self):
        """== vs is 의 차이"""
        # == : 값이 같은가?
        # is : 같은 객체인가? (메모리 주소가 같은가?)

        a = [1, 2, 3]
        b = [1, 2, 3]
        c = a

        # a와 b는 값은 같지만 다른 객체
        assert (a == b) == True  # 값 비교: 같음
        assert (a is b) == False  # 객체 비교: 다름

        # a와 c는 같은 객체
        assert (a == c) == True
        assert (a is c) == True

        # 불리언과 None은 is로 비교하는 게 관례
        x = True
        assert (x is True) == True

        y = None
        assert (y is None) == True

    def test_chained_comparison(self):
        """비교 연산자 체이닝 - 파이썬만의 편리한 문법"""
        x = 5

        # 다른 언어: (x > 0) and (x < 10)
        # 파이썬: 수학처럼 쓸 수 있음!
        assert (0 < x < 10) == True  # 0 < 5 < 10
        assert (1 <= x <= 5) == True  # 1 <= 5 <= 5

        # 더 긴 체이닝도 가능
        assert (0 < 1 < 2 < 3 < 4) == True

    def test_none_comparison(self):
        """None과 비교할 때 주의점"""
        value = None

        # None은 반드시 is로 비교!
        assert (value is None) == True
        assert (value is not None) == False

        # == 도 동작하지만, 권장하지 않음
        # 왜냐하면 커스텀 클래스에서 __eq__를 오버라이드하면
        # 예상치 못한 결과가 나올 수 있기 때문

    def test_common_mistake_zero_vs_none(self):
        """흔한 실수: 0과 None을 구분 못 함"""
        # 둘 다 falsy지만 완전히 다른 의미!

        score = 0  # 점수가 0점
        no_score = None  # 점수가 아직 없음

        # if문에서 주의!
        # if not score: 는 0점도 "점수 없음"으로 처리해버림

        # 올바른 방법: None인지 명시적으로 확인
        has_score = score is not None
        assert has_score == True  # 0점이지만 점수는 있음!

        has_score = no_score is not None
        assert has_score == False  # 진짜 점수 없음


class TestTips:
    """꿀팁 - 알아두면 유용한 것들"""

    def test_any_and_all(self):
        """any()와 all() - 여러 조건을 한번에 체크"""
        numbers = [2, 4, 6, 8, 10]

        # all(): 모두 True여야 True
        # "모든 숫자가 짝수인가?"
        all_even = all(n % 2 == 0 for n in numbers)
        assert all_even == True

        # any(): 하나라도 True면 True
        # "10보다 큰 수가 하나라도 있는가?"
        has_big_number = any(n > 10 for n in numbers)
        assert has_big_number == False

        has_big_number = any(n >= 10 for n in numbers)
        assert has_big_number == True

    def test_bool_conversion(self):
        """불리언 변환 활용"""
        # 빈 리스트 체크 - 두 방법 모두 가능
        items = []

        # 방법 1: 명시적 (초보자에게 추천)
        is_empty = len(items) == 0
        assert is_empty == True

        # 방법 2: Pythonic (파이썬스러운 방법)
        is_empty = not items  # 빈 리스트는 falsy
        assert is_empty == True

        # 아이템이 있는지 확인
        items = [1, 2, 3]
        has_items = bool(items)  # 또는 그냥 if items:
        assert has_items == True

    def test_ternary_operator(self):
        """삼항 연산자 - 한 줄로 조건 처리"""
        age = 20

        # 일반 if문
        # if age >= 18:
        #     status = "성인"
        # else:
        #     status = "미성년"

        # 삼항 연산자로 한 줄에!
        # 형식: [참일 때 값] if [조건] else [거짓일 때 값]
        status = "성인" if age >= 18 else "미성년"
        assert status == "성인"

        # 실용 예: 절대값 구하기
        x = -5
        abs_x = x if x >= 0 else -x
        assert abs_x == 5

    def test_comparison_chain_gotcha(self):
        """비교 체이닝의 함정"""
        # 이건 예상대로 동작
        assert (1 < 2 < 3) == True  # 1 < 2 and 2 < 3

        # 이건 주의! (괄호 위치가 중요)
        result = 1 < 2 < 3
        assert result == True

        # 이렇게 쓰면 다른 의미!
        # (1 < 2) < 3 은 True < 3, 즉 1 < 3
        result = (1 < 2) < 3
        assert result == True  # 우연히 True지만 의미가 다름!
