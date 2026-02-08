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


class TestPracticalUsage:
    """실무 활용 - 실제로 이렇게 씁니다"""

    def test_add_single_element(self):
        """add()로 요소 하나 추가하기"""
        skills = {"python", "java"}
        skills.add("javascript")

        assert "javascript" in skills
        assert len(skills) == 3

        # 이미 있는 요소를 추가해도 에러 없이 무시됩니다
        skills.add("python")
        assert len(skills) == 3  # 여전히 3개

    def test_update_multiple_elements(self):
        """update()로 여러 요소 한번에 추가하기"""
        numbers = {1, 2, 3}
        # 리스트, 튜플, 다른 set 등을 넣을 수 있습니다
        numbers.update([4, 5])
        numbers.update((6, 7))
        numbers.update({8, 9})

        assert numbers == {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def test_remove_vs_discard(self):
        """remove()와 discard()의 차이"""
        fruits = {"apple", "banana", "cherry"}

        # remove(): 요소가 없으면 에러 발생
        fruits.remove("banana")
        assert "banana" not in fruits

        with pytest.raises(KeyError):
            fruits.remove("mango")  # 없는 요소 삭제 시도 -> 에러!

        # discard(): 요소가 없어도 에러 없이 넘어감
        fruits.discard("mango")  # 에러 없음
        fruits.discard("apple")
        assert "apple" not in fruits

    def test_pop_removes_random_element(self):
        """pop()은 임의의 요소를 제거하고 반환합니다"""
        numbers = {10, 20, 30}

        # 어떤 요소가 나올지 모릅니다 (순서가 없으니까)
        popped = numbers.pop()

        assert popped in {10, 20, 30}
        assert len(numbers) == 2

    def test_clear_removes_all(self):
        """clear()로 모든 요소 삭제"""
        data = {1, 2, 3, 4, 5}
        data.clear()

        assert len(data) == 0
        assert data == set()

    def test_remove_duplicates_from_list(self):
        """리스트에서 중복 제거하기 - set의 가장 흔한 활용"""
        # 중복이 있는 리스트
        with_duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

        # set으로 변환하면 중복이 사라집니다
        unique = list(set(with_duplicates))

        assert len(unique) == 4
        # 주의: 원래 순서가 보장되지 않을 수 있습니다!
        assert set(unique) == {1, 2, 3, 4}

    def test_keep_order_while_removing_duplicates(self):
        """순서를 유지하면서 중복 제거하기 (Python 3.7+)"""
        items = ["b", "a", "b", "c", "a", "d", "c"]

        # dict.fromkeys()를 활용한 트릭
        # 딕셔너리는 Python 3.7+에서 삽입 순서를 보장합니다
        unique_ordered = list(dict.fromkeys(items))

        assert unique_ordered == ["b", "a", "c", "d"]  # 순서 유지!

    def test_find_common_elements(self):
        """두 리스트의 공통 요소 찾기"""
        team_a = ["alice", "bob", "charlie", "david"]
        team_b = ["bob", "david", "eve", "frank"]

        # set의 교집합 연산으로 쉽게 찾을 수 있습니다
        common_members = set(team_a) & set(team_b)

        assert common_members == {"bob", "david"}

    def test_union_combines_all(self):
        """합집합 - 두 집합의 모든 요소"""
        backend = {"python", "java", "go"}
        frontend = {"javascript", "typescript", "python"}

        # | 연산자 또는 union() 메서드
        all_languages = backend | frontend
        also_all = backend.union(frontend)

        assert all_languages == {"python", "java", "go", "javascript", "typescript"}
        assert all_languages == also_all

    def test_intersection_common_only(self):
        """교집합 - 공통 요소만"""
        students_math = {"alice", "bob", "charlie"}
        students_science = {"bob", "charlie", "david"}

        # & 연산자 또는 intersection() 메서드
        both_classes = students_math & students_science
        also_both = students_math.intersection(students_science)

        assert both_classes == {"bob", "charlie"}
        assert both_classes == also_both

    def test_difference_subtract_sets(self):
        """차집합 - 한쪽에만 있는 요소"""
        all_users = {"alice", "bob", "charlie", "david"}
        premium_users = {"bob", "david"}

        # - 연산자 또는 difference() 메서드
        free_users = all_users - premium_users
        also_free = all_users.difference(premium_users)

        assert free_users == {"alice", "charlie"}
        assert free_users == also_free

    def test_symmetric_difference_exclusive_elements(self):
        """대칭 차집합 - 한쪽에만 있는 모든 요소"""
        # A에만 있거나 B에만 있는 요소 (공통 제외)
        group_a = {"apple", "banana", "cherry"}
        group_b = {"banana", "cherry", "date"}

        # ^ 연산자 또는 symmetric_difference() 메서드
        exclusive = group_a ^ group_b
        also_exclusive = group_a.symmetric_difference(group_b)

        assert exclusive == {"apple", "date"}
        assert exclusive == also_exclusive


