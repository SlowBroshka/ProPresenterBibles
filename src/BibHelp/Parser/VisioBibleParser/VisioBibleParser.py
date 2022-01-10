import pathlib
from bs4 import BeautifulSoup

from src.BibHelp.Bible import Bible
from src.BibHelp.BiblePart import Book
from src.BibHelp.Parser.VisioBibleParser.VisioBiblePartParsers import chapterParser, verseParser


class VisioBibleParser:

    def __init__(self):
        self.__bible = Bible()

        self.__chapter_parser = chapterParser
        self.__verse_parser = verseParser

    @staticmethod
    def book_name(soup: BeautifulSoup) -> str:
        title = soup.title
        return title.text

    @staticmethod
    def __simplify_content(soup: BeautifulSoup) -> str:
        content = soup.find_all(['a'])
        if len(content) > 0:
            return content[0].text
        else:
            return ''

    def __parse_line(self, line: str):
        if res := self.__verse_parser.match(line):
            new_verse = self.__verse_parser.from_reg_match(res)
            self.__bible.add_verse(new_verse)
            return
        if res := self.__chapter_parser.match(line):
            new_chapter = self.__chapter_parser.from_reg_match(res)
            self.__bible.add_chapter(new_chapter)
            return

    def __fill_book(self, soup: BeautifulSoup):
        content = VisioBibleParser.__simplify_content(soup)
        for line in content.splitlines():
            self.__parse_line(line)

    def parse_book(self, book_path: str):
        with open(book_path, 'rb') as fp:
            soup = BeautifulSoup(fp, features='html.parser', exclude_encodings='latin-1')

            book_name = VisioBibleParser.book_name(soup)

            try:
                self.__bible.add_book(Book(book_name))
                self.__fill_book(soup)
            except NameError as err:
                print(f'{err}, skipped')
            except Exception as err:
                print(f'{err}, UNEXPECTED ERROR')

    def parse_all(self, path: str):
        for f_book in pathlib.Path(path).glob('*.htm'):
            self.parse_book(str(f_book))

        return self.__bible
