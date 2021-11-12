import re
import io

from abc import ABC, abstractmethod

from src.BibHelp.Bible import Bible
from src.BibHelp.BiblePart import *

class BiblePartParser(ABC):

    @abstractmethod
    def match(self, line: str) -> re.Match:
        pass

    @abstractmethod
    def from_line(self, match: re.Match) -> BiblePart:
        pass

class IBSVerseParser(BiblePartParser):
    __pattern = re.compile(r'^Глава\s+(\d+?)\n$')

    def match(self, line: str) -> re.Match:
        return IBSVerseParser.__pattern.match(line)

    def from_line(self, match: re.Match) -> BiblePart:
        verse_num = int(match.group(1))
        verse_content = match.group(2)
        return Verse(verse_num, verse_content)


class BibleParser(ABC):

    def __init__(self, testament: str, book: str, chapter: str, verse: str):
        self.testament = re.compile(testament)
        self.book = re.compile(book)
        self.chapter = re.compile(chapter)
        self.verse = re.compile(verse)

    @abstractmethod
    def parseAll(self, path: str) -> Bible:
        res_bible = Bible()
        with io.open(path, encoding='utf-8') as reader:
            for line in reader:
                res_bible.parse_line(line)
        return res_bible

    def from_line(self, line: str) -> Verse:
        pass

    def from_line(self, line: str) -> Chapter:
        pass


    def parse_line(self, line: str):
        if res := self.verse.match(line):
            new_verse = Verse.from_reg_exp(res)
            self.__add_verse(new_verse)
            return

        if res := self.chapter.match(line):
            new_chapter = Chapter.from_reg_exp(res)
            self.__add_chapter(new_chapter)
            return

        if res := self.testament.match(line):
            new_testament = Testament.from_reg_exp(res)
            self.__add_testament(new_testament)
            return

        if res := self.book.match(line):
            new_book = Book.from_reg_exp(res)
            self.__add_book(new_book)
            return


    @classmethod
    def verse(cls) -> re.Pattern:
        return self.verse

    @classmethod
    def chapter(cls):
        return cls.chapter

    @classmethod
    def book(cls):
        return cls.book

    @classmethod
    def testament(cls):
        return cls.testament
