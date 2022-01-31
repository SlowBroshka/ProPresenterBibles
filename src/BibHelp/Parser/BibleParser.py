import io

from src.BibHelp.Bible import Bible


class BibleParser:

    def __init__(self, testament_parser, book_parser, chapter_parser, verse_parser):
        self.__bible = Bible()
        self.__testament_parser = testament_parser
        self.__book_parser = book_parser
        self.__chapter_parser = chapter_parser
        self.__verse_parser = verse_parser

    def parse_all(self, path: str) -> Bible:
        with io.open(path, encoding='utf-8') as reader:
            for line in reader:
                self.parse_line(line)
        return self.__bible

    def parse_line(self, line: str):
        if res := self.__verse_parser.match(line):
            new_verse = self.__verse_parser.from_reg_match(res)
            self.__bible.add_verse(new_verse)
            return

        if res := self.__chapter_parser.match(line):
            new_chapter = self.__chapter_parser.from_reg_match(res)
            self.__bible.add_chapter(new_chapter)
            return

        if res := self.__testament_parser.match(line):
            new_testament = self.__testament_parser.from_reg_match(res)
            self.__bible.add_testament(new_testament)
            return

        if res := self.__book_parser.match(line):
            new_book = self.__book_parser.from_reg_match(res)
            self.__bible.add_book(new_book)
            return
