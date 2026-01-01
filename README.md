# Python Basic Lab

> Python 문법의 기초부터 심화까지, 테스트로 배우는 Python 입문서

[![Python Version](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![pytest Version](https://img.shields.io/badge/pytest-8.0-green.svg)](https://docs.pytest.org/)

## 📌 소개

이 저장소는 **Python 언어의 핵심 문법**을 학습 테스트(Learning Test)를 통해 익힙니다.

프레임워크나 라이브러리가 아닌, 순수 Python 언어에 집중합니다.

```
"코드를 실행하고, 결과로 이해한다"
```

## 🎯 학습 목표

- Python 문법을 **실행 가능한 코드**로 직접 검증
- 단순 암기가 아닌 **"왜 이렇게 동작하는가"** 이해
- **흔한 실수**와 **Pythonic한 코드**의 차이를 실험으로 체득
- 실무에서 바로 쓸 수 있는 **Python 기본기** 구축

## 🛠 기술 스택

| 구분 | 기술 |
|------|------|
| Language | Python 3.12 |
| Test Framework | pytest 9.0 |
| Package Manager | pip / uv |

## 📁 프로젝트 구조

```
tests/
├── phase1_fundamentals/         # 변수, 숫자, 문자열, 불리언
├── phase2_collections/          # list, tuple, set, dict
├── phase3_control_flow/         # if, for, while, match
├── phase4_functions/            # 함수, 람다, 스코프
├── phase5_oop/                  # 클래스, 상속, 특수 메서드
├── phase6_exceptions/           # 예외 처리
├── phase7_file_io/              # 파일 입출력
├── phase8_pythonic/             # 컴프리헨션, 제너레이터
├── phase9_advanced/             # 데코레이터, 클로저
└── phase10_modern/              # 타입 힌트, Protocol
```

## 📚 학습 내용

### Part 1: 기초 (Phase 1 ~ 3)

<details>
<summary><b>Phase 1. Fundamentals</b> - 변수와 기본 타입</summary>

| 테스트 | 학습 내용 |
|--------|-----------|
| `test_01_variables.py` | 동적 타이핑, 변수 할당, 다중 할당 |
| `test_02_numbers.py` | int, float, 연산자, 진수 변환 |
| `test_03_strings.py` | f-string, 슬라이싱, 주요 메서드 |
| `test_04_booleans.py` | True/False, truthy/falsy |
| `test_05_none.py` | None, is None 체크 |

**핵심 질문**
- Python은 왜 변수 선언 시 타입을 명시하지 않는가?
- `==`와 `is`의 차이는 무엇인가?
- 0, "", [], None이 모두 False로 평가되는 이유는?

</details>

<details>
<summary><b>Phase 2. Collections</b> - 컬렉션 자료형</summary>

| 테스트 | 학습 내용 |
|--------|-----------|
| `test_01_list.py` | 생성, 인덱싱, 슬라이싱, 메서드 |
| `test_02_tuple.py` | 불변 시퀀스, 언패킹, 네임드 튜플 |
| `test_03_set.py` | 집합 연산, 중복 제거 |
| `test_04_dict.py` | 키-값, 메서드, defaultdict |
| `test_05_collection_ops.py` | 공통 연산, 변환, 정렬 |

**핵심 질문**
- list와 tuple의 차이는? 언제 각각 사용하는가?
- dict의 키로 사용할 수 있는 타입과 없는 타입은?
- 슬라이싱 `[start:end:step]`의 동작 원리는?

</details>

<details>
<summary><b>Phase 3. Control Flow</b> - 제어문</summary>

| 테스트 | 학습 내용 |
|--------|-----------|
| `test_01_if_else.py` | 조건문, 삼항 연산자, 체이닝 |
| `test_02_for_loop.py` | for-in, range, enumerate, zip |
| `test_03_while_loop.py` | while, 무한 루프 패턴 |
| `test_04_match_case.py` | 패턴 매칭 (Python 3.10+) |
| `test_05_loop_control.py` | break, continue, for-else |

**핵심 질문**
- `for-else`는 어떤 상황에서 유용한가?
- `enumerate`와 `zip`은 왜 자주 사용되는가?
- `match-case`가 기존 `if-elif`보다 나은 점은?

</details>

### Part 2: 함수와 객체 (Phase 4 ~ 5)

<details>
<summary><b>Phase 4. Functions</b> - 함수</summary>

| 테스트 | 학습 내용 |
|--------|-----------|
| `test_01_basic_function.py` | def, 호출, docstring |
| `test_02_arguments.py` | 위치/키워드 인자, *args, **kwargs |
| `test_03_return_values.py` | 단일/다중 반환, None 반환 |
| `test_04_lambda.py` | 익명 함수, 고차 함수 |
| `test_05_scope.py` | LEGB 규칙, global, nonlocal |
| `test_06_builtin_functions.py` | map, filter, reduce, sorted |

**핵심 질문**
- `*args`와 `**kwargs`는 각각 언제 사용하는가?
- Python에서 함수가 "일급 객체"라는 것은 무슨 의미인가?
- LEGB 스코프 규칙이란?

</details>

<details>
<summary><b>Phase 5. OOP</b> - 객체지향 프로그래밍</summary>

| 테스트 | 학습 내용 |
|--------|-----------|
| `test_01_class_basics.py` | 클래스 정의, 인스턴스 생성 |
| `test_02_init_self.py` | 생성자, self의 역할 |
| `test_03_inheritance.py` | 상속, super(), MRO |
| `test_04_special_methods.py` | __str__, __repr__, __eq__ 등 |
| `test_05_class_method.py` | @classmethod, @staticmethod |
| `test_06_property.py` | @property, getter/setter |
| `test_07_dataclass.py` | @dataclass 데코레이터 |
| `test_08_abstract_class.py` | ABC, @abstractmethod |

**핵심 질문**
- `self`는 왜 항상 첫 번째 인자로 명시해야 하는가?
- `__str__`과 `__repr__`의 차이는?
- `@dataclass`는 어떤 코드를 자동으로 생성해주는가?

</details>

### Part 3: 실무 필수 (Phase 6 ~ 8)

<details>
<summary><b>Phase 6. Exceptions</b> - 예외 처리</summary>

| 테스트 | 학습 내용 |
|--------|-----------|
| `test_01_try_except.py` | try-except-else-finally 구조 |
| `test_02_exception_types.py` | 내장 예외 종류 |
| `test_03_raise.py` | 예외 발생, 재발생 |
| `test_04_custom_exception.py` | 커스텀 예외 클래스 |
| `test_05_finally.py` | 리소스 정리, 예외 체이닝 |

**핵심 질문**
- `try-except-else-finally`에서 `else`는 언제 실행되는가?
- 예외를 `raise`할 때 `from`을 붙이면 어떤 효과가 있는가?
- 커스텀 예외는 언제 만들어야 하는가?

</details>

<details>
<summary><b>Phase 7. File I/O</b> - 파일 입출력</summary>

| 테스트 | 학습 내용 |
|--------|-----------|
| `test_01_read_write.py` | open(), read(), write() |
| `test_02_context_manager.py` | with문, 자동 리소스 관리 |
| `test_03_path_lib.py` | pathlib.Path 활용 |
| `test_04_json_csv.py` | JSON, CSV 처리 |

**핵심 질문**
- `with open()`을 사용해야 하는 이유는?
- `pathlib`이 `os.path`보다 권장되는 이유는?
- 파일 인코딩을 명시해야 하는 이유는?

</details>

<details>
<summary><b>Phase 8. Pythonic</b> - 파이썬다운 코드</summary>

| 테스트 | 학습 내용 |
|--------|-----------|
| `test_01_list_comprehension.py` | 리스트 컴프리헨션 |
| `test_02_dict_comprehension.py` | 딕셔너리 컴프리헨션 |
| `test_03_generator.py` | yield, 제너레이터 표현식 |
| `test_04_iterator.py` | __iter__, __next__, iter() |
| `test_05_unpacking.py` | *, ** 언패킹, 확장 언패킹 |
| `test_06_walrus.py` | := 할당 표현식 |

**핵심 질문**
- 컴프리헨션은 왜 for 루프보다 권장되는가?
- 제너레이터는 리스트와 무엇이 다르고, 언제 사용하는가?
- `:=` (walrus operator)는 어떤 상황에서 유용한가?

</details>

### Part 4: 심화 (Phase 9 ~ 10)

<details>
<summary><b>Phase 9. Advanced</b> - 심화 문법</summary>

| 테스트 | 학습 내용 |
|--------|-----------|
| `test_01_decorator.py` | 함수/클래스 데코레이터 |
| `test_02_closure.py` | 클로저, 자유 변수 |
| `test_03_context_manager_custom.py` | __enter__, __exit__, @contextmanager |
| `test_04_metaclass_intro.py` | 메타클래스 기초 |

**핵심 질문**
- 데코레이터는 내부적으로 어떻게 동작하는가?
- 클로저란 무엇이고, 어떤 상황에서 유용한가?
- 커스텀 컨텍스트 매니저는 어떻게 만드는가?

</details>

<details>
<summary><b>Phase 10. Modern Python</b> - 모던 문법</summary>

| 테스트 | 학습 내용 |
|--------|-----------|
| `test_01_type_hints.py` | 타입 힌트, Generic, Union |
| `test_02_protocol.py` | Protocol (구조적 서브타이핑) |
| `test_03_enum.py` | Enum, auto() |
| `test_04_pattern_matching.py` | match-case 심화 |

**핵심 질문**
- 타입 힌트는 런타임에 영향을 주는가?
- `Protocol`과 `ABC`의 차이는?
- 패턴 매칭에서 가드(guard) 조건은 어떻게 사용하는가?

</details>

## 📝 학습 테스트 작성 원칙

### 1. 테스트 구조

```python
"""
Phase 1 - Variables (변수)
==========================
학습 목표: Python의 동적 타이핑과 변수 할당 이해

핵심 개념:
- 변수는 값을 가리키는 이름표
- 타입은 값에 붙어있고, 변수에 붙어있지 않음
"""
import pytest


class TestBasicConcept:
    """기본 개념 - 가장 먼저 알아야 할 것"""

    def test_variable_assignment(self):
        """변수에 값을 할당하면 그 값을 가리키게 된다"""
        x = 10  # x라는 이름표를 10이라는 값에 붙인다
        y = x   # y도 같은 10을 가리킨다

        assert x == 10
        assert y == 10
        assert x is y  # 같은 객체를 가리킴


class TestPracticalUsage:
    """실무 활용 - 실제로 이렇게 씁니다"""

    def test_multiple_assignment(self):
        """여러 변수에 동시에 값 할당하기"""
        a, b, c = 1, 2, 3

        assert a == 1
        assert b == 2
        assert c == 3


class TestEdgeCases:
    """주의사항 - 자주 하는 실수"""

    def test_mutable_default_argument_trap(self):
        """함수의 기본값으로 빈 리스트를 쓰면 안 되는 이유"""
        def bad_append(item, items=[]):  # 이렇게 하면 안 됨!
            items.append(item)
            return items

        result1 = bad_append(1)
        result2 = bad_append(2)  # 예상: [2], 실제: [1, 2]

        # 같은 리스트 객체가 재사용되어 버그 발생
        assert result2 == [1, 2]  # 의도하지 않은 결과!
```

### 2. 원칙

| 원칙 | 설명 |
|------|------|
| **docstring** | 각 테스트가 무엇을 검증하는지 한글로 설명 |
| **클래스 그룹핑** | 기본 / 실무 / 주의사항 / 꿀팁으로 분류 |
| **주석 활용** | 코드 중간에 "왜" 이렇게 동작하는지 설명 |
| **실행 가능** | 모든 테스트는 실제로 실행되고 통과해야 함 |

### 3. 학습 테스트가 다루는 것

```
✅ 기본 사용법
✅ 동작 원리 (왜 이렇게 동작하는가)
✅ 실무에서 자주 쓰는 패턴
✅ 흔한 실수와 함정
✅ Pythonic한 대안
```

## 🚀 실행 방법

```bash
# 전체 테스트 실행
pytest

# 상세 출력
pytest -v

# 특정 Phase만 실행
pytest tests/phase1_fundamentals/

# 특정 파일만 실행
pytest tests/phase1_fundamentals/test_01_variables.py

# 이름에 특정 문자열 포함된 테스트만
pytest -k "list"

# 첫 실패에서 중단
pytest -x

# print 출력 보기
pytest -s
```

## 📖 참고 자료

- [Python 공식 문서](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Fluent Python](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)

## 🔗 관련 저장소

| 저장소 | 설명 | 대상 |
|--------|------|------|
| **python-basic-lab** | Python 문법 입문 | 초보자 |
| python-core-lab | Python 내부 구현 탐구 | 문법 익숙한 사람 |
| testing-lab | pytest 심화 학습 | 테스트 작성 필요한 사람 |

---

<div align="center">

**"Simple is better than complex."**

*— The Zen of Python*

</div>