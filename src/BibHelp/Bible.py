import os

from src.BibHelp.BiblePart import *
from src.BibHelp.DBManager import *
from src.BibHelp.BibleMap import *

USX_EXTENSION = '.usx'


class Bible:
    def __init__(self):
        self.db = ...  # type: DBConnection
        self.old_testament = OldTestament()
        self.new_testament = NewTestament()
        self.__curr_book = ...  # type: Book
        self.__curr_chapter = ...  # type: Chapter
        self.__curr_verse = ...  # type: Verse
        self.__curr_testament = self.old_testament

    @classmethod
    def from_usx_folder(self, path_to_usx_folder: str):
        pass

    @classmethod
    def from_db(self, path_to_db: str):
        pass

    def dump_to_usx_format(self, dump_folder: str):
        all_books = self.get_all_books()
        for book in all_books:
            # Check containing in map
            alias = BIBLE_BOOKS_RU_EN_MAP[book.name]
            path_to_file = os.path.join(dump_folder, alias + USX_EXTENSION)

            with open(path_to_file, 'a') as file:
                file.write(f'<?xml version="1.0" encoding="utf-8"?>\n'
                           f'<usx version="2.0">\n'
                           f'  <book code="{alias}" '
                           f'style="id">{book.name}</book>  \n'
                           f'<para style="mt">{book.name}</para>\n')
                for chapter in book.chapters:
                    file.write(f'  <chapter number="{chapter.number}" style="c" />\n')
                    for verse in chapter.verses:
                        file.write(f'  <para style="p">\n'
                                   f'    <verse number="{verse.number}" style="v" />{verse.content}</para>\n')


    def get_all_books(self):
        return self.old_testament.books + self.new_testament.books

    def dump_to_sql(self, path='bible_db.sqlite'):
        self.db = DBConnection(path)
        self.db.create_db_struct()

        # So important to pass equal books in fill_* functions
        all_books = self.get_all_books()
        self.db.fill_books(all_books)
        self.db.fill_chapters(all_books)
        self.db.fill_verses(all_books)

    def modify_sql_for_pp(self):
        self.db.adap_db_for_pp()

    def close(self):
        self.db.close()

    def __add_verse(self, verse: Verse):
        if not self.__curr_chapter:
            raise ValueError(f'Bible empty Chapter. Verse: [{verse.number}]: [{verse.content}]')
        self.__curr_verse = verse
        self.__curr_chapter.add_verse(self.__curr_verse)

    def __add_chapter(self, chapter: Chapter):
        if not self.__curr_book:
            raise ValueError(f'Bible empty Book. Chapter: [{chapter.number}]')
        self.__curr_chapter = chapter
        self.__curr_book.add_chapter(self.__curr_chapter)

    def __add_book(self, book: Book):
        if not self.__curr_testament:
            raise ValueError(f'Bible empty Testament. Book: [{book.name}]')
        self.__curr_book = book
        self.__curr_testament.add_book(self.__curr_book)

    def __add_testament(self, testament: Testament):
        if testament.name == self.old_testament.name:
            self.__curr_testament = self.old_testament
        elif testament.name == self.new_testament.name:
            self.__curr_testament = self.new_testament
        else:
            raise ValueError(f'Bible wrong Testament. Testament: [{testament.name}]')

    def parse_line(self, line: str):
        if res := BiblePart.verse.match(line):
            new_verse = Verse.from_reg_exp(res)
            self.__add_verse(new_verse)
            return

        if res := BiblePart.chapter.match(line):
            new_chapter = Chapter.from_reg_exp(res)
            self.__add_chapter(new_chapter)
            return

        if res := BiblePart.testament.match(line):
            new_testament = Testament.from_reg_exp(res)
            self.__add_testament(new_testament)
            return

        if res := BiblePart.book.match(line):
            new_book = Book.from_reg_exp(res)
            self.__add_book(new_book)
            return
