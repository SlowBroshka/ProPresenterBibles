from src.BibHelp.BookStructure import Book
from src.BibHelp.BookStructure import Chapter
from src.BibHelp.BookStructure.Verse import Verse
from src.BibHelp.BookStructure.Testament import NewTestament, OldTestament, Testament


class Bible:
    def __init__(self):
        self.old_testament = OldTestament()
        self.new_testament = NewTestament()

        self.__curr_book = ...  # type: Book
        self.__curr_chapter = ...  # type: Chapter
        self.__curr_verse = ...  # type: Verse
        self.__curr_testament = self.old_testament

    def from_usx_folder(self, path_to_usx_folder: str):
        pass

    def from_db(self, path_to_db: str):
        pass

    def get_all_books(self):
        return self.old_testament.books + self.new_testament.books

    def print_all_books_info(self):
        all_books = self.get_all_books()
        for book in all_books:
            print(f'[INFO]: {book.info()}')

    def add_verse(self, verse: Verse):
        if not self.__curr_chapter:
            raise ValueError(f'Bible empty Chapter. Verse: [{verse.number}]: [{verse.content}]')
        self.__curr_verse = verse
        self.__curr_chapter.add_verse(self.__curr_verse)

    def add_chapter(self, chapter: Chapter):
        if not self.__curr_book:
            raise ValueError(f'Bible empty Book. Chapter: [{chapter.number}]')
        self.__curr_chapter = chapter
        self.__curr_book.add_chapter(self.__curr_chapter)

    def add_book(self, book: Book):
        if not self.__curr_testament:
            raise ValueError(f'Bible empty Testament. Book: [{book.name}]')
        self.__curr_book = book
        self.__curr_testament.add_book(self.__curr_book)

    def add_testament(self, testament: Testament):
        if testament.name == self.old_testament.name:
            self.__curr_testament = self.old_testament
        elif testament.name == self.new_testament.name:
            self.__curr_testament = self.new_testament
        else:
            raise ValueError(f'Bible wrong Testament. Testament: [{testament.name}]')

    def parse_line(self, line: str):
        if res := self.__parser.verse.match(line):
            new_verse = Verse.from_reg_exp(res)
            self.__add_verse(new_verse)
            return

        if res := self.__parser.chapter.match(line):
            new_chapter = Chapter.from_reg_exp(res)
            self.__add_chapter(new_chapter)
            return

        if res := self.__parser.testament.match(line):
            new_testament = Testament.from_reg_exp(res)
            self.__add_testament(new_testament)
            return

        if res := self.__parser.book.match(line):
            new_book = Book.from_reg_exp(res)
            self.__add_book(new_book)
            return
