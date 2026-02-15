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


class TestEdgeCases:
    """주의사항 - 자주 하는 실수와 함정"""

    def test_set_equality_ignores_order(self):
        """set 비교는 순서와 무관합니다"""
        set1 = {1, 2, 3}
        set2 = {3, 1, 2}
        set3 = {3, 2, 1}

        # 모두 같은 set입니다
        assert set1 == set2 == set3

    def test_set_in_list_vs_set_equality(self):
        """set과 list는 다른 타입입니다"""
        my_set = {1, 2, 3}
        my_list = [1, 2, 3]

        # 요소가 같아도 타입이 다르면 다릅니다
        assert my_set != my_list

    def test_modifying_set_during_iteration(self):
        """반복 중 set 수정하면 에러납니다"""
        numbers = {1, 2, 3, 4, 5}

        # 이렇게 하면 에러!
        # for n in numbers:
        #     if n % 2 == 0:
        #         numbers.remove(n)  # RuntimeError!

        # 대신 복사본을 순회하거나
        for n in numbers.copy():
            if n % 2 == 0:
                numbers.remove(n)

        assert numbers == {1, 3, 5}

    def test_set_comprehension_alternative(self):
        """set comprehension으로 조건부 생성"""
        # 위의 문제를 더 파이썬스럽게 해결
        original = {1, 2, 3, 4, 5}
        odd_only = {n for n in original if n % 2 != 0}

        assert odd_only == {1, 3, 5}

    def test_subset_and_superset(self):
        """부분집합과 상위집합 확인"""
        small = {1, 2}
        medium = {1, 2, 3}
        large = {1, 2, 3, 4, 5}

        # 부분집합: small의 모든 요소가 medium에 있는가?
        assert small.issubset(medium)
        assert small <= medium  # 연산자로도 가능

        # 진부분집합: 부분집합이면서 같지 않은가?
        assert small < medium  # True
        assert medium < medium  # False (자기 자신)

        # 상위집합: large가 medium의 모든 요소를 포함하는가?
        assert large.issuperset(medium)
        assert large >= medium

    def test_disjoint_no_common_elements(self):
        """서로소 - 공통 요소가 없는 집합"""
        evens = {2, 4, 6, 8}
        odds = {1, 3, 5, 7}
        primes = {2, 3, 5, 7}

        # evens와 odds는 공통 요소가 없습니다
        assert evens.isdisjoint(odds)

        # evens와 primes는 2가 공통입니다
        assert not evens.isdisjoint(primes)

    def test_copy_creates_shallow_copy(self):
        """copy()는 얕은 복사를 합니다"""
        original = {1, 2, 3}
        copied = original.copy()

        # 복사본 수정해도 원본은 그대로
        copied.add(4)

        assert original == {1, 2, 3}
        assert copied == {1, 2, 3, 4}

    def test_set_operations_return_new_set(self):
        """집합 연산은 새로운 set을 반환합니다"""
        a = {1, 2, 3}
        b = {3, 4, 5}

        union = a | b

        # 원본은 변하지 않습니다
        assert a == {1, 2, 3}
        assert b == {3, 4, 5}
        assert union == {1, 2, 3, 4, 5}

    def test_inplace_operations_modify_original(self):
        """update 계열 메서드는 원본을 수정합니다"""
        a = {1, 2, 3}
        b = {3, 4, 5}

        # |= 는 update()와 같습니다
        a |= b  # a = a | b 와 달리 a를 직접 수정

        assert a == {1, 2, 3, 4, 5}

        c = {10, 20}
        c.update([30, 40])
        assert c == {10, 20, 30, 40}

        d = {1, 2, 3, 4, 5}
        d &= {2, 3, 4}  # intersection_update
        assert d == {2, 3, 4}

        e = {1, 2, 3, 4, 5}
        e -= {1, 2}  # difference_update
        assert e == {3, 4, 5}


class TestTips:
    """꿀팁 - 알아두면 유용한 것들"""

    def test_count_unique_items(self):
        """고유 항목 개수 세기"""
        purchases = ["apple", "banana", "apple", "cherry", "banana", "apple"]

        unique_count = len(set(purchases))
        assert unique_count == 3

    def test_check_all_unique(self):
        """모든 요소가 고유한지 확인하기"""
        # 리스트의 길이와 set으로 변환한 길이가 같으면 중복 없음
        no_duplicates = [1, 2, 3, 4, 5]
        has_duplicates = [1, 2, 2, 3, 4]

        def is_all_unique(items):
            return len(items) == len(set(items))

        assert is_all_unique(no_duplicates) is True
        assert is_all_unique(has_duplicates) is False

    def test_find_duplicates(self):
        """중복된 요소 찾기"""
        items = ["a", "b", "a", "c", "b", "d", "a"]

        seen = set()
        duplicates = set()

        for item in items:
            if item in seen:
                duplicates.add(item)
            seen.add(item)

        assert duplicates == {"a", "b"}

    def test_multiple_set_operations(self):
        """여러 set을 한번에 연산하기"""
        a = {1, 2, 3}
        b = {2, 3, 4}
        c = {3, 4, 5}

        # 세 집합 모두에 있는 요소
        common_all = a & b & c
        assert common_all == {3}

        # 세 집합 중 하나라도 있으면
        any_of_them = a | b | c
        assert any_of_them == {1, 2, 3, 4, 5}

        # intersection/union에 여러 인자 전달 가능
        also_common = a.intersection(b, c)
        assert also_common == {3}

    def test_set_for_fast_lookup_table(self):
        """빠른 검색을 위한 set 활용"""
        # 금지된 단어 목록을 set으로 관리
        banned_words = {"spam", "virus", "malware", "phishing"}

        def is_safe(text):
            words = text.lower().split()
            # set의 in 연산은 O(1)로 매우 빠릅니다
            return not any(word in banned_words for word in words)

        assert is_safe("Hello world") is True
        assert is_safe("Click here no spam") is False

    def test_set_comprehension(self):
        """set comprehension - 조건부로 set 만들기"""
        # 1부터 20까지 중 3의 배수만
        multiples_of_3 = {n for n in range(1, 21) if n % 3 == 0}
        assert multiples_of_3 == {3, 6, 9, 12, 15, 18}

        # 문자열의 모음만 추출
        text = "Hello World"
        vowels = {char.lower() for char in text if char.lower() in "aeiou"}
        assert vowels == {"e", "o"}

    def test_set_with_tuple_for_coordinates(self):
        """좌표나 쌍을 set으로 관리하기"""
        # 방문한 좌표들을 기록 (게임, 그래프 탐색 등에서 유용)
        visited = set()

        visited.add((0, 0))
        visited.add((1, 0))
        visited.add((1, 1))
        visited.add((0, 0))  # 중복 - 무시됨

        assert len(visited) == 3
        assert (1, 1) in visited
        assert (2, 2) not in visited

    def test_group_and_compare(self):
        """그룹 비교하기"""
        # 두 팀이 가진 스킬 비교
        team_alpha = {"python", "java", "sql", "aws"}
        team_beta = {"javascript", "react", "sql", "aws"}

        # 공통 스킬
        shared_skills = team_alpha & team_beta
        assert shared_skills == {"sql", "aws"}

        # alpha만의 스킬
        alpha_unique = team_alpha - team_beta
        assert alpha_unique == {"python", "java"}

        # 어느 한 팀만 가진 스킬 (희소 스킬)
        rare_skills = team_alpha ^ team_beta
        assert rare_skills == {"python", "java", "javascript", "react"}

    def test_filter_using_set(self):
        """set을 이용한 빠른 필터링"""
        all_users = ["alice", "bob", "charlie", "david", "eve"]
        active_users = {"alice", "charlie", "eve"}

        # 활성 사용자만 필터링
        result = [user for user in all_users if user in active_users]
        assert result == ["alice", "charlie", "eve"]

        # 비활성 사용자만 필터링
        inactive = [user for user in all_users if user not in active_users]
        assert inactive == ["bob", "david"]
        