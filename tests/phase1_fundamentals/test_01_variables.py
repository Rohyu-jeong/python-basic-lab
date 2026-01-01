"""
Phase 1 - 변수 (Variables)
==========================
학습 목표: Python에서 변수가 무엇이고 어떻게 사용하는지 배웁니다.

핵심 개념:
- 변수는 데이터를 담는 이름표입니다
- Python은 동적 타이핑 언어입니다
- 같은 변수에 다른 타입의 값을 넣을 수 있습니다
- 변수 이름에는 규칙이 있습니다
"""


class TestBasicConcept:
    """기본 개념 - 가장 먼저 알아야 할 것"""

    def test_variable_is_a_name_tag(self):
        """변수는 값에 붙이는 이름표입니다"""
        # 변수 = 값
        # '=' 는 "같다"가 아니라 "할당한다(넣는다)"는 의미
        message = "안녕하세요"

        # message라는 이름으로 "안녕하세요"를 꺼내 쓸 수 있음
        assert message == "안녕하세요"

    def test_variable_assignment(self):
        """변수에 값을 넣는 것을 '할당(assignment)'이라고 합니다"""
        # 숫자 할당
        age = 25
        assert age == 25

        # 문자열 할당
        name = "김파이썬"
        assert name == "김파이썬"

        # 소수점 숫자(실수) 할당
        height = 175.5
        assert height == 175.5

    def test_variable_can_change(self):
        """변수의 값은 바꿀 수 있습니다 (그래서 '변'수입니다)"""
        score = 0
        assert score == 0

        # 점수가 올랐다!
        score = 100
        assert score == 100

        # 또 바뀔 수 있음
        score = 85
        assert score == 85
        