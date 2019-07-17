from typing import Iterator, Tuple, Union, overload


UString = Union[str, 'UnicodeString']


class BreakIterator:
    DONE: int

    @classmethod
    def createCharacterInstance(cls, locale: Locale) -> BreakIterator: ...

    @classmethod
    def createWordInstance(cls, locale: Locale) -> BreakIterator: ...

    @classmethod
    def createSentenceInstance(cls, locale: Locale) -> BreakIterator: ...

    def setText(self, text: UString) -> None: ...

    def first(self) -> int: ...

    def nextBoundary(self) -> int: ...

    def getRuleStatus(self) -> int: ...


class CaseMap:
    @classmethod
    def fold(cls, text: UString, edits: Edits) -> str: ...

    @classmethod
    def toLower(cls, locale: Locale, text: UString, edits: Edits) -> str: ...

    @classmethod
    def toUpper(cls, locale: Locale, text: UString, edits: Edits) -> str: ...

    @classmethod
    def toTitle(cls, locale: Locale, text: UString, edits: Edits) -> str: ...


class Edits:
    def __init__(self): ...

    def getFineIterator(self) -> Iterator[Tuple[bool, int, int, int, int, int]]: ...


class Locale:
    def __init__(self, name: str): ...


class Normalizer2:
    @classmethod
    def getNFCInstance(cls) -> Normalizer2: ...

    @classmethod
    def getNFDInstance(cls) -> Normalizer2: ...

    @classmethod
    def getNFKCInstance(cls) -> Normalizer2: ...

    @classmethod
    def getNFKDInstance(cls) -> Normalizer2: ...

    def normalize(self, text: UString) -> str: ...

    def spanQuickCheckYes(self, text: UString) -> int: ...

    def hasBoundaryBefore(self, c: UString) -> bool: ...


class UnicodeString:
    def __init__(self, string: str): ...

    @overload
    def __getitem__(self, index: int) -> str: ...

    @overload
    def __getitem__(self, index: slice) -> UnicodeString: ...

    def __len__(self) -> int: ...

    @overload
    def countChar32(self) -> int: ...

    @overload
    def countChar32(self, start: int, length: int) -> int: ...

    def charAt(self, index: int) -> int: ...

    def char32At(self, index: int) -> int: ...
