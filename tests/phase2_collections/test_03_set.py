"""
Phase 2 - Set (집합)
====================
학습 목표: 파이썬의 집합(set) 자료형을 완벽히 이해하고 활용하기

핵심 개념:
- set은 '중복을 허용하지 않는' 데이터 모음입니다
- 순서가 없어서 인덱싱이 불가능합니다
- 수학의 집합 연산(합집합, 교집합 등)을 지원합니다
- 해시 가능한(hashable) 요소만 담을 수 있습니다
"""
import pytest


class TestBasicConcept:
    """기본 개념 - 가장 먼저 알아야 할 것들"""

    def test_create_set_with_braces(self):
        """중괄호로 set 만들기"""
        # 중괄호 {}와 쉼표로 set을 만듭니다
        fruits = {"apple", "banana", "cherry"}

        assert isinstance(fruits, set)
        assert len(fruits) == 3

    def test_create_set_with_constructor(self):
        """set() 생성자로 만들기"""
        # 리스트, 문자열 등을 set으로 변환할 수 있습니다
        from_list = set([1, 2, 3])
        from_string = set("hello")  # 문자 하나하나가 요소가 됩니다

        assert from_list == {1, 2, 3}
        # "hello"에서 'l'이 2번 나오지만 set에서는 한 번만!
        assert from_string == {"h", "e", "l", "o"}

    def test_empty_set_gotcha(self):
        """빈 set 만들기 - 주의! {}는 빈 딕셔너리입니다"""
        # 이것은 빈 딕셔너리입니다, 빈 set이 아닙니다!
        empty_dict = {}
        assert type(empty_dict) == dict

        # 빈 set은 반드시 set()으로 만들어야 합니다
        empty_set = set()
        assert type(empty_set) == set
        assert len(empty_set) == 0

    def test_set_removes_duplicates_automatically(self):
        """set은 중복을 자동으로 제거합니다"""
        # 같은 값을 여러 번 넣어도 하나만 남습니다
        numbers = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}

        assert numbers == {1, 2, 3, 4}
        assert len(numbers) == 4

    def test_set_has_no_order(self):
        """set은 순서가 없습니다"""
        colors = {"red", "green", "blue"}

        # 인덱싱 불가능! colors[0] 하면 에러납니다
        with pytest.raises(TypeError):
            colors[0]  # noqa: B018 - 의도적으로 에러 발생시키는 코드

        # 순서가 없으므로 '몇 번째' 개념이 없습니다
        # 대신 '포함 여부'를 확인합니다
        assert "red" in colors

    def test_membership_check_is_fast(self):
        """set의 포함 여부 확인은 매우 빠릅니다"""
        # set은 해시 테이블을 사용해서 O(1) 시간에 검색합니다
        # 리스트는 O(n) - 요소가 많을수록 느려집니다
        large_set = set(range(10000))
        large_list = list(range(10000))

        # 둘 다 같은 결과지만, set이 훨씬 빠릅니다
        assert 9999 in large_set
        assert 9999 in large_list

    def test_hashable_elements_only(self):
        """set에는 해시 가능한 요소만 넣을 수 있습니다"""
        # 해시 가능 = 변하지 않는(immutable) 것들
        # 숫자, 문자열, 튜플은 OK
        valid_set = {1, "hello", (1, 2, 3)}
        assert len(valid_set) == 3

        # 리스트는 변할 수 있어서 넣을 수 없습니다
        with pytest.raises(TypeError):
            invalid_set = {[1, 2, 3]}  # noqa: F841

    def test_frozenset_is_immutable_set(self):
        """frozenset은 변경 불가능한 set입니다"""
        # frozenset은 한번 만들면 수정할 수 없습니다
        frozen = frozenset([1, 2, 3])

        # 추가/삭제 불가능
        with pytest.raises(AttributeError):
            frozen.add(4)

        # frozenset은 해시 가능해서 set의 요소가 될 수 있습니다!
        set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
        assert len(set_of_sets) == 2


