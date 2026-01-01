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

    def test_assign_same_value_to_multiple(self):
        """여러 변수에 같은 값을 한 번에 할당"""
        # 모두 0으로 초기화하고 싶을 때
        a = b = c = 0

        assert a == 0
        assert b == 0
        assert c == 0

    def test_assign_multiple_values(self):
        """여러 변수에 각각 다른 값을 한 줄로 할당"""
        # 콤마로 구분해서 한 줄에 여러 변수 할당
        name, age, city = "김파이썬", 25, "서울"

        assert name == "김파이썬"
        assert age == 25
        assert city == "서울"

    def test_swap_values(self):
        """두 변수의 값 교환 - Python의 우아한 방법"""
        a = 10
        b = 20

        # 다른 언어에서는 임시 변수가 필요:
        # temp = a
        # a = b
        # b = temp

        # Python에서는 한 줄로 끝!
        a, b = b, a

        assert a == 20
        assert b == 10

    def test_unpack_from_list(self):
        """리스트의 값들을 변수에 풀어서 담기 (언패킹)"""
        # 리스트에 담긴 값들을 각각의 변수로 분리
        coordinates = [37.5665, 126.9780]  # 서울 좌표

        latitude, longitude = coordinates

        assert latitude == 37.5665
        assert longitude == 126.9780

    def test_unpack_from_tuple(self):
        """튜플 언패킹"""
        person = ("홍길동", 30, "서울")

        name, age, city = person

        assert name == "홍길동"
        assert age == 30
        assert city == "서울"


class TestPracticalUsage:
    """실무 활용 - 실제로 이렇게 씁니다"""

    def test_counter_pattern(self):
        """카운터 패턴 - 숫자 세기"""
        count = 0

        # 무언가를 셀 때
        count = count + 1  # 1 증가
        count += 1  # 위와 같음 (축약형)
        count += 1

        assert count == 3

    def test_accumulator_pattern(self):
        """누적기 패턴 - 값 모으기"""
        total = 0

        # 점수들을 더하기
        scores = [85, 90, 78, 92]
        for score in scores:
            total += score

        assert total == 345

    def test_flag_pattern(self):
        """플래그 패턴 - 상태 표시"""
        is_logged_in = False
        has_permission = False

        # 로그인 성공!
        is_logged_in = True

        # 권한 체크
        if is_logged_in:
            has_permission = True

        assert is_logged_in is True
        assert has_permission is True

    def test_temporary_variable(self):
        """임시 변수 - 계산 중간 결과 저장"""
        price = 10000
        quantity = 3

        # 중간 계산 결과를 저장하면 코드가 읽기 쉬워짐
        subtotal = price * quantity
        tax = subtotal * 0.1
        total = subtotal + tax

        assert subtotal == 30000
        assert tax == 3000
        assert total == 33000

    def test_local_variable_in_function(self):
        """함수 안에서 만든 변수는 함수 안에서만 존재 (지역 변수)"""

        def greet():
            # local_message는 함수 안에서만 존재
            local_message = "함수 안녕"
            return local_message

        result = greet()
        assert result == "함수 안녕"

        # 함수 밖에서 local_message를 쓰려고 하면 에러 발생
        # print(local_message)  # NameError!

    def test_variable_shadowing(self):
        """같은 이름의 변수가 다른 범위에 있을 수 있음 (섀도잉)"""
        message = "바깥 메시지"

        def inner():
            # 함수 안에서 새로운 message 변수 생성
            message = "안쪽 메시지"
            return message

        # 함수 안의 message와 바깥의 message는 다른 변수
        assert inner() == "안쪽 메시지"
        assert message == "바깥 메시지"

    