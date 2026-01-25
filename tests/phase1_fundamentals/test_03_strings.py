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


