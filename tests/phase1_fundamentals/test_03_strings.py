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


class TestEdgeCases:
    """주의사항 - 자주 하는 실수와 함정"""

    def test_string_comparison_gotcha(self):
        """문자열 비교의 함정"""
        # == 는 값을 비교
        a = "hello"
        b = "hello"
        assert a == b  # 값이 같음

        # is 는 객체 동일성을 비교 (메모리 주소)
        # 짧은 문자열은 Python이 최적화해서 같은 객체를 재사용할 수 있음
        # 하지만 이것에 의존하면 안 됩니다!
        c = "hello world " * 100
        d = "hello world " * 100
        assert c == d  # 값은 같음
        # c is d 는 True일 수도 False일 수도 있음 (구현에 따라 다름)

        # 결론: 문자열 비교는 항상 == 사용!

    def test_empty_string_vs_none(self):
        """빈 문자열과 None의 차이"""
        empty = ""
        none_value = None

        # 빈 문자열은 문자열이다!
        assert type(empty) == str
        assert len(empty) == 0

        # None은 "값이 없음"을 나타내는 특별한 객체
        assert none_value is None

        # bool 변환 시 둘 다 False
        assert bool(empty) == False
        assert bool(none_value) == False

        # 하지만 다른 것이다!
        assert empty is not None
        assert empty != None  # 둘은 다름

        # 공백만 있는 문자열도 주의!
        # strip() 후 bool로 체크하면 실제 내용 유무 확인 가능
        spaces_only = "   "
        assert bool(spaces_only) == True  # 공백도 문자!
        assert bool(spaces_only.strip()) == False  # 내용은 없음

    def test_string_multiplication(self):
        """문자열 곱셈 - 반복 생성"""
        # 문자열 * 숫자 = 반복
        repeated = "Ha" * 3
        assert repeated == "HaHaHa"

        # 0이나 음수를 곱하면 빈 문자열
        assert "Hello" * 0 == ""
        assert "Hello" * -1 == ""

        # 구분선 만들 때 유용!
        separator = "-" * 20
        assert len(separator) == 20

    def test_string_concatenation_performance(self):
        """문자열 연결 성능 주의사항"""
        # 반복문에서 + 연결은 비효율적!
        # (매번 새 문자열 객체를 생성하기 때문)

        # 비효율적인 방법 (이렇게 하지 마세요)
        # result = ""
        # for i in range(1000):
        #     result += str(i)  # 매번 새 객체 생성

        # 효율적인 방법: join 사용
        numbers = [str(i) for i in range(10)]
        result = "".join(numbers)
        assert result == "0123456789"

        # 또는 리스트에 모았다가 한번에 join
        parts = []
        for i in range(5):
            parts.append(str(i))
        result = "-".join(parts)
        assert result == "0-1-2-3-4"

    def test_unicode_and_length(self):
        """유니코드와 문자열 길이"""
        # Python 3는 유니코드를 기본 지원!
        korean = "안녕하세요"
        emoji = "😀🎉🐍"

        # len()은 문자 개수를 반환 (바이트가 아님!)
        assert len(korean) == 5  # 5글자
        assert len(emoji) == 3  # 3개의 이모지

        # 한글 인덱싱도 정상 작동
        assert korean[0] == "안"
        assert korean[-1] == "요"

    def test_none_string_operations(self):
        """None과 문자열 연산 - TypeError 주의"""
        name = None

        # None과 문자열을 직접 연결하면 에러!
        # message = "Hello, " + name  # TypeError 발생!

        # 안전한 방법 1: 조건 검사
        if name is not None:
            message = "Hello, " + name
        else:
            message = "Hello, Guest"
        assert message == "Hello, Guest"

        # 안전한 방법 2: or 연산자 활용
        name = None
        safe_name = name or "Guest"  # None이면 "Guest" 사용
        message = f"Hello, {safe_name}"
        assert message == "Hello, Guest"


class TestTips:
    """꿀팁 - 알아두면 유용한 것들"""

    def test_f_string_debugging(self):
        """f-string 디버깅 팁 (Python 3.8+)"""
        x = 42
        name = "test"

        # = 를 붙이면 변수명과 값을 함께 출력!
        debug = f"{x=}"
        assert debug == "x=42"

        debug = f"{name=}"
        assert debug == "name='test'"

        # 표현식도 가능
        debug = f"{x * 2=}"
        assert debug == "x * 2=84"

    def test_string_alignment(self):
        """문자열 정렬과 패딩 - 표 형식 출력에 유용"""
        text = "Hi"

        # ljust(): 왼쪽 정렬, 나머지는 채움 문자로
        assert text.ljust(5) == "Hi   "  # 기본은 공백
        assert text.ljust(5, "-") == "Hi---"

        # rjust(): 오른쪽 정렬
        assert text.rjust(5) == "   Hi"
        assert text.rjust(5, "0") == "000Hi"

        # center(): 가운데 정렬
        assert text.center(6) == "  Hi  "
        assert text.center(6, "*") == "**Hi**"

        # zfill(): 숫자 앞에 0 채우기 (rjust의 특수 버전)
        assert "42".zfill(5) == "00042"
        assert "-42".zfill(5) == "-0042"  # 부호는 앞에 유지!

        # f-string으로도 정렬 가능
        num = 42
        assert f"{text:<5}" == "Hi   "  # 왼쪽 정렬
        assert f"{text:>5}" == "   Hi"  # 오른쪽 정렬
        assert f"{text:^6}" == "  Hi  "  # 가운데 정렬
        assert f"{num:05d}" == "00042"  # 0으로 패딩

    def test_string_partition(self):
        """partition - split보다 정교한 분리"""
        email = "user@example.com"

        # partition(): 구분자 기준으로 3등분
        # (앞부분, 구분자, 뒷부분) 튜플 반환
        before, sep, after = email.partition("@")
        assert before == "user"
        assert sep == "@"
        assert after == "example.com"

        # 구분자가 없으면 (원본, '', '') 반환
        text = "hello"
        before, sep, after = text.partition("@")
        assert before == "hello"
        assert sep == ""
        assert after == ""

    def test_string_translate(self):
        """translate - 문자 치환 테이블"""
        # 여러 문자를 한번에 치환할 때 유용
        text = "Hello, World!"

        # str.maketrans()로 치환 테이블 생성
        # 첫번째 인자의 문자를 두번째 인자의 문자로 치환
        table = str.maketrans("aeiou", "12345")
        result = text.translate(table)
        assert result == "H2ll4, W4rld!"

        # 세번째 인자는 삭제할 문자
        table = str.maketrans("", "", "aeiou")  # 모음 삭제
        result = text.translate(table)
        assert result == "Hll, Wrld!"

    def test_splitlines(self):
        """splitlines - 줄 단위로 분리"""
        text = "첫째줄\n둘째줄\r\n셋째줄"

        # splitlines()는 모든 종류의 줄바꿈을 처리
        # (\n, \r\n, \r 등)
        lines = text.splitlines()
        assert lines == ["첫째줄", "둘째줄", "셋째줄"]

        # keepends=True로 줄바꿈 문자 유지
        lines = text.splitlines(keepends=True)
        assert lines == ["첫째줄\n", "둘째줄\r\n", "셋째줄"]

    def test_removeprefix_removesuffix(self):
        """removeprefix/removesuffix - 접두사/접미사 제거 (Python 3.9+)"""
        filename = "test_data.csv"

        # 접두사 제거
        without_prefix = filename.removeprefix("test_")
        assert without_prefix == "data.csv"

        # 접미사 제거
        without_suffix = filename.removesuffix(".csv")
        assert without_suffix == "test_data"

        # 매칭되지 않으면 원본 그대로 반환
        unchanged = filename.removeprefix("hello")
        assert unchanged == "test_data.csv"

    def test_multiple_replace(self):
        """여러 문자열 한번에 치환하기"""
        text = "Hello, World! Hello, Python!"

        # 방법 1: replace 체이닝
        result = text.replace("Hello", "Hi").replace("World", "Earth")
        assert result == "Hi, Earth! Hi, Python!"

        # 방법 2: 딕셔너리로 관리 (많은 치환이 필요할 때)
        replacements = {"Hello": "Hi", "World": "Earth", "Python": "Universe"}
        result = text
        for old, new in replacements.items():
            result = result.replace(old, new)
        assert result == "Hi, Earth! Hi, Universe!"

    def test_string_check_content(self):
        """문자열 내용 검사 실용 예제 - 실무에서 자주 쓰는 패턴"""
        # 이메일 간단 검증 (in 연산자 조합)
        email = "user@example.com"
        is_valid_email = "@" in email and "." in email
        assert is_valid_email == True

        # 파일 확장자 확인 (lower + endswith 조합)
        filename = "Document.PDF"
        is_pdf = filename.lower().endswith(".pdf")
        assert is_pdf == True

        # 여러 확장자 한번에 확인
        is_image = filename.lower().endswith((".png", ".jpg", ".gif"))
        assert is_image == False

        # 실제 내용이 있는지 확인 (strip + bool 조합)
        text = "Hello"
        has_content = bool(text.strip())
        assert has_content == True

        empty_or_spaces = "   "
        has_content = bool(empty_or_spaces.strip())
        assert has_content == False
