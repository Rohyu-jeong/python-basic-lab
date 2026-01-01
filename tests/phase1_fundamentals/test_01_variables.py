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

    def test_valid_variable_names(self):
        """올바른 변수 이름 예시"""
        # 소문자와 언더스코어 (snake_case) - Python 권장 스타일
        user_name = "홍길동"
        total_count = 100
        is_valid = True

        # 숫자를 포함할 수 있음 (단, 시작은 안 됨)
        player1_score = 95
        item2 = "검"

        # 대문자도 가능 (보통 클래스 이름에 사용)
        MyVariable = "OK"

        # 언더스코어로 시작 (관례상 내부용)
        _private = "internal"

        # 한글도 가능 (하지만 권장하지 않음)
        이름 = "김파이썬"

        assert user_name == "홍길동"
        assert player1_score == 95
        assert 이름 == "김파이썬"
        assert _private == "internal"

    def test_naming_conventions(self):
        """Python 커뮤니티의 이름 짓기 관례 (PEP 8)"""
        # 변수와 함수: snake_case (소문자 + 언더스코어)
        my_variable = 1
        user_age = 25

        # 상수: SCREAMING_SNAKE_CASE (대문자 + 언더스코어)
        MAX_SIZE = 100
        PI = 3.14159

        # 클래스: PascalCase (단어 첫 글자마다 대문자)
        # MyClass, UserProfile (이건 클래스 챕터에서 배움)

        assert my_variable == 1
        assert MAX_SIZE == 100

    def test_meaningful_names(self):
        """의미 있는 이름을 사용하세요"""
        # 나쁜 예 - 무슨 뜻인지 모름
        x = 5
        t = 1000

        # 좋은 예 - 이름만 봐도 무엇인지 알 수 있음
        num_students = 5
        timeout_milliseconds = 1000

        # 테스트는 통과하지만, 좋은 이름이 코드 이해에 도움됨
        assert x == num_students
        assert t == timeout_milliseconds


class TestEdgeCases:
    """주의사항 - 자주 하는 실수와 함정"""

    def test_case_sensitive(self):
        """변수 이름은 대소문자를 구분합니다!"""
        name = "소문자"
        Name = "첫글자대문자"
        NAME = "전부대문자"

        # 모두 다른 변수임!
        assert name != Name
        assert Name != NAME
        assert name != NAME

    def test_cannot_start_with_number(self):
        """변수 이름은 숫자로 시작할 수 없습니다"""
        # 이렇게 하면 에러:
        # 1st_place = "금메달"  # SyntaxError!

        # 대신 이렇게:
        first_place = "금메달"
        place_1st = "금메달"

        assert first_place == "금메달"
        assert place_1st == "금메달"

    def test_invalid_variable_names(self):
        """사용할 수 없는 변수 이름들"""
        # 아래는 모두 SyntaxError:
        # 1player = "NO"      # 숫자로 시작 불가
        # user-name = "NO"    # 하이픈(-) 불가
        # user name = "NO"    # 공백 불가
        # class = "NO"        # 예약어 불가

        # 올바른 대안:
        player1 = "OK"
        user_name = "OK"
        klass = "OK"  # class 대신 klass 사용하기도 함

        assert player1 == "OK"
        assert user_name == "OK"

    def test_reserved_keywords(self):
        """예약어는 변수 이름으로 사용할 수 없습니다"""
        import keyword

        # Python 예약어 목록 확인
        reserved = keyword.kwlist

        # 이런 단어들은 변수 이름으로 못 씀
        assert "if" in reserved
        assert "for" in reserved
        assert "while" in reserved
        assert "class" in reserved
        assert "def" in reserved
        assert "return" in reserved
        assert "True" in reserved
        assert "False" in reserved
        assert "None" in reserved
        assert "and" in reserved
        assert "or" in reserved
        assert "not" in reserved

        # 예: if = 10  # SyntaxError!

    def test_avoid_builtin_names(self):
        """내장 함수 이름을 변수로 쓰지 마세요 (에러는 안 나지만 위험!)"""
        # 이렇게 하면 안 됨 (에러는 안 나지만 내장 함수를 덮어씀)
        # list = [1, 2, 3]  # 이제 list() 함수를 못 씀!
        # print = "hello"   # 이제 print() 함수를 못 씀!
        # str = "text"      # 이제 str() 함수를 못 씀!
        # id = 123          # 이제 id() 함수를 못 씀!

        # 대신 이렇게:
        my_list = [1, 2, 3]
        message = "hello"
        text = "text"
        user_id = 123

        assert my_list == [1, 2, 3]
        assert message == "hello"

    def test_undefined_variable(self):
        """정의하지 않은 변수를 사용하면 NameError"""
        import pytest

        # undefined_var라는 변수는 만든 적 없음
        with pytest.raises(NameError):
            # 이 줄에서 NameError 발생
            _ = undefined_var  # noqa: F821

    def test_assignment_vs_comparison(self):
        """= (할당)과 == (비교)를 혼동하지 마세요"""
        x = 10  # 할당: x에 10을 넣음

        # x == 10은 비교: x가 10인지 확인 (True/False 반환)
        assert (x == 10) is True
        assert (x == 5) is False

        # 조건문에서 =를 쓰면 에러!
        # if x = 10:  # SyntaxError!

        # 올바른 방법:
        if x == 10:
            result = "correct"
        assert result == "correct"

    def test_mutable_default_trap(self):
        """가변 객체를 여러 변수에 할당할 때 주의"""
        # 같은 리스트를 가리킴
        a = b = [1, 2, 3]

        # a를 수정하면 b도 바뀜!
        a.append(4)

        assert a == [1, 2, 3, 4]
        assert b == [1, 2, 3, 4]  # b도 바뀌어 버림!
        assert a is b  # 같은 객체를 가리키고 있음

        # 독립적인 리스트를 원하면:
        c = [1, 2, 3]
        d = [1, 2, 3]  # 따로 생성

        c.append(4)
        assert c == [1, 2, 3, 4]
        assert d == [1, 2, 3]  # d는 영향 없음

    def test_none_assignment(self):
        """None은 '값이 없음'을 나타내는 특별한 값"""
        # 변수를 선언만 하고 나중에 값을 넣고 싶을 때
        result = None

        assert result is None
        assert result == None  # 동작하지만 is None이 권장됨

        # 나중에 값 할당
        result = "완료"
        assert result is not None


class TestTips:
    """꿀팁 - 알아두면 유용한 것들"""

    def test_underscore_for_unused(self):
        """사용하지 않는 값은 언더스코어(_)로 표시"""
        # 좌표에서 x만 필요하고 y는 필요 없을 때
        coordinates = (100, 200)

        x, _ = coordinates  # _는 "이 값은 안 쓸 거예요"라는 표시

        assert x == 100

    def test_multiple_underscore(self):
        """*_로 여러 값을 한 번에 무시"""
        data = (1, 2, 3, 4, 5)

        first, *_, last = data  # 처음과 마지막만 필요

        assert first == 1
        assert last == 5

    def test_star_for_rest(self):
        """*로 나머지 값들을 리스트로 모으기"""
        numbers = [1, 2, 3, 4, 5]

        first, *rest = numbers
        assert first == 1
        assert rest == [2, 3, 4, 5]

        first, *middle, last = numbers
        assert first == 1
        assert middle == [2, 3, 4]
        assert last == 5

        *beginning, last = numbers
        assert beginning == [1, 2, 3, 4]
        assert last == 5

    def test_augmented_assignment(self):
        """복합 할당 연산자 - 코드를 짧게"""
        x = 10

        x += 5  # x = x + 5와 같음
        assert x == 15

        x -= 3  # x = x - 3과 같음
        assert x == 12

        x *= 2  # x = x * 2와 같음
        assert x == 24

        x //= 4  # x = x // 4와 같음 (정수 나눗셈)
        assert x == 6

        x **= 2  # x = x ** 2와 같음 (거듭제곱)
        assert x == 36

        x %= 10  # x = x % 10과 같음 (나머지)
        assert x == 6

    def test_chained_comparison(self):
        """연속 비교 - Python만의 편리한 문법"""
        age = 25

        # 다른 언어에서는: age >= 20 and age < 30
        # Python에서는 수학처럼 쓸 수 있음!
        is_in_twenties = 20 <= age < 30

        assert is_in_twenties is True

        # 여러 개도 가능
        x = 5
        assert 1 < x < 10 < 100
        assert 0 <= x <= 10

    def test_id_function(self):
        """id() - 변수가 가리키는 메모리 주소(고유 번호) 확인"""
        a = [1, 2, 3]
        b = a  # b는 a와 같은 리스트를 가리킴
        c = [1, 2, 3]  # c는 새로운 리스트

        # a와 b는 같은 객체를 가리킴
        assert id(a) == id(b)

        # c는 값은 같지만 다른 객체
        assert a == c  # 값은 같음
        assert id(a) != id(c)  # 하지만 다른 객체

        # is 연산자로도 같은 객체인지 확인 가능
        assert a is b
        assert a is not c

    def test_small_integer_caching(self):
        """Python은 작은 정수(-5~256)를 캐싱합니다"""
        # 작은 정수는 같은 객체를 재사용
        a = 100
        b = 100
        assert a is b  # 같은 객체!

        # 큰 정수는 새로 생성될 수 있음
        x = 1000
        y = 1000
        # x is y는 True일 수도 False일 수도 있음 (구현에 따라 다름)
        # 하지만 값 비교는 항상 True
        assert x == y

    def test_variable_deletion(self):
        """del로 변수 삭제하기"""
        import pytest

        x = 10
        assert x == 10

        del x  # 변수 삭제

        # 삭제 후 접근하면 NameError
        with pytest.raises(NameError):
            _ = x  # noqa: F821

    def test_multiple_return_unpacking(self):
        """함수의 여러 반환값을 언패킹"""

        def get_user_info():
            return "홍길동", 30, "서울"

        # 함수 반환값을 바로 언패킹
        name, age, city = get_user_info()

        assert name == "홍길동"
        assert age == 30
        assert city == "서울"

    def test_enumerate_unpacking(self):
        """enumerate와 함께 언패킹 (반복문에서 자주 사용)"""
        fruits = ["사과", "바나나", "체리"]

        result = []
        for index, fruit in enumerate(fruits):
            result.append(f"{index}: {fruit}")

        assert result == ["0: 사과", "1: 바나나", "2: 체리"]

    def test_dict_items_unpacking(self):
        """딕셔너리 items()와 함께 언패킹"""
        scores = {"국어": 90, "영어": 85, "수학": 95}

        result = []
        for subject, score in scores.items():
            result.append(f"{subject}: {score}점")

        assert "국어: 90점" in result
        assert "영어: 85점" in result
        assert "수학: 95점" in result
