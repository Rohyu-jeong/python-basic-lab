"""
Phase 1 - 문자열(Strings)
=========================
학습 목표: Python에서 텍스트를 다루는 방법을 배웁니다

핵심 개념:
- 문자열은 문자들의 순서 있는 나열입니다 (시퀀스)
- 문자열은 불변(immutable)입니다 - 한번 만들면 수정 불가
- 작은따옴표('')와 큰따옴표("")는 동일하게 동작합니다
- f-string은 Python 3.6+에서 가장 권장되는 문자열 포매팅 방식입니다
"""


class TestBasicConcept:
    """기본 개념 - 문자열을 만들고 다루는 가장 기본적인 방법"""

    def test_string_creation(self):
        """문자열을 만드는 여러 가지 방법"""
        # 작은따옴표로 만들기
        single = 'Hello'

        # 큰따옴표로 만들기 - 작은따옴표와 완전히 동일!
        double = "Hello"

        assert single == double  # 둘은 같습니다

        # 따옴표 안에 따옴표를 넣고 싶을 때
        # 바깥과 다른 따옴표를 쓰면 됩니다
        quote1 = "He said 'Hi'"
        quote2 = 'He said "Hi"'

        assert "'" in quote1  # 작은따옴표 포함
        assert '"' in quote2  # 큰따옴표 포함

    def test_multiline_string(self):
        """여러 줄 문자열 - 삼중 따옴표 사용"""
        # 삼중 따옴표(''' 또는 """)로 여러 줄 작성
        poem = """장미는 빨갛고
제비꽃은 파랗고
Python은 멋지다"""

        # 줄바꿈 문자(\n)가 포함됩니다
        assert "\n" in poem
        assert poem.count("\n") == 2  # 줄바꿈이 2개

    def test_escape_sequences(self):
        """이스케이프 시퀀스 - 특수 문자 표현하기"""
        # \n: 줄바꿈 (new line)
        newline = "첫째줄\n둘째줄"
        assert len(newline) == 7  # \n은 1글자로 취급 (3 + 1 + 3)

        # \t: 탭 (tab)
        tabbed = "이름\t나이"
        assert "\t" in tabbed

        # \\: 역슬래시 자체
        path = "C:\\Users\\Documents"
        assert path.count("\\") == 2

        # \': 작은따옴표, \": 큰따옴표
        escaped = 'It\'s a "test"'
        assert "'" in escaped and '"' in escaped

    def test_raw_string(self):
        """raw 문자열 - 이스케이프 무시하기"""
        # r을 붙이면 이스케이프 시퀀스가 무시됩니다
        # 파일 경로나 정규표현식에서 유용!
        normal = "C:\new\test"  # \n이 줄바꿈으로 해석됨
        raw = r"C:\new\test"  # \n이 그대로 문자로

        assert len(raw) > len(normal)  # raw가 더 김
        assert "\\n" in raw  # 역슬래시+n이 그대로 있음

    def test_string_immutability(self):
        """문자열의 불변성 - 한번 만들면 수정 불가"""
        text = "Hello"

        # 문자열은 수정할 수 없습니다!
        # text[0] = 'h'  # 이렇게 하면 TypeError 발생

        # 대신 새로운 문자열을 만들어야 합니다
        new_text = "h" + text[1:]  # 'h' + 'ello'
        assert new_text == "hello"
        assert text == "Hello"  # 원본은 그대로!


class TestPracticalUsage:
    """실무 활용 - 실제로 자주 사용하는 문자열 기능들"""

    def test_f_string_basic(self):
        """f-string 기본 - 가장 현대적인 문자열 포매팅"""
        name = "Python"
        version = 3.12

        # f를 붙이고 중괄호 안에 변수를 넣으면 됩니다
        message = f"Hello, {name}!"
        assert message == "Hello, Python!"

        # 여러 변수도 가능
        info = f"{name} 버전 {version}"
        assert info == "Python 버전 3.12"

    def test_f_string_expressions(self):
        """f-string 표현식 - 중괄호 안에서 계산하기"""
        x = 10
        y = 3

        # 중괄호 안에서 직접 계산 가능!
        result = f"{x} + {y} = {x + y}"
        assert result == "10 + 3 = 13"

        # 함수 호출도 가능
        name = "python"
        greeting = f"Hello, {name.upper()}!"
        assert greeting == "Hello, PYTHON!"

        # 조건 표현식도 가능
        score = 85
        grade = f"결과: {'합격' if score >= 60 else '불합격'}"
        assert grade == "결과: 합격"

    def test_f_string_formatting(self):
        """f-string 포맷 지정 - 숫자 다루기"""
        # 소수점 자릿수 지정: {값:.자릿수f}
        pi = 3.14159265
        formatted = f"파이: {pi:.2f}"  # 소수점 2자리
        assert formatted == "파이: 3.14"

        # 천단위 콤마: {값:,}
        big_number = 1234567
        with_comma = f"금액: {big_number:,}원"
        assert with_comma == "금액: 1,234,567원"

        # 퍼센트 표시: {값:.자릿수%}
        ratio = 0.756
        percent = f"진행률: {ratio:.1%}"
        assert percent == "진행률: 75.6%"

    def test_string_indexing(self):
        """문자열 인덱싱 - 특정 위치의 문자 가져오기"""
        text = "Python"
        #       012345  <- 인덱스 (0부터 시작!)
        #      -6-5-4-3-2-1  <- 음수 인덱스 (뒤에서부터)

        # 양수 인덱스: 앞에서부터
        assert text[0] == "P"  # 첫 번째 문자
        assert text[1] == "y"  # 두 번째 문자

        # 음수 인덱스: 뒤에서부터
        assert text[-1] == "n"  # 마지막 문자
        assert text[-2] == "o"  # 뒤에서 두 번째

    def test_string_slicing(self):
        """문자열 슬라이싱 - 부분 문자열 추출하기"""
        text = "Hello, World!"
        #       0123456789...

        # 기본 문법: text[시작:끝]
        # 시작은 포함, 끝은 미포함!
        assert text[0:5] == "Hello"  # 0~4번 인덱스
        assert text[7:12] == "World"  # 7~11번 인덱스

        # 시작 생략: 처음부터
        assert text[:5] == "Hello"

        # 끝 생략: 끝까지
        assert text[7:] == "World!"

        # 음수 인덱스 활용
        assert text[-6:] == "World!"  # 뒤에서 6글자

        # 스텝(간격) 지정: text[시작:끝:스텝]
        assert text[::2] == "Hlo ol!"  # 2칸씩 건너뛰기
        assert text[::-1] == "!dlroW ,olleH"  # 역순!

    def test_string_methods_search(self):
        """문자열 검색 메서드"""
        text = "Hello, World! Hello, Python!"

        # find(): 찾은 위치 반환, 없으면 -1
        assert text.find("World") == 7
        assert text.find("Java") == -1

        # index(): find와 같지만 없으면 에러 발생
        assert text.index("World") == 7

        # count(): 등장 횟수
        assert text.count("Hello") == 2
        assert text.count("o") == 4

        # startswith(), endswith(): 시작/끝 확인
        assert text.startswith("Hello")
        assert text.endswith("!")

        # endswith는 튜플로 여러 패턴 확인 가능
        filename = "document.pdf"
        assert filename.endswith((".pdf", ".doc", ".txt"))

        # in 연산자: 포함 여부 (가장 직관적!)
        assert "World" in text
        assert "Java" not in text

    def test_string_methods_transform(self):
        """문자열 변환 메서드"""
        # 대소문자 변환
        assert "hello".upper() == "HELLO"
        assert "HELLO".lower() == "hello"
        assert "hello world".title() == "Hello World"  # 각 단어 첫글자 대문자
        assert "hello world".capitalize() == "Hello world"  # 문장 첫글자만

        # 공백 제거
        text = "  Hello, World!  "
        assert text.strip() == "Hello, World!"  # 양쪽 공백 제거
        assert text.lstrip() == "Hello, World!  "  # 왼쪽만
        assert text.rstrip() == "  Hello, World!"  # 오른쪽만

        # 문자 교체
        assert "Hello".replace("l", "L") == "HeLLo"
        assert "a-b-c".replace("-", "_") == "a_b_c"

    def test_string_methods_split_join(self):
        """split과 join - 문자열 분리와 결합"""
        # split(): 문자열을 리스트로 분리
        sentence = "Python is awesome"
        words = sentence.split()  # 공백 기준 분리
        assert words == ["Python", "is", "awesome"]

        csv_data = "apple,banana,cherry"
        fruits = csv_data.split(",")  # 콤마 기준 분리
        assert fruits == ["apple", "banana", "cherry"]

        # join(): 리스트를 문자열로 결합
        # "구분자".join(리스트) 형태로 사용
        words = ["Python", "is", "fun"]
        sentence = " ".join(words)
        assert sentence == "Python is fun"

        path_parts = ["home", "user", "documents"]
        path = "/".join(path_parts)
        assert path == "home/user/documents"

    def test_string_validation_methods(self):
        """문자열 검증 메서드 - 문자열의 성질 확인"""
        # 숫자로만 구성?
        assert "12345".isdigit() == True
        assert "123.45".isdigit() == False  # 점이 포함됨

        # 알파벳으로만 구성?
        assert "Hello".isalpha() == True
        assert "Hello123".isalpha() == False

        # 알파벳 또는 숫자?
        assert "Hello123".isalnum() == True
        assert "Hello 123".isalnum() == False  # 공백 포함

        # 공백으로만 구성?
        assert "   ".isspace() == True
        assert " a ".isspace() == False

        # 대문자/소문자?
        assert "HELLO".isupper() == True
        assert "hello".islower() == True


