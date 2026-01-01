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

    def test_no_type_declaration_needed(self):
        """Python은 변수 타입을 미리 선언하지 않아도 됩니다 (동적 타이핑)"""
        # Java나 C에서는: int number = 10;
        # Python에서는 그냥:
        number = 10

        # Python이 알아서 "아, 이건 정수구나" 파악함
        assert type(number) == int

    def test_type_can_change(self):
        """같은 변수에 다른 타입의 값을 넣을 수 있습니다"""
        # 처음에는 숫자
        data = 42
        assert type(data) == int

        # 이제 문자열로 바꿈 (다른 언어에서는 에러나는 경우가 많음!)
        data = "마흔둘"
        assert type(data) == str

        # 리스트로도 바꿀 수 있음
        data = [4, 2]
        assert type(data) == list

    def test_check_type_with_type_function(self):
        """type() 함수로 변수의 타입을 확인할 수 있습니다"""
        integer_var = 10
        float_var = 3.14
        string_var = "hello"
        bool_var = True

        assert type(integer_var) == int  # 정수
        assert type(float_var) == float  # 실수 (소수점)
        assert type(string_var) == str  # 문자열
        assert type(bool_var) == bool  # 불리언 (참/거짓)

    def test_isinstance_for_type_checking(self):
        """isinstance()는 타입 체크의 더 좋은 방법입니다"""
        number = 42

        # type() == 보다 isinstance()를 더 권장
        # 이유: 상속 관계도 체크해줌 (OOP에서 배울 내용)
        assert isinstance(number, int)
        assert isinstance(3.14, float)
        assert isinstance("hello", str)

        # 여러 타입 중 하나인지 확인도 가능
        value = 100
        assert isinstance(value, (int, float))  # int 또는 float인지

    