import io
import pathlib

from src.BibHelp.Bible import Bible
from src.BibHelp.Parser.IBiblePartParser import IBiblePartParser
from src.BibHelp.BookStructure.Book import Book
from src.BibHelp.BookStructure.Chapter import Chapter
from src.BibHelp.BookStructure.Verse import Verse
from src.BibHelp.BookStructure.Testament import Testament


class BibleParser:

    def __init__(self, parser: IBiblePartParser):
        self.__bible = Bible()
        self.__parser = parser

    def parse_all(self, path: str) -> Bible:
        with io.open(path, encoding='utf-8') as reader:
            for line in reader:
                self.parse_line(line)
        return self.__bible

    def parse_all_dir(self, path: str, filter: str) -> Bible:
        for f_book in pathlib.Path(path).glob(filter):
            with io.open(f_book, encoding='utf-8') as reader:
                for line in reader:
                    self.parse_line(line)

        return self.__bible

    def parse_line(self, line: str):
        if res := self.__parser.verse_parser().match(line):
            new_verse = self.__parser.verse_parser().from_reg_match(res)
            new_verse.__class__ = Verse
            self.__bible.add_verse(new_verse)
            return

        if res := self.__parser.chapter_parser().match(line):
            new_chapter = self.__parser.chapter_parser().from_reg_match(res)
            new_chapter.__class__ = Chapter
            self.__bible.add_chapter(new_chapter)
            return

        if res := self.__parser.testament_parser().match(line):
            new_testament = self.__parser.testament_parser().from_reg_match(res)
            new_testament.__class__ = Testament
            self.__bible.add_testament(new_testament)
            return

        if res := self.__parser.book_parser().match(line):
            new_book = self.__parser.book_parser().from_reg_match(res)
            new_book.__class__ = Book
            self.__bible.add_book(new_book)
            return
