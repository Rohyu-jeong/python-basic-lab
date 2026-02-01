"""
Phase 2 - 리스트 (List)
=======================
학습 목표: 파이썬에서 가장 많이 쓰이는 자료구조인 리스트를 완벽히 이해하기

핵심 개념:
- 리스트는 여러 값을 순서대로 담는 "상자"입니다
- 대괄호 []로 만들고, 쉼표로 값을 구분합니다
- 순서가 있어서 몇 번째인지(인덱스)로 값을 꺼낼 수 있습니다
- 값을 추가, 삭제, 변경할 수 있습니다 (가변적 = mutable)
"""

import pytest


class TestBasicConcept:
    """기본 개념 - 리스트 생성, 인덱싱, 슬라이싱, 수정"""

    # === 리스트 생성 ===

    def test_create_empty_list(self):
        """빈 리스트 만들기 - 아무것도 없는 서랍장 준비"""
        # 방법 1: 대괄호 사용 (가장 일반적)
        empty1 = []

        # 방법 2: list() 함수 사용
        empty2 = list()

        assert empty1 == []
        assert empty2 == []
        assert len(empty1) == 0  # len()은 리스트의 길이(개수)를 알려줍니다

    def test_create_list_with_values(self):
        """값이 들어있는 리스트 만들기"""
        # 숫자 리스트
        numbers = [1, 2, 3, 4, 5]

        # 문자열 리스트
        fruits = ["사과", "바나나", "오렌지"]

        # 섞어서도 가능! (파이썬의 유연함)
        mixed = [1, "hello", 3.14, True]

        assert len(numbers) == 5
        assert len(fruits) == 3
        assert len(mixed) == 4

    def test_list_preserves_order_and_allows_duplicates(self):
        """리스트는 순서를 기억하고 중복을 허용합니다"""
        items = ["첫번째", "두번째", "세번째"]
        assert items[0] == "첫번째"
        assert items[1] == "두번째"

        # 같은 값이 여러 번 들어갈 수 있어요
        numbers = [1, 1, 2, 2, 2, 3]
        assert len(numbers) == 6
        assert numbers.count(2) == 3

    # === 인덱싱 ===

    def test_positive_index(self):
        """양수 인덱스: 앞에서부터 세기 (0부터 시작!)"""
        colors = ["빨강", "주황", "노랑", "초록", "파랑"]
        #          [0]     [1]     [2]     [3]     [4]

        assert colors[0] == "빨강"  # 첫 번째
        assert colors[1] == "주황"  # 두 번째
        assert colors[4] == "파랑"  # 다섯 번째 (마지막)

    def test_negative_index(self):
        """음수 인덱스: 뒤에서부터 세기"""
        colors = ["빨강", "주황", "노랑", "초록", "파랑"]
        #          [-5]    [-4]    [-3]    [-2]    [-1]

        assert colors[-1] == "파랑"  # 마지막
        assert colors[-2] == "초록"  # 마지막에서 두 번째

    def test_index_out_of_range(self):
        """범위를 벗어나면 IndexError 발생"""
        numbers = [10, 20, 30]

        with pytest.raises(IndexError):
            _ = numbers[3]

        with pytest.raises(IndexError):
            _ = numbers[-4]

    # === 슬라이싱 ===

    def test_basic_slicing(self):
        """기본 슬라이싱: list[시작:끝] - 끝은 미포함!"""
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        assert numbers[2:5] == [2, 3, 4]  # 2번부터 4번까지
        assert numbers[:3] == [0, 1, 2]   # 처음부터 2번까지
        assert numbers[7:] == [7, 8, 9]   # 7번부터 끝까지
        assert numbers[:] == numbers      # 전체 복사

    def test_slicing_with_step(self):
        """스텝 사용: list[시작:끝:스텝]"""
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        assert numbers[::2] == [0, 2, 4, 6, 8]   # 2칸씩 건너뛰기
        assert numbers[::-1] == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  # 역순

    def test_slicing_never_errors(self):
        """슬라이싱은 범위를 벗어나도 에러 없음 (안전함!)"""
        numbers = [1, 2, 3]

        assert numbers[1:100] == [2, 3]  # 가능한 만큼만
        assert numbers[100:200] == []     # 빈 리스트 반환

    # === 리스트 수정 ===

    def test_change_value(self):
        """값 변경하기"""
        fruits = ["사과", "바나나", "오렌지"]
        fruits[1] = "포도"
        assert fruits == ["사과", "포도", "오렌지"]

    def test_append_and_insert(self):
        """append(): 맨 뒤에 추가, insert(): 원하는 위치에 삽입"""
        numbers = [1, 2, 3]
        numbers.append(4)
        assert numbers == [1, 2, 3, 4]

        fruits = ["사과", "오렌지"]
        fruits.insert(1, "바나나")
        assert fruits == ["사과", "바나나", "오렌지"]

    def test_extend_vs_append(self):
        """extend vs append - 자주 헷갈리는 부분!"""
        list1 = [1, 2, 3]
        list1.append([4, 5])  # 리스트 자체를 하나의 요소로 추가
        assert list1 == [1, 2, 3, [4, 5]]

        list2 = [1, 2, 3]
        list2.extend([4, 5])  # 요소들을 풀어서 추가
        assert list2 == [1, 2, 3, 4, 5]

    def test_remove_and_pop(self):
        """remove(): 값으로 삭제, pop(): 인덱스로 삭제하고 반환"""
        numbers = [1, 2, 3, 2, 4]
        numbers.remove(2)  # 첫 번째 2만 삭제
        assert numbers == [1, 3, 2, 4]

        fruits = ["사과", "바나나", "오렌지"]
        removed = fruits.pop(1)
        assert removed == "바나나"
        assert fruits == ["사과", "오렌지"]

        stack = [1, 2, 3]
        last = stack.pop()  # 인덱스 없으면 마지막 삭제
        assert last == 3

    def test_del_and_clear(self):
        """del: 인덱스/슬라이스로 삭제, clear(): 전체 삭제"""
        numbers = [0, 1, 2, 3, 4, 5]
        del numbers[0]
        assert numbers == [1, 2, 3, 4, 5]

        del numbers[1:3]
        assert numbers == [1, 4, 5]

        numbers.clear()
        assert numbers == []


class TestPracticalUsage:
    """실무 활용 - 실제로 이렇게 씁니다"""

    def test_list_as_stack(self):
        """스택으로 사용: 마지막에 넣은 것을 먼저 꺼내기 (LIFO)"""
        stack = []
        stack.append("접시1")
        stack.append("접시2")
        stack.append("접시3")

        assert stack.pop() == "접시3"
        assert stack.pop() == "접시2"
        assert stack.pop() == "접시1"

    def test_find_element(self):
        """요소 찾기: in, index(), count()"""
        fruits = ["사과", "바나나", "오렌지", "바나나"]

        assert "바나나" in fruits
        assert "포도" not in fruits
        assert fruits.index("바나나") == 1  # 첫 번째 위치
        assert fruits.count("바나나") == 2

    def test_sorting(self):
        """정렬: sort() vs sorted()"""
        numbers = [3, 1, 4, 1, 5, 9, 2, 6]

        # sorted(): 새 리스트 반환 (원본 유지)
        sorted_nums = sorted(numbers)
        assert sorted_nums == [1, 1, 2, 3, 4, 5, 6, 9]
        assert numbers == [3, 1, 4, 1, 5, 9, 2, 6]  # 원본 그대로

        # sort(): 원본을 직접 정렬
        numbers.sort()
        assert numbers == [1, 1, 2, 3, 4, 5, 6, 9]

        # 내림차순
        numbers.sort(reverse=True)
        assert numbers == [9, 6, 5, 4, 3, 2, 1, 1]

    def test_reverse_list(self):
        """리스트 뒤집기"""
        original = [1, 2, 3, 4, 5]

        # [::-1]: 새 리스트 반환 (가장 많이 사용)
        reversed_list = original[::-1]
        assert reversed_list == [5, 4, 3, 2, 1]
        assert original == [1, 2, 3, 4, 5]  # 원본 유지

        # reverse(): 원본을 직접 뒤집음
        original.reverse()
        assert original == [5, 4, 3, 2, 1]

    def test_concatenation_and_multiplication(self):
        """리스트 합치기와 반복"""
        list1 = [1, 2, 3]
        list2 = [4, 5, 6]

        combined = list1 + list2
        assert combined == [1, 2, 3, 4, 5, 6]

        pattern = [1, 2] * 3
        assert pattern == [1, 2, 1, 2, 1, 2]

        zeros = [0] * 5
        assert zeros == [0, 0, 0, 0, 0]

    def test_min_max_sum(self):
        """리스트 통계: min(), max(), sum()"""
        numbers = [3, 1, 4, 1, 5, 9, 2, 6]

        assert min(numbers) == 1
        assert max(numbers) == 9
        assert sum(numbers) == 31

        average = sum(numbers) / len(numbers)
        assert average == 31 / 8


class TestEdgeCases:
    """주의사항 - 자주 하는 실수와 함정"""

    def test_mutable_default_argument_trap(self):
        """함정 1: 함수의 기본값으로 빈 리스트 쓰기"""

        # 잘못된 방법: 기본값이 공유됨!
        def bad_append(item, lst=[]):
            lst.append(item)
            return lst

        result1 = bad_append(1)
        result2 = bad_append(2)
        assert result2 == [1, 2]  # 예상: [2], 실제: [1, 2] - 버그!

        # 올바른 방법: None을 기본값으로
        def good_append(item, lst=None):
            if lst is None:
                lst = []
            lst.append(item)
            return lst

        result3 = good_append(1)
        result4 = good_append(2)
        assert result3 == [1]
        assert result4 == [2]

    def test_shallow_copy_trap(self):
        """함정 2: 얕은 복사 - 내부 객체는 공유됨"""
        import copy

        original = [[1, 2], [3, 4]]
        shallow = original[:]

        # 내부 리스트는 같은 객체
        shallow[0][0] = 999
        assert original[0][0] == 999  # 원본도 바뀜!

        # 해결책: 깊은 복사
        original2 = [[1, 2], [3, 4]]
        deep = copy.deepcopy(original2)
        deep[0][0] = 999
        assert original2[0][0] == 1  # 원본은 그대로!

    def test_remove_while_iterating_trap(self):
        """함정 3: 반복하면서 삭제하기"""
        numbers = [1, 2, 3, 4, 5]

        # 올바른 방법: 복사본으로 반복
        for num in numbers[:]:
            if num % 2 == 0:
                numbers.remove(num)

        assert numbers == [1, 3, 5]

    def test_list_multiplication_trap(self):
        """함정 4: 리스트 곱셈으로 2차원 배열 만들기"""
        # 잘못된 방법: 같은 리스트가 복제됨
        bad_matrix = [[0] * 3] * 3
        bad_matrix[0][0] = 1
        assert bad_matrix == [[1, 0, 0], [1, 0, 0], [1, 0, 0]]  # 모든 행이 바뀜!

        # 올바른 방법: 리스트 컴프리헨션
        good_matrix = [[0] * 3 for _ in range(3)]
        good_matrix[0][0] = 1
        assert good_matrix == [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

    def test_empty_list_access(self):
        """함정 5: 빈 리스트에서 접근하기"""
        empty = []

        with pytest.raises(IndexError):
            empty.pop()

        with pytest.raises(IndexError):
            _ = empty[0]

        # 안전하게 확인하고 접근하기
        first = empty[0] if empty else None
        assert first is None


class TestTips:
    """꿀팁 - 알아두면 유용한 것들"""

    def test_join_and_split(self):
        """리스트 <-> 문자열 변환"""
        words = ["Hello", "World", "Python"]
        sentence = " ".join(words)
        assert sentence == "Hello World Python"

        csv = "apple,banana,orange"
        fruits = csv.split(",")
        assert fruits == ["apple", "banana", "orange"]

    def test_enumerate_for_index(self):
        """인덱스와 값을 함께 얻기: enumerate()"""
        fruits = ["사과", "바나나", "오렌지"]

        result = []
        for index, fruit in enumerate(fruits):
            result.append(f"{index}: {fruit}")

        assert result == ["0: 사과", "1: 바나나", "2: 오렌지"]

    def test_zip_multiple_lists(self):
        """여러 리스트 동시 순회: zip()"""
        names = ["Alice", "Bob", "Charlie"]
        scores = [85, 92, 78]

        result = []
        for name, score in zip(names, scores):
            result.append(f"{name}: {score}점")

        assert result == ["Alice: 85점", "Bob: 92점", "Charlie: 78점"]

    def test_all_and_any(self):
        """모두 참? 하나라도 참? all(), any()"""
        assert all([True, True, True]) is True
        assert all([True, False, True]) is False

        assert any([False, False, True]) is True
        assert any([False, False, False]) is False

    def test_list_comprehension_preview(self):
        """리스트 컴프리헨션 맛보기 (Phase 8에서 자세히!)"""
        # 기존 방식
        squares_old = []
        for x in range(5):
            squares_old.append(x ** 2)

        # 리스트 컴프리헨션
        squares_new = [x ** 2 for x in range(5)]

        assert squares_old == squares_new == [0, 1, 4, 9, 16]

    def test_copy_methods_summary(self):
        """리스트 복사 방법 3가지"""
        original = [1, 2, 3]

        copy1 = original[:]       # 슬라이싱 (가장 많이 사용)
        copy2 = list(original)    # list() 함수
        copy3 = original.copy()   # copy() 메서드

        assert copy1 == copy2 == copy3 == original
        assert copy1 is not original

    def test_check_list_type(self):
        """리스트인지 확인하기"""
        my_list = [1, 2, 3]
        my_string = "hello"

        assert isinstance(my_list, list)
        assert not isinstance(my_string, list)
