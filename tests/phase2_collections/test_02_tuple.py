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


class TestPracticalUsage:
    """실무 활용 - 실제로 이렇게 씁니다"""

    def test_tuple_unpacking_basic(self):
        """튜플 언패킹 기본 - 여러 변수에 한 번에 할당"""
        # 튜플의 각 값을 개별 변수로 꺼내는 것을 "언패킹"이라고 합니다
        coordinates = (10, 20)
        x, y = coordinates  # 한 줄로 두 변수에 할당!

        assert x == 10
        assert y == 20

        # 직접 언패킹도 가능
        a, b, c = 1, 2, 3
        assert a == 1
        assert b == 2
        assert c == 3

    def test_swap_values_with_tuple(self):
        """변수 값 교환 - 파이썬의 우아한 방법"""
        a = 10
        b = 20

        # 다른 언어에서는 임시 변수가 필요하지만
        # 파이썬에서는 튜플 언패킹으로 한 줄에 끝!
        a, b = b, a

        assert a == 20
        assert b == 10

    def test_function_return_multiple_values(self):
        """함수에서 여러 값 반환하기 - 튜플의 가장 흔한 용도"""

        def get_min_max(numbers):
            """최솟값과 최댓값을 동시에 반환"""
            return min(numbers), max(numbers)  # 튜플로 반환됨

        data = [5, 2, 9, 1, 7]
        minimum, maximum = get_min_max(data)  # 언패킹으로 받기

        assert minimum == 1
        assert maximum == 9

        # 튜플 그대로 받을 수도 있음
        result = get_min_max(data)
        assert result == (1, 9)
        assert type(result) == tuple

    def test_unpacking_with_star(self):
        """* 를 사용한 확장 언패킹 - 나머지를 리스트로 받기"""
        numbers = (1, 2, 3, 4, 5)

        # 첫 번째와 나머지
        first, *rest = numbers
        assert first == 1
        assert rest == [2, 3, 4, 5]  # 나머지는 리스트가 됨!

        # 처음, 중간, 마지막
        head, *middle, tail = numbers
        assert head == 1
        assert middle == [2, 3, 4]
        assert tail == 5

        # 마지막만 따로
        *others, last = numbers
        assert others == [1, 2, 3, 4]
        assert last == 5

    def test_unpacking_in_for_loop(self):
        """for 문에서 언패킹 활용"""
        # 좌표 리스트를 순회할 때
        points = [(0, 0), (1, 2), (3, 4)]

        distances_from_origin = []
        for x, y in points:  # 각 튜플을 x, y로 언패킹
            distance = (x**2 + y**2) ** 0.5  # 원점으로부터 거리
            distances_from_origin.append(distance)

        assert distances_from_origin[0] == 0.0
        assert distances_from_origin[1] == (1 + 4) ** 0.5

    def test_tuple_with_enumerate(self):
        """enumerate와 함께 사용 - 인덱스와 값을 동시에"""
        fruits = ("apple", "banana", "cherry")

        result = []
        for index, fruit in enumerate(fruits):  # (인덱스, 값) 튜플을 언패킹
            result.append(f"{index}: {fruit}")

        assert result == ["0: apple", "1: banana", "2: cherry"]

    def test_tuple_with_zip(self):
        """zip과 함께 사용 - 여러 시퀀스를 동시에 순회"""
        names = ("Alice", "Bob", "Charlie")
        ages = (25, 30, 35)
        cities = ("Seoul", "Busan", "Daegu")

        people = []
        for name, age, city in zip(names, ages, cities):
            people.append(f"{name}({age}) from {city}")

        assert people[0] == "Alice(25) from Seoul"
        assert people[1] == "Bob(30) from Busan"

    def test_tuple_as_dict_key(self):
        """딕셔너리 키로 사용 - 리스트는 안 되지만 튜플은 됩니다"""
        # 튜플은 불변이므로 딕셔너리 키로 사용 가능!
        # 좌표를 키로 사용하는 예시
        grid = {}
        grid[(0, 0)] = "origin"
        grid[(1, 0)] = "right"
        grid[(0, 1)] = "up"

        assert grid[(0, 0)] == "origin"
        assert grid[(1, 0)] == "right"

        # 리스트는 키로 사용 불가 (unhashable)
        import pytest

        with pytest.raises(TypeError):
            bad_dict = {[0, 0]: "this will fail"}

    def test_tuple_for_grouping_data(self):
        """데이터 그룹화 - 관련 있는 값들을 묶어두기"""
        # RGB 색상을 튜플로 표현
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)

        # 함수에서 활용
        def is_pure_color(rgb):
            """순색인지 확인 (RGB 중 하나만 255)"""
            r, g, b = rgb
            return (r == 255 or g == 255 or b == 255) and rgb.count(0) == 2

        assert is_pure_color(red) is True
        assert is_pure_color(green) is True
        assert is_pure_color((128, 128, 128)) is False  # 회색은 순색 아님


