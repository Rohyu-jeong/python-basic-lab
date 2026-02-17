"""
Phase 2 - 딕셔너리 (Dictionary)
==============================
학습 목표: 키-값 쌍으로 데이터를 저장하고 빠르게 검색하기

핵심 개념:
- 딕셔너리는 키(key)와 값(value)의 쌍으로 이루어진 자료구조
- 키는 유일해야 하고, 불변(immutable) 타입만 가능
- 순서가 보장됨 (Python 3.7+)
- 해시 테이블 기반으로 검색이 매우 빠름 (O(1))
"""


class TestBasicConcept:
    """기본 개념 - 딕셔너리 생성과 기본 조작"""

    def test_create_dict(self):
        """딕셔너리 만드는 여러 방법"""
        # 중괄호로 생성 (가장 흔한 방법)
        person = {"name": "철수", "age": 25, "city": "서울"}

        # dict() 생성자 사용
        person2 = dict(name="영희", age=23, city="부산")

        # 리스트의 튜플로부터 생성
        items = [("apple", 1000), ("banana", 500)]
        prices = dict(items)

        # 빈 딕셔너리
        empty1 = {}
        empty2 = dict()

        assert person["name"] == "철수"
        assert person2["name"] == "영희"
        assert prices["apple"] == 1000
        assert len(empty1) == 0

    def test_access_and_modify(self):
        """값 읽기, 수정, 추가, 삭제"""
        scores = {"국어": 90, "영어": 85, "수학": 95}

        # 읽기: 대괄호 사용
        korean = scores["국어"]
        assert korean == 90

        # 수정: 기존 키에 새 값 할당
        scores["영어"] = 90
        assert scores["영어"] == 90

        # 추가: 새로운 키에 값 할당
        scores["과학"] = 88
        assert "과학" in scores

        # 삭제: del 키워드
        del scores["수학"]
        assert "수학" not in scores
        assert len(scores) == 3

    def test_key_not_found(self):
        """없는 키 접근 시 주의점"""
        data = {"a": 1, "b": 2}

        # 대괄호로 없는 키 접근 → KeyError 발생!
        import pytest

        with pytest.raises(KeyError):
            _ = data["z"]

        # get()은 없는 키도 안전하게 처리
        # 키가 없으면 None 반환
        result = data.get("z")
        assert result is None

        # 기본값 지정 가능
        result = data.get("z", 0)
        assert result == 0

        # 원본은 변경되지 않음
        assert "z" not in data

    def test_keys_values_items(self):
        """키, 값, 키-값 쌍 순회하기"""
        fruit_colors = {"사과": "빨강", "바나나": "노랑", "포도": "보라"}

        # keys(): 모든 키
        keys = list(fruit_colors.keys())
        assert keys == ["사과", "바나나", "포도"]

        # values(): 모든 값
        values = list(fruit_colors.values())
        assert values == ["빨강", "노랑", "보라"]

        # items(): (키, 값) 튜플
        items = list(fruit_colors.items())
        assert items == [("사과", "빨강"), ("바나나", "노랑"), ("포도", "보라")]

        # for문에서 활용
        result = []
        for fruit, color in fruit_colors.items():
            result.append(f"{fruit}은 {color}색")
        assert result[0] == "사과은 빨강색"


