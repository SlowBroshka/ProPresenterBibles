import re
from src.BibHelp.BookStructure.BiblePart import BiblePart
from src.BibHelp.BookStructure.Book import Book
from src.BibHelp.BibleMap import BookNameManager


class Testament(BiblePart):
    def __init__(self):
        self.name = str()
        self.books = list()

    def __sort_books(self):
        self.books = sorted(self.books, key=lambda x: BookNameManager.index_in_bible(x.name.ntc_ru_long))

    def add_book(self, book: Book):
        self.books.append(book)
        self.__sort_books()

    def print(self):
        print(f'[Testament] {self.name}')

    @staticmethod
    def from_reg_exp(math: re.Match):
        text = math.group(1)
        stripped = text.strip()
        if stripped == "Ветхий Завет":
            return OldTestament()
        elif stripped == "Новый Завет":
            return NewTestament()


class OldTestament(Testament):
    def __init__(self):
        super().__init__()
        self.name = "Ветхий Завет"


class NewTestament(Testament):
    def __init__(self):
        super().__init__()
        self.name = "Новый Завет"
