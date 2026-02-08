"""
Phase 2 - 튜플(Tuple)
====================
학습 목표: 불변(immutable) 시퀀스인 튜플의 특성과 활용법 익히기

핵심 개념:
- 튜플은 한 번 만들면 수정할 수 없는 리스트라고 생각하면 됩니다
- 괄호 ()로 만들지만, 사실 쉼표(,)가 튜플을 만드는 핵심입니다
- 여러 값을 묶어서 한 번에 다루고 싶을 때, 특히 변경되면 안 되는 데이터에 사용합니다
- 함수에서 여러 값을 반환할 때 자주 사용됩니다
"""


class TestBasicConcept:
    """기본 개념 - 가장 먼저 알아야 할 것"""

    def test_create_tuple_with_parentheses(self):
        """괄호로 튜플 만들기 - 가장 흔한 방법"""
        # 괄호 안에 값들을 쉼표로 구분해서 넣으면 튜플이 됩니다
        fruits = ("apple", "banana", "cherry")

        assert fruits == ("apple", "banana", "cherry")
        assert type(fruits) == tuple

    def test_create_tuple_without_parentheses(self):
        """괄호 없이 튜플 만들기 - 쉼표가 핵심!"""
        # 사실 튜플을 만드는 건 괄호가 아니라 쉼표입니다
        # 괄호 없이 쉼표로만 나열해도 튜플이 됩니다
        numbers = 1, 2, 3

        assert numbers == (1, 2, 3)
        assert type(numbers) == tuple

    def test_single_element_tuple_gotcha(self):
        """원소가 하나인 튜플 - 쉼표를 꼭 붙여야 합니다!"""
        # 괄호만 있으면 그냥 값입니다 (튜플이 아님!)
        not_a_tuple = ("hello")
        assert type(not_a_tuple) == str  # 문자열입니다!
        assert not_a_tuple == "hello"

        # 쉼표를 붙여야 진짜 튜플이 됩니다
        real_tuple = ("hello",)  # 쉼표 주목!
        assert type(real_tuple) == tuple
        assert len(real_tuple) == 1

        # 괄호 없이도 쉼표만 있으면 튜플
        also_tuple = "hello",
        assert type(also_tuple) == tuple

    def test_empty_tuple(self):
        """빈 튜플 만들기"""
        # 방법 1: 빈 괄호
        empty1 = ()
        assert len(empty1) == 0
        assert type(empty1) == tuple

        # 방법 2: tuple() 함수
        empty2 = tuple()
        assert empty2 == ()

    def test_tuple_from_other_iterables(self):
        """다른 자료형을 튜플로 변환하기"""
        # 리스트를 튜플로
        from_list = tuple([1, 2, 3])
        assert from_list == (1, 2, 3)

        # 문자열을 튜플로 (한 글자씩 분리됨)
        from_string = tuple("abc")
        assert from_string == ("a", "b", "c")

        # range를 튜플로
        from_range = tuple(range(5))
        assert from_range == (0, 1, 2, 3, 4)

    def test_tuple_indexing(self):
        """인덱싱 - 원하는 위치의 값 가져오기"""
        colors = ("red", "green", "blue", "yellow")

        # 앞에서부터 접근 (0부터 시작)
        assert colors[0] == "red"  # 첫 번째
        assert colors[1] == "green"  # 두 번째

        # 뒤에서부터 접근 (음수 인덱스)
        assert colors[-1] == "yellow"  # 마지막
        assert colors[-2] == "blue"  # 뒤에서 두 번째

    def test_tuple_slicing(self):
        """슬라이싱 - 일부분 잘라내기"""
        numbers = (0, 1, 2, 3, 4, 5)

        # [시작:끝] - 끝은 포함 안 됨
        assert numbers[1:4] == (1, 2, 3)

        # 처음부터
        assert numbers[:3] == (0, 1, 2)

        # 끝까지
        assert numbers[3:] == (3, 4, 5)

        # 전체 복사
        assert numbers[:] == (0, 1, 2, 3, 4, 5)

        # 건너뛰기 [시작:끝:간격]
        assert numbers[::2] == (0, 2, 4)  # 2칸씩 건너뛰기

        # 역순
        assert numbers[::-1] == (5, 4, 3, 2, 1, 0)

    def test_tuple_is_immutable(self):
        """튜플은 불변(immutable) - 한 번 만들면 수정 불가!"""
        numbers = (1, 2, 3)

        # 값을 바꾸려고 하면 에러가 납니다
        import pytest

        with pytest.raises(TypeError):
            numbers[0] = 100  # TypeError: 'tuple' object does not support item assignment

        # 하지만! 튜플 안에 리스트가 있으면 그 리스트는 수정 가능
        mixed = (1, 2, [3, 4])
        mixed[2].append(5)  # 리스트 자체는 수정 가능
        assert mixed == (1, 2, [3, 4, 5])
        # 튜플이 저장하는 건 리스트의 "위치(참조)"이고,
        # 그 위치는 변하지 않았기 때문에 가능합니다

    def test_tuple_operations(self):
        """튜플 연산 - 더하기와 곱하기"""
        tuple1 = (1, 2)
        tuple2 = (3, 4)

        # 더하기: 튜플을 이어 붙임 (새로운 튜플 생성)
        combined = tuple1 + tuple2
        assert combined == (1, 2, 3, 4)

        # 곱하기: 반복 (새로운 튜플 생성)
        repeated = tuple1 * 3
        assert repeated == (1, 2, 1, 2, 1, 2)

    def test_tuple_methods(self):
        """튜플 메서드 - 딱 2개뿐입니다"""
        numbers = (1, 2, 3, 2, 2, 4)

        # count(): 특정 값이 몇 개 있는지
        assert numbers.count(2) == 3  # 2가 3개 있음

        # index(): 특정 값의 위치 (처음 나오는 위치)
        assert numbers.index(2) == 1  # 2가 처음 나오는 인덱스는 1

        # 그 외에는 메서드가 없습니다!
        # 불변이니까 추가/삭제/정렬 메서드가 필요 없겠죠?

    def test_membership_and_length(self):
        """포함 여부 확인과 길이"""
        fruits = ("apple", "banana", "cherry")

        # in: 포함 여부
        assert "banana" in fruits
        assert "grape" not in fruits

        # len(): 길이
        assert len(fruits) == 3


