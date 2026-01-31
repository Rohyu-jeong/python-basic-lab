"""
Phase 1 - None 타입
===================
학습 목표: Python의 "없음"을 나타내는 None 이해하기

핵심 개념:
- None은 Python에서 "값이 없음"을 나타내는 특별한 값
- None은 타입이 NoneType인 유일한 값 (싱글톤)
- None 체크는 == 대신 is를 사용하는 것이 관례
- 함수가 명시적으로 return하지 않으면 None을 반환
"""


class TestBasicConcept:
    """기본 개념 - None이 뭔가요?"""

    def test_none_is_nothing(self):
        """None은 '아무것도 없음'을 나타내는 특별한 값입니다"""
        # 다른 언어의 null, nil과 비슷한 개념
        value = None

        # None은 그 자체로 하나의 값입니다
        assert value is None

    def test_none_type(self):
        """None의 타입은 NoneType입니다"""
        value = None

        # type()으로 타입을 확인할 수 있습니다
        assert type(value).__name__ == "NoneType"

        # None은 NoneType의 유일한 인스턴스입니다
        assert isinstance(value, type(None))

    def test_none_is_singleton(self):
        """None은 싱글톤입니다 - 프로그램에서 딱 하나만 존재"""
        a = None
        b = None

        # 모든 None은 같은 객체를 가리킵니다
        # id()는 객체의 메모리 주소를 반환합니다
        assert id(a) == id(b)

        # is 연산자로 같은 객체인지 확인
        assert a is b

    def test_none_is_falsy(self):
        """None은 불리언 문맥에서 False로 평가됩니다"""
        value = None

        # bool()로 변환하면 False
        assert bool(value) is False

        # if 문에서 False처럼 동작
        if value:
            result = "truthy"
        else:
            result = "falsy"

        assert result == "falsy"


class TestPracticalUsage:
    """실무 활용 - None은 이렇게 씁니다"""

    def test_function_returns_none(self):
        """return이 없는 함수는 자동으로 None을 반환합니다"""

        def say_hello(name):
            print(f"Hello, {name}!")  # print는 출력만 하고 값을 반환하지 않음
            # return이 없음!

        result = say_hello("Python")

        # 명시적 return이 없으면 None 반환
        assert result is None

    def test_explicit_return_none(self):
        """명시적으로 None을 반환할 수도 있습니다"""

        def find_user(user_id):
            users = {1: "Alice", 2: "Bob"}

            if user_id in users:
                return users[user_id]
            else:
                return None  # 못 찾으면 None 반환

        assert find_user(1) == "Alice"
        assert find_user(999) is None  # 없는 사용자

    def test_none_as_default_parameter(self):
        """함수의 기본값으로 None을 자주 사용합니다"""

        # 왜 None을 기본값으로 쓸까요?
        # 리스트 같은 가변 객체를 기본값으로 쓰면 문제가 생길 수 있기 때문!

        def add_item(item, items=None):
            if items is None:
                items = []  # 매 호출마다 새 리스트 생성
            items.append(item)
            return items

        result1 = add_item("사과")
        result2 = add_item("바나나")

        # 각각 독립적인 리스트
        assert result1 == ["사과"]
        assert result2 == ["바나나"]

    def test_none_for_optional_values(self):
        """선택적 값을 표현할 때 None을 사용합니다"""

        class User:
            def __init__(self, name, email=None):
                self.name = name
                self.email = email  # 이메일은 선택사항

        user1 = User("Alice", "alice@example.com")
        user2 = User("Bob")  # 이메일 없이 생성

        assert user1.email == "alice@example.com"
        assert user2.email is None

    def test_none_in_data_structures(self):
        """컬렉션에서 None을 값으로 사용할 수 있습니다"""
        # 리스트에 None 포함
        scores = [85, None, 90, None, 78]  # None은 "점수 없음"

        # None이 아닌 점수만 필터링
        valid_scores = [s for s in scores if s is not None]
        assert valid_scores == [85, 90, 78]

        # 딕셔너리에서 None 값
        config = {
            "host": "localhost",
            "port": 8080,
            "timeout": None  # 설정되지 않음
        }
        assert config["timeout"] is None


class TestEdgeCases:
    """주의사항 - None 다룰 때 조심할 것들"""

    def test_is_vs_equality(self):
        """None 비교는 == 대신 is를 사용하세요"""
        value = None

        # 둘 다 동작하지만...
        assert value == None  # 동작은 하지만 권장하지 않음
        assert value is None  # 이것이 파이썬 관례!

        # 왜 is를 쓸까요?
        # 1. None은 싱글톤이므로 is가 의미적으로 정확
        # 2. __eq__를 오버라이드한 객체에서 == 는 예상과 다를 수 있음
        # 3. is가 더 빠름

    def test_none_is_not_zero(self):
        """None은 0이 아닙니다"""
        zero = 0
        nothing = None

        # 둘 다 falsy하지만 같지 않습니다
        assert bool(zero) is False
        assert bool(nothing) is False

        # 하지만 서로 다릅니다!
        assert zero != nothing
        assert zero is not nothing

    def test_none_is_not_empty_string(self):
        """None은 빈 문자열이 아닙니다"""
        empty = ""
        nothing = None

        # 둘 다 falsy하지만
        assert bool(empty) is False
        assert bool(nothing) is False

        # 서로 다릅니다!
        assert empty != nothing
        assert empty is not nothing

    def test_none_is_not_empty_list(self):
        """None은 빈 리스트가 아닙니다"""
        empty_list = []
        nothing = None

        assert bool(empty_list) is False
        assert bool(nothing) is False

        # 서로 다릅니다!
        assert empty_list != nothing
        assert empty_list is not nothing

    def test_none_attribute_error(self):
        """None에 메서드를 호출하면 에러가 발생합니다"""
        value = None

        # None에는 일반 객체의 메서드가 없습니다
        try:
            value.upper()  # 문자열 메서드를 None에 호출
        except AttributeError as e:
            # "'NoneType' object has no attribute 'upper'"
            assert "NoneType" in str(e)

    def test_check_before_use(self):
        """None일 수 있는 값은 사용 전에 체크하세요"""

        def get_username(user_dict):
            # user_dict이 None일 수 있다면?
            if user_dict is None:
                return "Anonymous"
            return user_dict.get("name", "Unknown")

        assert get_username({"name": "Alice"}) == "Alice"
        assert get_username(None) == "Anonymous"
        assert get_username({}) == "Unknown"


class TestTips:
    """꿀팁 - None 활용 노하우"""

    def test_or_operator_with_none(self):
        """or 연산자로 None 대신 기본값 사용하기"""
        username = None

        # None이면 기본값 사용
        display_name = username or "Guest"
        assert display_name == "Guest"

        # 값이 있으면 그 값 사용
        username = "Alice"
        display_name = username or "Guest"
        assert display_name == "Alice"

        # 주의: 0이나 빈 문자열도 기본값으로 대체됨
        count = 0
        result = count or 10  # 0도 falsy라서 10이 됨
        assert result == 10

    def test_none_coalescing_pattern(self):
        """None일 때만 기본값을 쓰고 싶다면"""
        # or는 0, "", [] 등도 대체해버림
        # None만 대체하고 싶을 때는 이렇게:

        value = 0
        result = value if value is not None else 10
        assert result == 0  # 0은 유지됨

        value = None
        result = value if value is not None else 10
        assert result == 10  # None만 대체됨

    def test_getattr_with_none_default(self):
        """getattr로 안전하게 속성 접근하기"""

        class User:
            def __init__(self):
                self.name = "Alice"
                # email 속성은 없음

        user = User()

        # 없는 속성에 접근하면 에러 대신 None 반환
        email = getattr(user, "email", None)
        assert email is None

        # 있는 속성은 정상 접근
        name = getattr(user, "name", None)
        assert name == "Alice"

    def test_dict_get_returns_none(self):
        """딕셔너리의 get()은 키가 없으면 None을 반환합니다"""
        data = {"name": "Alice", "age": 25}

        # 대괄호 접근: 키가 없으면 KeyError
        # data["email"]  # KeyError 발생!

        # get() 접근: 키가 없으면 None (또는 지정한 기본값)
        email = data.get("email")
        assert email is None

        # 기본값 지정 가능
        email = data.get("email", "not provided")
        assert email == "not provided"

    def test_filter_none_values(self):
        """None 값 필터링하는 여러 방법"""
        data = [1, None, 2, None, 3, None]

        # 방법 1: 리스트 컴프리헨션
        filtered1 = [x for x in data if x is not None]
        assert filtered1 == [1, 2, 3]

        # 방법 2: filter 함수 (None을 필터로 쓰면 falsy 제거)
        filtered2 = list(filter(None, data))
        assert filtered2 == [1, 2, 3]

        # ⚠️ 방법 2는 0도 제거하니 주의!
        data_with_zero = [1, None, 0, None, 3]
        filtered3 = list(filter(None, data_with_zero))
        assert filtered3 == [1, 3]  # 0도 사라짐!

        # None만 제거하려면 방법 1 사용
        filtered4 = [x for x in data_with_zero if x is not None]
        assert filtered4 == [1, 0, 3]  # 0은 유지

    def test_none_safe_chain(self):
        """중첩된 None 체크 패턴"""
        # 데이터가 여러 겹으로 중첩된 경우
        response = {
            "data": {
                "user": {
                    "profile": {
                        "email": "alice@example.com"
                    }
                }
            }
        }

        # 안전하게 깊은 값 접근하기
        def safe_get(data, *keys):
            for key in keys:
                if data is None:
                    return None
                data = data.get(key) if isinstance(data, dict) else None
            return data

        email = safe_get(response, "data", "user", "profile", "email")
        assert email == "alice@example.com"

        # 중간에 없는 키가 있어도 에러 없이 None 반환
        missing = safe_get(response, "data", "user", "settings", "theme")
        assert missing is None
