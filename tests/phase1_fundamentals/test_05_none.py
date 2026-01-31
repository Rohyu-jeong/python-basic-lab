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


