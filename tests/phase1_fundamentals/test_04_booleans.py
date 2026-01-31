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


