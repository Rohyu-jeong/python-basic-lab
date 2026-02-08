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


class TestEdgeCases:
    """주의사항 - 자주 하는 실수와 함정"""

    def test_accidental_tuple_creation(self):
        """실수: 의도치 않게 튜플 만들기"""
        # 쉼표를 실수로 넣으면 튜플이 됩니다

        # 이런 실수를 할 수 있어요
        number = 100,  # 쉼표가 들어감!
        assert type(number) == tuple

        # 특히 여러 줄에 걸쳐 작성할 때 주의
        value = (
            "hello"  # 쉼표 없으면 문자열
        )
        assert type(value) == str

        value_tuple = (
            "hello",  # 쉼표 있으면 튜플
        )
        assert type(value_tuple) == tuple

    def test_unpacking_count_mismatch(self):
        """실수: 언패킹할 때 개수가 안 맞음"""
        point = (10, 20, 30)

        # 변수 개수가 맞아야 합니다
        import pytest

        # 너무 적은 변수
        with pytest.raises(ValueError):
            x, y = point  # ValueError: too many values to unpack

        # 너무 많은 변수
        with pytest.raises(ValueError):
            a, b, c, d = point  # ValueError: not enough values to unpack

        # 올바른 방법
        x, y, z = point
        assert (x, y, z) == (10, 20, 30)

    def test_tuple_inside_tuple(self):
        """중첩 튜플 다루기"""
        # 튜플 안에 튜플이 있을 수 있습니다
        nested = ((1, 2), (3, 4), (5, 6))

        # 인덱스를 연속으로 사용
        assert nested[0] == (1, 2)
        assert nested[0][0] == 1
        assert nested[1][1] == 4

        # 중첩 언패킹
        (a, b), (c, d), (e, f) = nested
        assert a == 1
        assert d == 4

    def test_comparing_tuples(self):
        """튜플 비교 - 앞에서부터 순서대로 비교"""
        # 튜플은 앞에서부터 순서대로 비교합니다
        assert (1, 2, 3) < (1, 2, 4)  # 세 번째 원소에서 결정
        assert (1, 2) < (1, 2, 0)  # 길이가 짧은 게 더 작음
        assert (2, 0) > (1, 9, 9, 9)  # 첫 번째 원소에서 이미 결정

        # 이 성질을 이용한 정렬
        students = [("Kim", 85), ("Lee", 90), ("Park", 85)]
        # 점수로 정렬, 점수 같으면 이름으로 정렬
        sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
        # -x[1]로 점수 내림차순, x[0]으로 이름 오름차순
        assert sorted_students[0] == ("Lee", 90)  # 최고점
        assert sorted_students[1] == ("Kim", 85)  # 같은 점수면 이름순

    def test_tuple_not_always_hashable(self):
        """함정: 튜플이라고 항상 딕셔너리 키로 쓸 수 있는 건 아닙니다"""
        # 튜플 안에 리스트가 있으면 해시 불가능!
        import pytest

        # 순수 튜플은 딕셔너리 키로 사용 가능
        pure_tuple = (1, 2, 3)
        valid_dict = {pure_tuple: "works"}
        assert valid_dict[(1, 2, 3)] == "works"

        # 리스트를 포함한 튜플은 안 됨!
        mixed_tuple = (1, [2, 3])
        with pytest.raises(TypeError):
            bad_dict = {mixed_tuple: "fails"}  # unhashable type: 'list'


class TestTips:
    """꿀팁 - 알아두면 유용한 것들"""

    def test_named_tuple_basic(self):
        """네임드 튜플 - 인덱스 대신 이름으로 접근"""
        from collections import namedtuple

        # 튜플인데 이름으로 접근할 수 있어서 더 읽기 좋습니다
        Point = namedtuple("Point", ["x", "y"])

        p = Point(10, 20)

        # 이름으로 접근 (더 읽기 좋음!)
        assert p.x == 10
        assert p.y == 20

        # 인덱스로도 접근 가능
        assert p[0] == 10
        assert p[1] == 20

        # 여전히 튜플입니다
        assert isinstance(p, tuple)

    def test_named_tuple_practical(self):
        """네임드 튜플 실용 예제"""
        from collections import namedtuple

        # 학생 정보를 담는 구조
        Student = namedtuple("Student", ["name", "grade", "score"])

        students = [
            Student("김철수", 3, 85),
            Student("이영희", 2, 92),
            Student("박민수", 3, 78),
        ]

        # 이름으로 접근하니 코드가 읽기 좋음
        top_student = max(students, key=lambda s: s.score)
        assert top_student.name == "이영희"
        assert top_student.score == 92

        # 언패킹도 됨
        name, grade, score = top_student
        assert name == "이영희"

    def test_tuple_vs_list_performance(self):
        """튜플 vs 리스트 성능 - 튜플이 더 가볍습니다"""
        import sys

        # 같은 데이터인데 튜플이 메모리를 덜 씁니다
        tuple_data = (1, 2, 3, 4, 5)
        list_data = [1, 2, 3, 4, 5]

        tuple_size = sys.getsizeof(tuple_data)
        list_size = sys.getsizeof(list_data)

        # 리스트가 더 큽니다 (추가/삭제를 위한 여유 공간 때문)
        assert tuple_size < list_size

    def test_when_to_use_tuple(self):
        """언제 튜플을 쓸까요?"""
        # 1. 변경되면 안 되는 상수 데이터
        DAYS_OF_WEEK = ("월", "화", "수", "목", "금", "토", "일")
        HTTP_STATUS = (200, 201, 204, 400, 401, 403, 404, 500)

        # 2. 의미 있는 순서가 있는 짧은 데이터 묶음
        rgb_red = (255, 0, 0)
        coordinate = (37.5665, 126.9780)  # 위도, 경도

        # 3. 데이터베이스 쿼리 결과처럼 읽기 전용 레코드
        db_row = ("user_001", "홍길동", "hong@email.com")

        assert DAYS_OF_WEEK[0] == "월"
        assert 404 in HTTP_STATUS
        assert rgb_red[0] == 255

    def test_tuple_unpacking_in_comprehension(self):
        """컴프리헨션에서 언패킹 활용"""
        pairs = [(1, "a"), (2, "b"), (3, "c")]

        # 각 튜플에서 숫자만 추출
        numbers = [num for num, letter in pairs]
        assert numbers == [1, 2, 3]

        # 문자만 추출해서 대문자로
        letters = [letter.upper() for num, letter in pairs]
        assert letters == ["A", "B", "C"]

        # 딕셔너리로 변환
        mapping = {letter: num for num, letter in pairs}
        assert mapping == {"a": 1, "b": 2, "c": 3}

    def test_underscore_for_unused_values(self):
        """언더스코어로 불필요한 값 무시하기"""
        data = ("Kim", 25, "Seoul", "Engineer")

        # 이름과 직업만 필요할 때
        name, _, _, job = data  # 언더스코어는 "이 값은 안 씀"을 의미
        assert name == "Kim"
        assert job == "Engineer"

        # 첫 번째만 필요할 때
        first, *_ = data  # 나머지 전부 무시
        assert first == "Kim"

    def test_tuple_to_list_and_back(self):
        """튜플 수정이 필요할 때 - 리스트로 변환 후 다시 튜플로"""
        original = (1, 2, 3, 4, 5)

        # 튜플은 수정 불가하므로 리스트로 변환
        temp_list = list(original)
        temp_list[2] = 99  # 수정
        temp_list.append(6)  # 추가

        # 다시 튜플로
        modified = tuple(temp_list)
        assert modified == (1, 2, 99, 4, 5, 6)

        # 원본은 그대로
        assert original == (1, 2, 3, 4, 5)
