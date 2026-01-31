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


