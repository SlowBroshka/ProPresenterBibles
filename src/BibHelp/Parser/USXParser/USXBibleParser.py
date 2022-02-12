import pathlib

import bs4.element
from bs4 import BeautifulSoup

from src.BibHelp.Bible import Bible
from src.BibHelp.BiblePart import Book
from src.BibHelp.BiblePart import Verse
from src.BibHelp.BiblePart import Chapter
from src.BibHelp.Parser.USXParser.USXBiblePartParsers import chapterParser, verseParser


class USXBibleParser:

    def __init__(self):
        self.__bible = Bible()

        self.__chapter_parser = chapterParser
        self.__verse_parser = verseParser

    @staticmethod
    def book_name(soup: BeautifulSoup) -> str:
        title = soup.find_all('para', attrs={'style': 'h'})
        if len(title) == 0:
            raise ValueError(f'Can\'t find book\n---SOUP--- {soup}\n---SOUP---\n')

        # Some fragile
        return title[0].text

    @staticmethod
    def __simplify_content(soup: BeautifulSoup) -> list:
        content = soup.find_all(['chapter', 'para'])
        if len(content) > 0:
            return content
        else:
            return ['']

    @staticmethod
    def __beautify_verse(verse: Verse) -> Verse:
        # Avoid '< >' because verse can be used in usx (xml) format
        tmp = verse.content.replace('<', '[')
        tmp = tmp.replace('>', ']')
        verse.content = tmp
        return verse

    def __parse_line(self, line: bs4.element.Tag):
        if line.name == 'chapter':
            print(f'Add chapter: [{line}]')
            chapter_num = int(line.attrs.get('number'))
            self.__bible.add_chapter(Chapter(chapter_num))
            # if res := self.__verse_parser.match(line):
            #     new_verse = self.__verse_parser.from_reg_match(res)
            #
            #     new_verse = USXBibleParser.__beautify_verse(new_verse)
            #
            #     self.__bible.add_verse(new_verse)
            #     return
            return

    def __fill_book(self, soup: BeautifulSoup):
        cleared_content = USXBibleParser.__simplify_content(soup)
        for line in cleared_content:
            self.__parse_line(line)

    def parse_book(self, book_path: str):
        with open(book_path, 'rb') as fp:
            soup = BeautifulSoup(fp, features='html.parser', from_encoding='cp1251')

            book_name = USXBibleParser.book_name(soup)
            print(book_name)

            try:
                self.__bible.add_book(Book(book_name))
                self.__fill_book(soup)
            except NameError as err:
                print(f'{err}, skipped')
            except Exception as err:
                print(f'{err}, UNEXPECTED ERROR')

    def parse_all(self, path: str):
        for f_book in pathlib.Path(path).glob('*.usx'):
            self.parse_book(str(f_book))

        return self.__bible
